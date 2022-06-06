import re

from frappe.utils.pdf import get_pdf as frappe_get_pdf


def get_pdf(html, options=None):
    """
    Args:
        html(str): pdf content
        options(dict):
            margin(int): page margin in mm
            page-height(int): page height in mm
            page-width(int): page width in mm
    """
    # parse pdf option from html
    # we use special format in html
    # sample: margin:10mm||
    options = {} if options is None else options
    for attr in ('margin', 'page-height', 'page-width'):
        try:
            match = re.search(
                r'{}:(.+)\|\|'.format(attr),
                html
            )
            if match:
                val = str(match.group(1)).strip()
                if attr == 'margin':
                    options['margin-right'] = val
                    options['margin-left'] = val
                    options['margin-top'] = val
                    options['margin-bottom'] = val
                else:
                    options[attr] = val
        except Exception:
            pass

    return frappe_get_pdf(html, options)
