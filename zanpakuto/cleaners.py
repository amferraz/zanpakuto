# -*- coding: utf-8 -*-

from lxml.html import clean
from lxml.html.diff import block_level_tags, block_level_container_tags

tags_begin_paragraph = (block_level_tags +
                        block_level_container_tags +
                        ('br',))


default_cleaner = clean.Cleaner(
    page_structure=False,
    remove_unknown_tags=False,
    allow_tags=['blockquote', 'a', 'em', 'p', 'strong',
                'h3', 'h4', 'h5', 'ul', 'ol', 'li', 'sub', 'sup',
                'abbr', 'acronym', 'dl', 'dt', 'dd', 'cite',
                'dft', 'br', 'table', 'tr', 'td', 'th', 'thead',
                'tbody', 'tfoot', 'div', 'span'],
    safe_attrs=frozenset(['href']),
    safe_attrs_only=True,
    add_nofollow=True,
    scripts=True,
    javascript=True,
    comments=False,
    style=True,
    links=False,
    meta=False,
    processing_instructions=False,
    frames=False,
    annoying_tags=False
)


__all__ = ['default_cleaner', 'tags_begin_paragraph']
