import qrcode
import io
import base64


error_correct_map = {
    '~7%': qrcode.constants.ERROR_CORRECT_L,
    '~15%': qrcode.constants.ERROR_CORRECT_M,
    '~25%': qrcode.constants.ERROR_CORRECT_Q,
    '~30%': qrcode.constants.ERROR_CORRECT_H,
}


def get_qrcode_img(data, error_correction='~15%'):
    # make qrcode
    qr = qrcode.QRCode(
        error_correction=error_correct_map[error_correction],
    )
    qr.add_data(data)
    qr.make()

    # stream img
    qr_img = qr.make_image()
    stream = io.BytesIO()
    qr_img.save(stream, 'PNG')

    # make img tag from stream
    img_src = 'data: image/png;base64, ' + \
        base64.b64encode(stream.getvalue()).decode('utf-8')
    qr_html = '<img src="{}" />'.format(img_src)

    return qr_html
