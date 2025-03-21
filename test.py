# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose

def item_to_str(item):
   return item.name + ", " + str(item.sell_in) + ", " + str(item.quality)

def assert_updates(*item_pairs):
   n = len(item_pairs)
   items_updated = [Item(original.name, original.sell_in, original.quality) for (original, EXPECTED) in item_pairs]
   items_updated = GildedRose(items_updated).update_quality()
   # TODO: Add check that items_updated is still an array
   try:
      updated_len = len(items_updated)
   except TypeError:
      raise Exception("update_quality did not return an array!")
   if updated_len != n:
      raise Exception(" ".join([
         "Updated list changed length.",
         "Expected: " + str(n) + ".",
         "Actual: " + str(len(items_updated))
      ]))

   errs = []
   for i in range(n):
      [original, EXPECTED] = item_pairs[i]
      updated = items_updated[i]
      if EXPECTED.name == updated.name:
         if EXPECTED.sell_in == updated.sell_in:
            if EXPECTED.quality == updated.quality:
               continue # don't error

      errs.append("\n".join([
         "Conflict for item " + str(i) + ": name, sell_in, quality",
         "Original item: " + item_to_str(original),
         "Updated  item: " + item_to_str(updated),
         "Expected item: " + item_to_str(EXPECTED),
      ]))
   if len(errs) > 0:
      raise Exception("\n" + "\n\n".join(errs))

