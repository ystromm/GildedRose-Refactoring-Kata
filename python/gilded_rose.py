# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = 80
            elif item.name == "Aged Brie":
                item.sell_in = item.sell_in - 1
                if item.quality < 50:
                    item.quality += self.quality_delta_aged_brie(item.sell_in)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.sell_in = item.sell_in - 1
                if item.quality < 50:
                    item.quality += 1
                    if item.sell_in < 11:
                        item.quality += 1
                    if item.sell_in < 6:
                        item.quality += 1
                if item.sell_in < 0:
                    item.quality = 0
            else:
                item.sell_in = item.sell_in - 1
                if item.quality > 0:
                    item.quality = item.quality - 1
                if item.sell_in < 0:
                    if item.quality > 0:
                        item.quality = item.quality - 1

    def quality_delta_aged_brie(self, item_sell_in):
        if item_sell_in < 0:
            delta = 2
        else:
            delta = 1
        return delta


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
