# -*- coding: utf-8 -*-

import unittest

from zanpakuto import simplify_html


class TestSimplifyHtmlExcerpt(unittest.TestCase):

    def assert_simplify_html(self, html, expected_stripped_html):
        obtained_html = simplify_html(html)
        self.assertEqual(expected_stripped_html, obtained_html)

    def test_unwrapped_text(self):
        html = u'Some Text 1'
        expected_html = u'<p>Some Text 1</p>'
        self.assert_simplify_html(html, expected_html)

    def test_single_p(self):
        html = u'<p>Some Text 2</p>'
        expected_html = u'<p>Some Text 2</p>'
        self.assert_simplify_html(html, expected_html)

    def test_text_with_one_br(self):
        html = u'Text here<br>And here'
        expected_html = u'<p>Text here</p><p>And here</p>'
        self.assert_simplify_html(html, expected_html)
