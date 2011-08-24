qrqit
-----

Simple binding of qrencode library released under the public domain
extracted from qurl. This is a quick and dirty extraction from a code.


Requirements
++++++++++++

To build the binding you will need to install:

 - `libqrencode-dev <apt://libqrencode-dev>`_
 - `Cython <apt://cython>`_

To use it you will need:

 - `Python Imaging Librairy <apt://python-imaging>`_


Installation
++++++++++++

Do one of this command to install it from pypi

::

    pip install qrkit

or::

    easy_install qrkit

From code::
   
   $ python setup.py install


Note: if you get an error on MacOSX try to install with the following
arguments:

    $ env ARCHFLAGS="-arch i386 -arch x86_64" python setup.py install


Simple usage
++++++++++++

::
    
    from qrimage.qrimg import encode_to_img
    
    img = encode_to_img('http://www.python.org/', width=300, border=10)
    img.save('qrimage.png', 'PNG', quality=80)
