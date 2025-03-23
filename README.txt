Approach to solving:

1. I decided to refactor the code by updating the update logic from the large if-else statements in the update_quality() method,
to improve modularity. 

2. Now, each kind of inventory item's logic is encapsulated in its own update function

3. These methods are organized within the _InventoryStrategies class which consists of @staticmethods because they do not require
access to class or instance state.

4. The "Conjured" items are not included in the dictionary by name because they come in many variations as seen in the test cases.
So, instead the code just cheecks if it's in the item name and this also helps with modularity in case you want to add more items 


Alternative Approach:
I do realize there is another approach that I could have taken: using a class hierarchy to represent different types of items.
However, I chose the approach above because it is a more straightforward solution, keeping parts of the legacy code and the original structure.
In case there are new items/strategies to add, it would also be easier to add them to the dictionary and add a function to the _InventoryStrategies
class.

For the alternate approach, I would have needed to implement an object-oriented design using inheritance, where each item type would have a subclass.
This would be a good refactoring method if the problem scope were larger, but since there is a simple strategy in this case, I chose the approach above.


output:
$ python run_update.py

-------- day 0 --------
name, sellIn, quality
+5 Dexterity Vest, 10, 20
Aged Brie, 2, 0
Elixir of the Mongoose, 5, 7
Sulfuras, Hand of Ragnaros, 0, 80
Sulfuras, Hand of Ragnaros, -1, 80
Backstage passes to a TAFKAL80ETC concert, 15, 20
Backstage passes to a TAFKAL80ETC concert, 10, 49
Backstage passes to a TAFKAL80ETC concert, 5, 49
Conjured Mana Cake, 3, 6

-------- day 1 --------
name, sellIn, quality
+5 Dexterity Vest, 9, 19
Aged Brie, 1, 1
Elixir of the Mongoose, 4, 6
Sulfuras, Hand of Ragnaros, 0, 80
Sulfuras, Hand of Ragnaros, -1, 80
Backstage passes to a TAFKAL80ETC concert, 14, 21
Backstage passes to a TAFKAL80ETC concert, 9, 50
Backstage passes to a TAFKAL80ETC concert, 4, 50
Conjured Mana Cake, 2, 4

$ python test.py      
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK