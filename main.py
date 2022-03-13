    
class Backpack:
    items = []

    def add_item(item):
        if(len(Backpack.items) < 8):
            Backpack.items.append(item)
        elif(len(Bag1.items) < 4):
            Bag1.items.append(item)
        elif(len(Bag2.items) < 4):
            Bag2.items.append(item)
        elif(len(Bag3.items) < 4):
            Bag3.items.append(item)
        elif(len(Bag4.items) < 4):
            Bag4.items.append(item)
        else: raise Exception("All bags are full, adding another item is not possible.")

class Bag1:
    category = ""
    items = []
class Bag2:
    category = ""
    items = []
class Bag3:
    category = ""
    items = []
class Bag4:
    category = ""
    items = []

def reset_all_bags():
    Backpack.items = []
    Bag1.items = []
    Bag2.items = []
    Bag3.items = []
    Bag4.items = []