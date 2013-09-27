# -*- coding: utf-8 -*-

import six
import lxml

from cleaners import default_cleaner, tags_begin_paragraph


def strip_html(html_excerpt):
    """Strips HTML tags.

    :param html_excerpt: the HTML excerpt to be stripped
    :type html_excerpt: str
    :returns:  str -- the stripped HTML

    """
    tree = lxml.html.fromstring(html_excerpt)
    tree = lxml.html.clean.clean_html(tree)
    text = tree.text_content()
    text = text.strip()
    return text


def marks_new_paragraph(tag):
    return tag in tags_begin_paragraph


def simplify_html(html_excerpt, root=None):

    # clean document
    document = lxml.html.fromstring(html_excerpt)
    cleaned_document = default_cleaner.clean_html(document)

    # restructuring output
    if not root:
        root = lxml.etree.Element("root")

    subelements_iter = cleaned_document.iter()
    previous_accum_text = ''
    previous_tail = ''

    for cur_element in subelements_iter:
        cur_tag = cur_element.tag

        if previous_accum_text and marks_new_paragraph(cur_tag):
            new_p = lxml.etree.SubElement(root, "p")
            new_p.text = previous_accum_text
            previous_accum_text = ''

        if previous_tail:
            new_p = lxml.etree.SubElement(root, "p")
            new_p.text = previous_tail
            previous_tail = ''

        if cur_element.text:
            previous_accum_text += cur_element.text

        if cur_element.tail and not marks_new_paragraph(cur_tag):
            previous_accum_text += cur_element.tail
        elif cur_element.tail and marks_new_paragraph(cur_tag):
            previous_tail = cur_element.tail

    # for the possible last pieces of text
    if previous_accum_text:
        new_p = lxml.etree.SubElement(root, "p")
        new_p.text = previous_accum_text

    if previous_tail:
        new_p = lxml.etree.SubElement(root, "p")
        new_p.text = previous_tail
        previous_tail = ''

    # the concatenation of the children, to ignore outer tag
    output_text = six.u('').join(map(lxml.html.tostring, root.iterchildren()))
    return output_text


__all__ = ['strip_html', 'simplify_html']
