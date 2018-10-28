#!/bin/bash - 
#===============================================================================
#
#          FILE: setup.sh
# 
#   DESCRIPTION: Setup C++ env 
# 
#       CREATED: 2018-10-28
#
#        AUTHOR: Anthony Dervish
#
#===============================================================================

set -o nounset                              # Treat unset variables as an error

cd build
conan install ..
cmake -DCMAKE_BUILD_TYPE=Debug ..
make install

