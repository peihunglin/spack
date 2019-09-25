# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class LlvmOpenmp(CMakePackage):
    """The OpenMP subproject of LLVM contains the components required to build
    an executable OpenMP program that are outside the compiler itself."""

    homepage = "https://openmp.llvm.org/"
    git      = "https://github.com/zygyz/openmp.git"
#    url      = "https://releases.llvm.org/8.0.0/openmp-8.0.0.src.tar.xz"

#    version('8.0.0', sha256='f7b1705d2f16c4fc23d6531f67d2dd6fb78a077dd346b02fed64f4b8df65c9d5')
    version('romp-mod', branch='romp-mod2')
    version('debug-ompt', branch='romp-mod2')

    depends_on('cmake@2.8:', type='build')
    
    @when('@debug-ompt')
    def cmake_args(self):
        # Disable LIBOMP_INSTALL_ALIASES, otherwise the library is installed as
        # libgomp alias which can conflict with GCC's libgomp.
        # Also, turn on debug flag for ompt
        return ['-DLIBOMP_INSTALL_ALIASES=OFF', 
                '-DLIBOMP_OMPT_DEBUG=ON',
                '-DLIBOMP_OMPT_SUPPORT=ON',
                '-DLIBOMP_OMPT_OPTIONAL=ON',]

    def cmake_args(self):
        # Disable LIBOMP_INSTALL_ALIASES, otherwise the library is installed as
        # libgomp alias which can conflict with GCC's libgomp.
        return ['-DLIBOMP_INSTALL_ALIASES=OFF',
                '-DLIBOMP_OMPT_SUPPORT=ON',
                '-DLIBOMP_OMPT_OPTIONAL=ON',]

    @property
    def libs(self):
        return find_libraries('libomp', root=self.prefix, recursive=True)
