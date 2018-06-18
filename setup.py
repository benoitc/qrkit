# This file is part of qrkit released in the Public Domain.
# See the NOTICE for more information.
import codecs
import os

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

from qrkit import __version__

ext_modules = [Extension("qrkit.qrencode", ["qrkit/qrencode.pyx"],
                         libraries=['qrencode'])]

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="qrkit",
    version=__version__,
    description="Simple QR code kit.",
    long_description=LONG_DESCRIPTION,
    url="http://github.com/benoitc/qrkit",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules,

    packages=['qrkit'],
    requires=['Cython', 'Pillow'],
)
