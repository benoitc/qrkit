# This file is part of qrkit released in the Public Domain.
# See the NOTICE for more information.

try:
    from PIL.ImageOps import expand as img_expand
    from PIL.Image import frombytes as img_frombytes
except ImportError:
    raise ImportError('Please install PIL or Pillow.')

from qrkit.qrencode import encode, to_matrix


def encode_to_img(data, width=400, border=10):
    if not isinstance(data, bytes):
        raise ValueError("Please use encode bytes to image.")

    if not data or not data.strip(b'\x00'):
        raise ValueError("You cannot encode a null data in a qrcode.")

    qrcode = encode(data)
    matrix = to_matrix(qrcode)

    dotsize = (width - (border * 2)) // qrcode['width']
    realwidth = qrcode['width'] * dotsize

    rawdata = b''
    for row in matrix:
        line = b''
        for col in row:
            line += dotsize * bytes([col * 255])
        rawdata += dotsize * line

    img = img_frombytes('L', (realwidth, realwidth), rawdata)
    return img_expand(img, border, 255)
