# -*- coding: utf-8 -*-

import unittest

from zanpakuto import strip_html


class TestStripHtmlTags(unittest.TestCase):

    def assert_strip_html(self, html, expected_stripped_html):
        obtained_text = strip_html(html)
        self.assertEqual(expected_stripped_html, obtained_text)

    def test_tag_h1(self):
        html = u"""<h1>Some Text 1</h1>"""
        expected_text = u'Some Text 1'
        self.assert_strip_html(html, expected_text)

    def test_tag_h2(self):
        html = u"""<h2>Some Text 2</h2>"""
        expected_text = u'Some Text 2'
        self.assert_strip_html(html, expected_text)

    def test_tag_p(self):
        html = u"""<p>Some Text 3</p>"""
        expected_text = u'Some Text 3'
        self.assert_strip_html(html, expected_text)

    def test_tags_h1_script(self):
        html = u""" <script>alert('ok');</script><h2>Some Text 4</h2>"""
        expected_text = u'Some Text 4'
        self.assert_strip_html(html, expected_text)
