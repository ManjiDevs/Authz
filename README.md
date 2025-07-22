# AuthZ

A simple Python module to verify bot authorization via API.

## Usage

```python
from authz import id

if id("1893701490", "123:TOKEN", "mybot"):
    print("Authorized")
else:
    print("Unauthorized")