#!/usr/bin/env python
# coding: utf-8

import unittest

import feed2maildir.reader

class ReaderTestCase(unittest.TestCase):
    def test_read_no_feeds(self):
        testfeed = {}
        reader = feed2maildir.reader.Reader(testfeed)
        self.assertEqual(reader.feeds, {})

    def test_read_my_blog(self):
        testfeed = {'Blog': 'https://sulami.github.io/feed/rss.xml'}
        reader = feed2maildir.reader.Reader(testfeed)
        self.assertIsNotNone(reader.feeds['Blog'])

if __name__ == '__main__':
    unittest.main()