class test_gilded_rose(unittest.TestCase):
    def test_normal_item(self):
        assert_updates(
            [Item("baz",  2,  4), Item("baz",  1,  3)],
            [Item("baz",  1,  1), Item("baz",  0,  0)],
            [Item("baz",  0,  4), Item("baz", -1,  2)],
            [Item("baz", -1,  4), Item("baz", -2,  2)],

            [Item("baz",  1,  0), Item("baz",  0,  0)],
            [Item("baz",  0,  1), Item("baz", -1,  0)],
            [Item("baz",  0,  0), Item("baz", -1,  0)],
            [Item("baz", -1,  1), Item("baz", -2,  0)],
            [Item("baz", -1,  0), Item("baz", -2,  0)],
        )

    def test_aged_brie(self):
        assert_updates(
            [Item("Aged Brie",  2,  4), Item("Aged Brie",  1,  5)],
            [Item("Aged Brie",  1,  4), Item("Aged Brie",  0,  5)],
            [Item("Aged Brie",  1, 49), Item("Aged Brie",  0, 50)],
            [Item("Aged Brie",  0,  4), Item("Aged Brie", -1,  6)],
            [Item("Aged Brie", -1,  4), Item("Aged Brie", -2,  6)],

            [Item("Aged Brie",  1, 50), Item("Aged Brie",  0, 50)],
            [Item("Aged Brie",  0, 49), Item("Aged Brie", -1, 50)],
            [Item("Aged Brie",  0, 50), Item("Aged Brie", -1, 50)],
            [Item("Aged Brie", -1, 49), Item("Aged Brie", -2, 50)],
            [Item("Aged Brie", -1, 50), Item("Aged Brie", -2, 50)],
        )

    def test_sulfuras(self):
        assert_updates(
            [Item("Sulfuras, Hand of Ragnaros",  0, 80), Item("Sulfuras, Hand of Ragnaros",  0, 80)],
            [Item("Sulfuras, Hand of Ragnaros", -1, 80), Item("Sulfuras, Hand of Ragnaros", -1, 80)],
        )

    def test_backstage_pass(self):
        assert_updates(
            [Item("Backstage passes to a TAFKAL80ETC concert", 13, 19), Item("Backstage passes to a TAFKAL80ETC concert", 12, 20)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 12, 19), Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 11, 19), Item("Backstage passes to a TAFKAL80ETC concert", 10, 20)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 10, 19), Item("Backstage passes to a TAFKAL80ETC concert",  9, 21)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  9, 19), Item("Backstage passes to a TAFKAL80ETC concert",  8, 21)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  8, 19), Item("Backstage passes to a TAFKAL80ETC concert",  7, 21)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  7, 19), Item("Backstage passes to a TAFKAL80ETC concert",  6, 21)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  6, 19), Item("Backstage passes to a TAFKAL80ETC concert",  5, 21)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  5, 19), Item("Backstage passes to a TAFKAL80ETC concert",  4, 22)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  4, 19), Item("Backstage passes to a TAFKAL80ETC concert",  3, 22)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  3, 19), Item("Backstage passes to a TAFKAL80ETC concert",  2, 22)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  2, 19), Item("Backstage passes to a TAFKAL80ETC concert",  1, 22)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  1, 19), Item("Backstage passes to a TAFKAL80ETC concert",  0, 22)],

            [Item("Backstage passes to a TAFKAL80ETC concert",  0, 19), Item("Backstage passes to a TAFKAL80ETC concert", -1,  0)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  0, 50), Item("Backstage passes to a TAFKAL80ETC concert", -1,  0)],
            [Item("Backstage passes to a TAFKAL80ETC concert", -1,  0), Item("Backstage passes to a TAFKAL80ETC concert", -2,  0)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 13, 49), Item("Backstage passes to a TAFKAL80ETC concert", 12, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 13, 50), Item("Backstage passes to a TAFKAL80ETC concert", 12, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 10, 48), Item("Backstage passes to a TAFKAL80ETC concert",  9, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49), Item("Backstage passes to a TAFKAL80ETC concert",  9, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert", 10, 50), Item("Backstage passes to a TAFKAL80ETC concert",  9, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  5, 47), Item("Backstage passes to a TAFKAL80ETC concert",  4, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  5, 48), Item("Backstage passes to a TAFKAL80ETC concert",  4, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  5, 49), Item("Backstage passes to a TAFKAL80ETC concert",  4, 50)],
            [Item("Backstage passes to a TAFKAL80ETC concert",  5, 50), Item("Backstage passes to a TAFKAL80ETC concert",  4, 50)],
        )

    def test_conjured(self):
        assert_updates(
            [Item("Conjured foo",  4, 19), Item("Conjured foo",  3, 17)],
            [Item("Conjured foo",  1, 19), Item("Conjured foo",  0, 17)],
            [Item("Conjured foo",  0, 19), Item("Conjured foo", -1, 15)],
            [Item("Conjured foo", -1, 19), Item("Conjured foo", -2, 15)],

            [Item("Conjured bar",  4, 19), Item("Conjured bar",  3, 17)],
            [Item("Conjured bar",  1, 19), Item("Conjured bar",  0, 17)],
            [Item("Conjured bar",  0, 19), Item("Conjured bar", -1, 15)],
            [Item("Conjured bar", -1, 19), Item("Conjured bar", -2, 15)],

            [Item("Conjured foo",  2,  2), Item("Conjured foo",  1,  0)],
            [Item("Conjured foo",  2,  1), Item("Conjured foo",  1,  0)],
            [Item("Conjured foo",  2,  0), Item("Conjured foo",  1,  0)],
            [Item("Conjured foo",  1,  2), Item("Conjured foo",  0,  0)],
            [Item("Conjured foo",  1,  1), Item("Conjured foo",  0,  0)],
            [Item("Conjured foo",  1,  0), Item("Conjured foo",  0,  0)],
            [Item("Conjured foo",  0,  4), Item("Conjured foo", -1,  0)],
            [Item("Conjured foo",  0,  3), Item("Conjured foo", -1,  0)],
            [Item("Conjured foo",  0,  2), Item("Conjured foo", -1,  0)],
            [Item("Conjured foo",  0,  1), Item("Conjured foo", -1,  0)],
            [Item("Conjured foo",  0,  0), Item("Conjured foo", -1,  0)],
            [Item("Conjured foo", -1,  4), Item("Conjured foo", -2,  0)],
            [Item("Conjured foo", -1,  3), Item("Conjured foo", -2,  0)],
            [Item("Conjured foo", -1,  2), Item("Conjured foo", -2,  0)],
            [Item("Conjured foo", -1,  1), Item("Conjured foo", -2,  0)],
            [Item("Conjured foo", -1,  0), Item("Conjured foo", -2,  0)],
        )

if __name__ == '__main__':
   unittest.main()
