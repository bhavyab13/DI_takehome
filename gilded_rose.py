# Add your solution here!
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

class _InventoryStrategies:
    @staticmethod
    def update_normal(item):
        item.sell_in -= 1
        degrade = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - degrade)

    @staticmethod
    def update_aged_brie(item):
        item.sell_in -= 1
        increase = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + increase)

    @staticmethod
    # Sulfuras is a Legendary item, so no update needed
    def update_sulfuras(item):
        pass  

    @staticmethod
    def update_backstage(item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

    @staticmethod
    #Conjured items degrade twice as fast
    def update_conjured(item):
        item.sell_in -= 1
        degrade = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - degrade)


class GildedRose:
    #Mapping of item names to their update strategies
    __inventoryItem = {
        "Aged Brie": _InventoryStrategies.update_aged_brie,
        "Sulfuras, Hand of Ragnaros": _InventoryStrategies.update_sulfuras,
        "Backstage passes to a TAFKAL80ETC concert": _InventoryStrategies.update_backstage,
    }

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            strategy = self.__get_strategy(item)
            strategy(item)
        return self.items

    @staticmethod
    def __get_strategy(item):
        if "Conjured" in item.name:
            return _InventoryStrategies.update_conjured
        return GildedRose.__inventoryItem.get(item.name, _InventoryStrategies.update_normal)
