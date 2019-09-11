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


class Romp(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    git = "https://github.com/zygyz/romp-v2.git" 
    # FIXME: Add proper versions and checksums here.
    version('experimental', branch='experimental')
    version('develop', branch='master')
    # version('1.2.3', '0123456789abcdef0123456789abcdef')
     
    depends_on('boost')
    depends_on('dyninst')
    depends_on('gflags')
    depends_on('glog')
    depends_on('gperftools')
    depends_on('llvm-openmp') 

    def cmake_args(self):
        spec = self.spec
        args = [
             '-DCMAKE_CXX_FLAGS=%s' % '-std=c++11',
        ]
        return args 
