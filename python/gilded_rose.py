# -*- coding: utf-8 -*-


def update_backstage_pass(item):
    item.sell_in = item.sell_in - 1
    if item.quality < 50:
        item.quality += 1
        if item.sell_in < 11:
            item.quality += 1
        if item.sell_in < 6:
            item.quality += 1
    else:
        item.quality += 0
    if item.sell_in < 0:
        item.quality = 0
    return Item(item.name, item.sell_in, item.quality)


def update_sulfuras(item):
    item.quality = 80
    updated_item = Item(item.name, item.sell_in, item.quality)
    return updated_item


def update_normal_item(item):
    item.sell_in = item.sell_in - 1
    if item.quality > 0:
        item.quality = item.quality - 1
    if item.sell_in < 0:
        if item.quality > 0:
            item.quality = item.quality - 1
    updated_item = Item(item.name, item.sell_in, item.quality)
    return updated_item


def quality_delta_aged_brie(item_sell_in):
    if item_sell_in < 0:
        delta = 2
    else:
        delta = 1
    return delta


def update_brie(item):
    item.sell_in = item.sell_in - 1
    if item.quality < 50:
        item.quality += quality_delta_aged_brie(item.sell_in)
    updated_item = Item(item.name, item.sell_in, item.quality)
    return updated_item


class GildedRose(object):

    item_update_map = {
        "Sulfuras, Hand of Ragnaros": update_sulfuras,
        "Aged Brie": update_brie,
        "Backstage passes to a TAFKAL80ETC concert": update_backstage_pass
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        self.items = [self.update_item_quality(item) for item in self.items]

    def update_item_quality(self, item):
        return GildedRose.item_update_map.get(item.name, update_normal_item)(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
