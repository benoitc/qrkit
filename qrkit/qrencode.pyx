# This file is part of qrkit releasedi in the Public Domain. 
# See the NOTICE for more information.


from libc.stdlib cimport *

cdef extern from "qrencode.h":
    int QR_ECLEVEL_L
    int QR_ECLEVEL_M
    int QR_ECLEVEL_Q
    int QR_ECLEVEL_H
    
    int QR_MODE_NUM
    int QR_MODE_AN
    int QR_MODE_8
    int QR_MODE_KANJI
    
    ctypedef struct QRcode:
        int version
        int width
        unsigned char *data
    
    QRcode* QRcode_encodeString(char *string, int version, int level,
            int hint, int casesensitive)


def encode(char *string, version=5, case_sensitive=True,
        mode=QR_MODE_8, level=QR_MODE_8):
    """ create a QR code from a String """
    
    cdef QRcode *_qrcode

    str_copy = string
    str_copy = str_copy + b'\0'
    try:
        _qrcode = QRcode_encodeString(str_copy, int(version), int(level),
            int(mode), int(case_sensitive))
        qrcode = dict(
                version = _qrcode.version,
                width = _qrcode.width,
                data = _qrcode.data
        )
    finally:
        free(_qrcode)

    return qrcode
   
def to_matrix(qrcode):
    """ Convert a QRcode to a matrix of ones and zeros """

    cdef unsigned char *qdata

    qwidth = qrcode['width']
    qdata = qrcode['data']
    
    # build matrix
    matrix = []
    for y in range(qwidth):
        line = []
        for x in range(qwidth):
            if qdata[y * qwidth + x] % 2:
                line.append(0)
            else:
                line.append(1)
        matrix.append(line)
    return matrix


