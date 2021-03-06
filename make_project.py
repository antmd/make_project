#!/usr/bin/env python
from __future__ import print_function
import shutil
import subprocess
import begin
import jinja2
import os
import sys
from os import path
import jinja2
from jinja2 import Environment, FileSystemLoader, StrictUndefined

script_dir = os.path.realpath(os.path.dirname(os.path.realpath(__file__)))
print("script_dir = {}".format(script_dir))
languages_dir = os.path.join(script_dir, 'languages')


def available_languages():
    files = os.listdir(languages_dir)
    return [f for f in files if os.path.isdir(os.path.join(languages_dir, f))]


class Project(object):
    def __init__(self, name, language):
        self.name = name
        self.language = language

def mkdir(name, exist_ok=False):
    try:
        os.makedirs(name)
    except Exception as e:
        if not exist_ok:
            raise e

def copyfile(src, dst, follow_symlinks=False):
    if not follow_symlinks and os.path.islink(src):
        linkto = os.readlink(src)
        os.symlink(linkto, dst)
    else:
        shutil.copy(src,dst)

@begin.start
def main(name, language, project_root=None):
    language_dir = os.path.join(languages_dir, language)

    if not os.path.exists(language_dir):
        print("Language '{}' has no templates. Available languages: {}".format(language,
                                                                               ', '.join(available_languages())),
              file=sys.stderr)
        sys.exit(1)

    if project_root is None:
        mkdir(name, exist_ok=True)
        project_root = name

    language_dir = os.path.realpath(language_dir)
    project_root = os.path.realpath(project_root)

    project = Project(name, language)

    template_loader = FileSystemLoader([language_dir, '/'])
    env = Environment(
        loader=template_loader
        , trim_blocks=True
        , lstrip_blocks=True
        , undefined=StrictUndefined
    )

    template_files_dir = os.path.join(language_dir, 'files')

    if os.path.exists(template_files_dir):
        for base, dirs, files in os.walk(template_files_dir):

            rdir = os.path.relpath(base, template_files_dir)
            ndir = os.path.join(project_root, rdir)
            os.chdir(ndir)

            for d in dirs:
                mkdir(d, exist_ok=True)

            for file in files:
                src = os.path.join(template_files_dir, rdir, file)
                se = os.path.splitext(file)
                if se[1] == '.jinja':
                    dest = os.path.join(os.getcwd(), se[0])
                    if os.path.exists(dest):
                        os.unlink(dest)
                    print("Expanding {} -> {}".format(src, dest))
                    template = env.get_template(src)

                    try:
                        out = template.render(project=project)
                        out_path = path.join(dest)
                        with open(out_path, "w") as out_fh:
                            print(out, file=out_fh)

                    except jinja2.exceptions.UndefinedError as ex:
                        print("\nERROR: Undefined attribute: {}".format(ex.message), file=sys.stderr)
                        print(
                            "You can define template variables using a semi-colon-separated list of <KEY>=<VALUE> as the value of the --defines flag.",
                            file=sys.stderr)

                else:
                    dest = os.path.join(os.getcwd(), file)
                    if os.path.lexists(dest):
                        os.unlink(dest)
                    print("Copying {} -> {}".format(src, dest))
                    copyfile(src, dest, follow_symlinks=False)

        setup_file = path.join(language_dir, 'setup.py') if path.exists(path.join(language_dir, 'setup.py')) else \
            path.join(language_dir, 'setup.sh') if path.exists(path.join(language_dir, 'setup.sh')) else \
            path.join(language_dir, 'setup') if path.exists(path.join(language_dir, 'setup')) else None

        if setup_file:
            print("Running {}".format(setup_file))
            environ = {'PATH':os.getenv('PATH')
                       , 'HOME': os.getenv('HOME')
                       , 'PROJECT_DIR': project_root
                       }
            subprocess.call(setup_file, env=environ, cwd=project_root)
