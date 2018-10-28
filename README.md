# make_project
Create simple projects, easily. For C++, etc.

e.g.

```
make_project.py MyExperiment cpp
cd MyExperiment
vim main.cpp
... develop stuff ...
```

Sometimes, you want to get started on a small project or an experiment without spending time creating a build environment. You still want to take advantage of the tools available, but those tools need configuration. Maybe you have a template project you can duplicate to get started; then all you have to do is change some strings and you can get started.

make_project contains example templates (for C++ only, at the moment), and simplifies the duplication and string substitution so you can get started on your project.

The C++ project template sets up a conan/CMake build environment, and configures clang-format and YouCompleteMe.

make_project takes a hierarchy of files (the source hierarchy) selected by language (e.g. 'cpp' for C++), and creates a new folder of files (the destination hierarchy), mirroring the source hierarchy. The following rules are applied during the copy:

1. For files ending in `.jinja`, the file is passed through Jinja2, where special variables are substituted out. The resulting file is written without the `.jinja` file extension to the destination hierarchy.
2. For files not ending in `.jinja` the file is simply copied to the destination hierarchy.

At the moment, the only variables expanded by Jinja2 are:

* `project`
  * `name` -- the original name given on the command-line
  * `language` -- the language given on the command-line
  
Pull requests are welcome.
