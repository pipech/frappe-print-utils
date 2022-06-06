## :printer: [WIP] Print Utils

Print Utilities for Frappe Framework

### Installation

```
bench get-app print_utils https://github.com/pipech/frappe-print-utils
bench install-app print_utils
```

### Usage

### Python Function

```python
from print_utils.layout import get_print_layout

html = get_print_layout(
  content=body,
)
```

#### Jinja Templating

```jinja
{{ get_qrcode_img("your_barcode_data", error_correction='~15%') }}
{{ get_barcode_img(data="5901234123457", barcode_class="ean13") }}
```

#### License

MIT
