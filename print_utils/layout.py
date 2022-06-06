import frappe


def get_print_layout(content, papersize=None, margin=None):
    html = frappe.render_template(
        template='print_utils/templates/print_formats/base/base_template.html.j2',
        context={
            'body': content,
        },
        is_path=True,
    )
    return html
