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
DefaultBuildType=Debug
DefaultToolchainFile="${HOME}/.local/share/cmake/default_toolchain"
declare -a args
if [[ -e "$DefaultToolchainFile" ]]; then
    args+=(-DCMAKE_TOOLCHAIN_FILE="${DefaultToolchainFile}")
fi
if [[ -n "${DefaultBuildType}" ]]; then
    args+=(-DCMAKE_BUILD_TYPE="${DefaultBuildType}")
fi
cmake ${args[@]+"${args[@]}"} ..
make install

