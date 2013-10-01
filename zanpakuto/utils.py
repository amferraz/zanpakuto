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


def append_element(text, tag, on_tree):
    new_element = lxml.etree.SubElement(on_tree, tag)
    new_element.text = text


def simplify_html(html_excerpt, root=None):

    # clean document
    document = lxml.html.fromstring(html_excerpt)
    cleaned_document = default_cleaner.clean_html(document)

    # restructuring output
    if not root:
        root = lxml.etree.Element("root")

    subelements_iter = cleaned_document.iter()
    accum_text = ''
    previous_tail = ''

    for cur_element in subelements_iter:
        cur_tag = cur_element.tag

        if accum_text and marks_new_paragraph(cur_tag):
            append_element(accum_text, 'p', root)
            accum_text = ''

        if previous_tail:
            append_element(previous_tail, 'p', root)
            previous_tail = ''

        if cur_element.text:
            accum_text += cur_element.text

        if cur_element.tail and not marks_new_paragraph(cur_tag):
            accum_text += cur_element.tail
        elif cur_element.tail and marks_new_paragraph(cur_tag):
            previous_tail = cur_element.tail

    # for the possible last pieces of text
    if accum_text:
        append_element(accum_text, 'p', root)

    if previous_tail:
        append_element(previous_tail, 'p', root)

    # the concatenation of the children, to ignore outer tag
    output_text = six.u('').join(map(lxml.html.tostring, root.iterchildren()))
    return output_text


__all__ = ['strip_html', 'simplify_html']
