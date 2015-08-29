qrkit
-----

Simple binding of qrencode library released under the public domain
extracted from qurl.


Requirements
++++++++++++

To build the binding you will need to install:

 - `libqrencode-dev <apt://libqrencode-dev>`_
 - `Cython <apt://cython>`_

To use it you will need either:

 - `Python Imaging Library <http://www.pythonware.com/products/pil/>`_
 - `Pillow <https://pillow.readthedocs.org/>`_


Installation
++++++++++++

Do one of this command to install it from pypi

::

    pip install qrkit

or::

    easy_install qrkit

From code::
   
   $ python setup.py install


Simple usage
++++++++++++

::
    
    from qrkit.qrimg import encode_to_img
    
    img = encode_to_img('http://www.python.org/', width=300, border=10)
    img.save('qrimage.png', 'PNG', quality=80)
