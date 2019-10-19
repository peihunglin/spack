# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install romp
#
# You can edit this file again by typing:
#
#     spack edit romp
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *
import os.path

class Romp(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    git = "https://github.com/zygyz/romp-v2.git" 

    version('experimental', branch='experimental')
    version('develop', branch='master')

    variant('debug_dyninst', default=False,
            description='Build with dyninst debug info')
    variant('debug_ompt', default=False,
            description='Build with debug mode openmp lib')
       
    depends_on('boost')
    depends_on('dyninst@10.1.1', when='~debug_dyninst')
    depends_on('gflags')
    depends_on('glog')
    depends_on('gperftools')
    depends_on('llvm-openmp@debug-ompt', when='+debug_ompt') 
    depends_on('llvm-openmp@romp-mod', when='~debug_ompt') 

    def cmake_args(self):
        spec = self.spec
        args = [
             '-DCMAKE_CXX_FLAGS=%s' % '-std=c++11 -lpthread',
        ]
        cmake_prefix_path = [self.spec['llvm-openmp'].prefix];
        if '+debug_dyninst' in spec:
            args.append('-DCUSTOM_DYNINST=ON')
            # suppose the debug version of dyninst is installed
            # at $HOME/dyninst; pass this path to CMAKE_PREFIX_PATH
            home_dir = os.path.expanduser('~') 
            dyninst_path = os.path.join(home_dir, 'dyninst')
            cmake_prefix_path.append(dyninst_path)
        args.append('-DCMAKE_PREFIX_PATH=' + ';'.join(cmake_prefix_path))
        return args 
