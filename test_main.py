import pytest

from main import Backpack, Bag1, Bag2, Bag3, Bag4, reset_all_bags

def fill_Backpack(item, count):
    reset_all_bags()
    for i in range(count):
        Backpack.add_item(item)

def test_item_is_added_to_Backpack():
    fill_Backpack("", 0)
    Backpack.add_item("copper")
    assert "copper" in Backpack.items

def item_is_removed_from_Backpack():
    fill_Backpack("", 0)
    Backpack.add_item("copper")
    Backpack.remove_item("copper")
    assert "copper" not in Backpack.items

def test_item_is_added_to_Bag1_if_Backpack_is_full():
    fill_Backpack("copper", 8)
    Backpack.add_item("wood")
    assert "wood" in Bag1.items

def test_item_is_added_to_Bag2_if_Bag1_is_full():
    fill_Backpack("copper", 12)
    Backpack.add_item("wood")
    assert "wood" in Bag2.items

def test_item_is_added_to_Bag3_if_Bag2_is_full():
    fill_Backpack("copper", 16)
    Backpack.add_item("wood")
    assert "wood" in Bag3.items

def test_item_is_added_to_Bag4_if_Bag3_is_full():
    fill_Backpack("copper", 20)
    Backpack.add_item("wood")
    assert "wood" in Bag4.items

def test_raises_error_when_item_is_added_and_Bag4_is_full():
    fill_Backpack("copper", 24)       
    with pytest.raises(Exception, match=r".*not possible.*"):
        Backpack.add_item("wood")