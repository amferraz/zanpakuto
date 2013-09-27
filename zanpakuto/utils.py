# -*- coding: utf-8 -*-

import six
import lxml

from lxml.html import fromstring
from lxml.html.clean import clean_html
from lxml import etree


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


def simplify_html(html_excerpt, root=None):

    if not root:
        root = etree.Element("root")

    document = fromstring(html_excerpt)

    subelements_iter = document.iter()
    for current_element in subelements_iter:
        p_text = ''

        if current_element.text:
            p_text = p_text + current_element.text
        if current_element.tail:
            p_text = p_text + current_element.tail

        if p_text:
            new_p = etree.SubElement(root, "p")
            new_p.text = p_text

    output_text = six.u('').join(map(lxml.html.tostring, root.iterchildren()))
    return output_text


__all__ = ['strip_html', 'simplify_html']
