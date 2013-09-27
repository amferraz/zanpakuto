# zanpakuto

[![Build Status](https://travis-ci.org/amferraz/zanpakuto.png)](http://travis-ci.org/amferraz/zanpakuto)

zanpakuto is a small utility to simplify HTML excerpts. Its main objective is
to normalize weird, deep, non-semantic, stylish portions of HTML containing
text into a cleaner form.

## Examples

### strip_html:

    from zanpakuto import strip_html
    html = "<h1>Some html with <i>italics</i> and <b>bold</b> tags."
    print strip_html(html)

It will output:

    Some html with italics and bold tags.
