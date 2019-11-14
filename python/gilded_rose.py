# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        self.items = [self._update_quality_for_item(item) for item in self.items]

    def _update_quality_for_item(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            return _update_quality_for_sulfurus(item)
        elif item.name == "Aged Brie":
            return _update_quality_for_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return _update_quality_for_backstage_pass(item)
        else:
            return _update_quality_for_other(item)

def _update_quality_for_sulfurus(item):
    return Item(item.name, item.sell_in, 80)

def _update_quality_for_aged_brie(item):
    sell_in = item.sell_in - 1
    quality = item.quality
    if quality < 50:
        quality = quality + 1
    if sell_in < 0:
        if quality < 50:
            quality = quality + 1
    return Item(item.name, sell_in, quality)

def _update_quality_for_backstage_pass(item):
    sell_in = item.sell_in - 1
    quality = item.quality
    if quality < 50:
        quality = quality + 1
        if sell_in < 11:
            if quality < 50:
                quality = quality + 1
        if sell_in < 6:
            if quality < 50:
                quality = quality + 1
    if sell_in < 0:
        quality = 0
    return Item(item.name, sell_in, quality)

def _update_quality_for_other(item):
    sell_in = item.sell_in - 1
    quality = item.quality
    if quality > 0:
        quality = item.quality - 1
    if sell_in < 0:
        if quality > 0:
            quality = quality - 1
    return Item(item.name, sell_in, quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
