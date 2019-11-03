# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        gilded_rose = self.gilded_rose_update_quality([Item("foo", 0, 0)])
        self.assertEqual("foo", gilded_rose.items[0].name)

    def test_empty_should_return_empty(self):
        gilded_rose = self.gilded_rose_update_quality([])
        self.assertEqual([], gilded_rose.items)

    def test_quality_should_decrease(self):
        gilded_rose = self.gilded_rose_update_quality([Item("foo", 1, 1)])
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_quality_should_decrease_double_if_sell_in_has_passed(self):
        gilded_rose = self.gilded_rose_update_quality([Item("foo", 0, 10)])
        self.assertEqual(8, gilded_rose.items[0].quality)

    def test_quality_should_not_become_negative(self):
        gilded_rose = self.gilded_rose_update_quality([Item("foo", 0, 0)])
        self.assertGreaterEqual(0, gilded_rose.items[0].quality)

    def test_sell_in_should_decrease(self):
        gilded_rose = self.gilded_rose_update_quality([Item("foo", 1, 1)])
        self.assertEqual(0, gilded_rose.items[0].sell_in)

    def test_aged_brie_quality_should_increase_in_quality_after_sell_in(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Aged Brie", -1, 1)])
        self.assertEqual(3, gilded_rose.items[0].quality)

    def test_aged_brie_quality_should_increase_in_quality(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Aged Brie", 1, 1)])
        self.assertEqual(2, gilded_rose.items[0].quality)

    def test_aged_brie_quality_should_increase_in_quality_but_not_above_50(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Aged Brie", 1, 50)])
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_sulfuras_quality_should_keep_quality(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Sulfuras, Hand of Ragnaros", 1, 80)])
        self.assertEqual(400, gilded_rose.items[0].quality)

    def test_sulfuras_quality_should_keep_quality(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Sulfuras, Hand of Ragnaros", 1, 80)])
        self.assertEqual(1, gilded_rose.items[0].sell_in)

    def test_backstage_passes_should_increase_in_quality(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 20, 1)])
        self.assertEqual(2, gilded_rose.items[0].quality)

    def test_backstage_passes_should_increase_by_2_in_quality(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 9, 1)])
        self.assertEqual(3, gilded_rose.items[0].quality)

    def test_backstage_passes_should_increase_by_3_in_quality(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 4, 1)])
        self.assertEqual(4, gilded_rose.items[0].quality)

    def test_backstage_passes_should_have_zero_quailty_when_sell_in_is_passed(self):
        gilded_rose = self.gilded_rose_update_quality([Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)])
        self.assertEqual(0, gilded_rose.items[0].quality)

    def gilded_rose_update_quality(self, items):
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        print(gilded_rose.items)
        return gilded_rose

if __name__ == '__main__':
    unittest.main()
