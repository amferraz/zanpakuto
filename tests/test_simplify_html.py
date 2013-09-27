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

    def test_text_with_two_brs(self):
        html = u'A<br>B<br>C'
        expected_html = u'<p>A</p><p>B</p><p>C</p>'
        self.assert_simplify_html(html, expected_html)

    def test_text_with_two_consecutive_brs(self):
        html = u'A<br><br>B'
        expected_html = u'<p>A</p><p>B</p>'
        self.assert_simplify_html(html, expected_html)

    def test_p_with_script(self):
        html = u"<script>alert('ok');</script><p>A</p>"
        expected_html = u'<p>A</p>'
        self.assert_simplify_html(html, expected_html)

    def test_html_with_div(self):
        html = u"<div>A</div>"
        expected_html = u'<p>A</p>'
        self.assert_simplify_html(html, expected_html)

    def test_html_with_span(self):
        html = u"A<span>B</span>C"
        expected_html = u'<p>ABC</p>'
        self.assert_simplify_html(html, expected_html)

    def test_html_with_multiple_divs(self):
        html = u"<div>A</div><div>B</div><div>C</div>"
        expected_html = u'<p>A</p><p>B</p><p>C</p>'
        self.assert_simplify_html(html, expected_html)

    def test_html_with_divs_and_span(self):
        html = u"<div>A</div><span>B</span><div>C</div>"
        expected_html = u'<p>AB</p><p>C</p>'
        self.assert_simplify_html(html, expected_html)

    def test_p_with_tail(self):
        html = u"<p>A</p>B<p>C</p>"
        expected_html = u"<p>A</p><p>B</p><p>C</p>"
        self.assert_simplify_html(html, expected_html)

    def test_h1_means_p(self):
        html = u"<p>A</p><h1>B</h1><p>C</p>"
        expected_html = u'<p>A</p><p>B</p><p>C</p>'
        self.assert_simplify_html(html, expected_html)

    def test_multiple_nested_divs(self):
        html = u"A<div><div>B</div><div><div>C</div></div></div><div>D</div>"
        expected_html = u'<p>A</p><p>B</p><p>C</p><p>D</p>'
        self.assert_simplify_html(html, expected_html)
