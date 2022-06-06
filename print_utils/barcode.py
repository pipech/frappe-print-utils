import barcode
from barcode.writer import ImageWriter
import io
import base64


def get_barcode_img(data, barcode_class):
    # make barcode
    barcode_obj = barcode.get_barcode_class(barcode_class)
    barcode_img = barcode_obj(
        data,
        writer=ImageWriter(),
    )

    # stream img
    stream = io.BytesIO()
    barcode_img.write(stream)

    # make img tag from stream
    img_src = 'data: image/png;base64, ' + \
        base64.b64encode(stream.getvalue()).decode('utf-8')
    barcode_html = '<img src="{}" />'.format(img_src)

    return barcode_html
