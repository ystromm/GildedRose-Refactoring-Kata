# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        self.items = [self._update_quality_for_item(item) for item in self.items]

    def _update_quality_for_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return Item(item.name, item.sell_in, item.quality)
        else:
            if item.name == "Aged Brie":
                item.sell_in = item.sell_in - 1
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                return Item(item.name, item.sell_in, item.quality)
            else:
                item.sell_in = item.sell_in - 1
                if item.name != "Backstage passes to a TAFKAL80ETC concert":
                    if item.quality > 0:
                        item.quality = item.quality - 1
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                        if item.name == "Backstage passes to a TAFKAL80ETC concert":
                            if item.sell_in < 11:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                            if item.sell_in < 6:
                                if item.quality < 50:
                                    item.quality = item.quality + 1
                if item.sell_in < 0:
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            item.quality = item.quality - 1
                    else:
                        item.quality = 0
                return Item(item.name, item.sell_in, item.quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
