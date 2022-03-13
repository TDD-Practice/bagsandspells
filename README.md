# bagsandspells

Durance collects materials and casts spells

Rules
Durance has 1 backpack and 4 extra bags
Each bag has a capacity of 4 items, the backpack has a capacity of 8 items
Each bag can have a category, the backpack doesn't have one
Items are sorted alphabetically after organizing the bags
Example
Let's say that Durance has 8 items in his backpack and 1 empty extra bag, which has a category for Metals:

backpack = ['Leather', 'Iron', 'Copper', 'Marigold', 'Wool', 'Gold', 'Silk', 'Copper']
bag_with_metals_category = []
bag_with_no_category = []
bag_with_weapons_category = []
bag_with_no_category = []
he finds 2 new items, which are stored in the next available bag, since the backpack is already full:

backpack = ['Leather', 'Iron', 'Copper', 'Marigold', 'Wool', 'Gold', 'Silk', 'Copper']
bag_with_metals_category = ['Copper', 'Cherry Blossom']
bag_with_no_category = []
bag_with_weapons_category = []
bag_with_no_category = []
he now casts the organizing spell:

backpack = ['Cherry Blossom', 'Iron', 'Leather', 'Marigold', 'Silk', 'Wool']
bag_with_metals_category = ['Copper', 'Copper', 'Copper', 'Gold']
bag_with_no_category = []
bag_with_weapons_category = []
bag_with_no_category = []
{
"clothes": ["Leather", "Linen", "Silk", "Wool"],
"herbs": ["Cherry Blossom", "Marigold", "Rose", "Seaweed"],
"metals": ["Copper", "Gold", "Iron", "Silver"],
"weapons": ["Axe", "Dagger", "Mace", "Sword"]
}
