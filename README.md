# zanpakuto

[![Build Status](https://travis-ci.org/amferraz/zanpakuto.png)](http://travis-ci.org/amferraz/zanpakuto)

zanpakuto is a small Python library that aims to simplify HTML excerpts. Its
main objective is to normalize weird, deep-nested, non-semantic, stylish
portions of HTML containing text into a cleaner HTML.

This project is makes use of the awesome [lxml](http://lxml.de/) and it is inspired by [htmllaundry](https://github.com/wichert/htmllaundry).

## Usage examples

### strip_html:

```python
from zanpakuto import strip_html
html = "<h1>Some html with <i>italics</i> and <b>bold</b> tags."
print strip_html(html)
```

It will output:

    Some html with italics and bold tags.

### simplify_html
```python
from zanpakuto import simplify_html
html = u"A<div><div>B</div><div><div>C</div></div></div><div>D</div>"
print simplify_html(html)
```

It will output:

```html
<p>A</p><p>B</p><p>C</p><p>D</p>
```

Take a look on `tests` package to more examples.
