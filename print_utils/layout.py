import frappe
from .paper_size import paper_size_map


def get_print_layout(
    content,
    paper_size='A4',
    orientation='Portrait',
    margin=10,
    font_size='14px',
):
    """
    Args:
        content (str): content to be printed in html format
        paper_size (str|dict): standard paper size ('A4', 'Letter', ...)
            or custom paper size in mm {'width': x, 'height': y}
        orientation (str): orientation of the paper ('Portrait' or 'Landscape')
        margin (int): margin in mm
        font_size (str): css font size ('14pt', '14px', ...)

    Return:
        (str): html layout
    """
    # get paper size
    if type(paper_size) == str:
        paper_size = paper_size.upper()
        paper_dimension = paper_size_map.get(paper_size)
        paper_width = paper_dimension.get('mm')[0]
        paper_height = paper_dimension.get('mm')[1]
    else:
        paper_width = paper_size.get('width')
        paper_height = paper_size.get('height')

    # set paper size based on orientation
    orientation = orientation.lower()
    if orientation == 'landscape':
        paper_width, paper_height = paper_height, paper_width

    # render template
    html = frappe.render_template(
        template='print_utils/templates/print_formats/base/base_template.html.j2',
        context={
            'body': content,
            'width': paper_width,
            'height': paper_height,
            'margin': margin,
            'font_size': font_size,
        },
        is_path=True,
    )
    return html
