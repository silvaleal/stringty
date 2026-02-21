The **Stringty** is a Python library for **manipulating file content in a simple way**. either replacing all content or appending new content.

## Installation

```bash
pip install stringty
```

## Replace the entire content

```python
from stringty import Stringty

content = """
a = "ab2c"

print(a)"""

Stringty().rescript("test.py", content)
```

## Append content to the end

```python
from stringty import Stringty

content = """
a = "ab2c"


print(a)"""

Stringty().imprement("test.py", content)
```
