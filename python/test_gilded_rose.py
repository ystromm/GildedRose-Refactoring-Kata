# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def empty_should_return_empty(self):
        items = []
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([], gilded_rose.items)


if __name__ == '__main__':
    unittest.main()
