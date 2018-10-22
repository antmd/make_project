# make_project
Create simple projects easily for C++, etc.

This project takes takes a hierarchy of files (the source hierarchy) selected by language (e.g. 'cpp' for C++), and creates a new folder of files (the destination hierarchy), mirroring the source hierarchy. The following rules are applied during the copy:

1. For files ending in `.jinja`, the file is passed through Jinja2, where special variables are substituted out. The resulting file is written without the `.jinja` file extension to the destination hierarchy.
2. For files not ending in `.jinja` the file is simply copied to the destination hierarchy.

At the moment, the only variables expanded by Jinja2 are:

* `project`
  * `name` -- the original name given on the command-line
  * `language` -- the language given on the command-line
  
Pull requests are welcome.
