import barcode
from barcode.writer import ImageWriter
import io
import base64


def get_barcode_img(data, barcode_class, options=None):
    """
    Args:
        data(str): barcode data
        barcode_class(str): barcode class such as ean13
        options(dict): https://python-barcode.readthedocs.io/en/stable/writers.html#common-writer-options

    Return:
        (str): html img tag
    """
    # make barcode
    barcode_obj = barcode.get_barcode_class(barcode_class)
    barcode_img = barcode_obj(
        data,
        writer=ImageWriter(),
    )

    # stream img
    stream = io.BytesIO()
    barcode_img.write(stream, options=options)

    # make img tag from stream
    img_src = 'data: image/png;base64, ' + \
        base64.b64encode(stream.getvalue()).decode('utf-8')
    barcode_html = '<img src="{}" />'.format(img_src)

    return barcode_html
