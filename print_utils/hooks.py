from . import __version__ as app_version

app_name = "print_utils"
app_title = "Print Utils"
app_publisher = "SpaceCode"
app_description = "Print Utilities for Frappe Framework"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "p@spacecode.co.th"
app_license = "MIT"

jinja = {
	"methods": [
		"print_utils.qrcode.get_qrcode_img",
		"print_utils.barcode.get_barcode_img",
	],
}
