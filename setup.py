# -*- coding: utf-8 -
#
# This file is part of qrkit releasedi in the Public Domain. 
# See the NOTICE for more information.


import os

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

from qrkit import __version__

ext_modules = [Extension("qrkit.qrencode", ["qrkit/qrencode.pyx"],
    libraries=['qrencode'])]

setup(
    name ="qrkit",
    version = __version__,

    description = "Simple QR code kit.",

    long_description = file(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        )).read(),
     
    url = "http://github.com/benoitc/qrkit",

    classifiers = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Environment :: Other Environment', 
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,

    packages = ['qrkit'],
)
