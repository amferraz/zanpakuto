# -*- coding: utf-8 -*-

from lxml.html import fromstring
from lxml.html.clean import clean_html


def strip_html(html_excerpt):
    """Strips HTML tags.

    :param html_excerpt: the HTML excerpt to be stripped
    :type html_excerpt: str
    :returns:  str -- the stripped HTML

    """
    tree = fromstring(html_excerpt)
    tree = clean_html(tree)
    text = tree.text_content()
    text = text.strip()
    return text
