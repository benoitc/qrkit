# -*- coding: utf-8 -*-
#
# This file is part of qrkit released in the Public Domain.
# See the NOTICE for more information.

try:
    from PIL.ImageOps import expand as img_expand
    from PIL.Image import fromstring as img_fromstring
except ImportError:
    try:
        from ImageOps import expand as img_expand
        from Image import fromstring as img_fromstring
    except ImportError:
        raise ImportError('Please install PIL or Pillow.')

from qrkit.qrencode import encode, to_matrix


def encode_to_img(string, width=400, border=10):
    qrcode = encode(string)
    matrix = to_matrix(qrcode)

    dotsize = (width - (border * 2)) / qrcode['width']
    realwidth = qrcode['width'] * dotsize

    rawdata = ''
    for row in matrix:
        line = ''
        for col in row:
            line += dotsize * chr(col * 255)
        rawdata += dotsize * line

    img = img_fromstring('L', (realwidth, realwidth), rawdata)
    return img_expand(img, border, 255)
