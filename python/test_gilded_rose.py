# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_empty_should_return_empty(self):
        items = []
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([], gilded_rose.items)

    def test_quality_should_decrease(self):
        items = [Item("foo", 0, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_quality_should_not_become_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertGreaterEqual(0, gilded_rose.items[0].quality)

    def test_sellby_should_decrease(self):
        items = [Item("foo", 1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].sell_in)

if __name__ == '__main__':
    unittest.main()
