import pytest

from main import Backpack, Bag1, Bag2, Bag3, Bag4

def item_is_added_to_backpack():
    Backpack.add_item("copper")
    assert len(Backpack.items) == 1
    assert "copper" in Backpack.items

def test_item_is_added_to_Bag1_if_Backpack_is_full():
    for i in range(8):
        Backpack.add_item("copper")
    Bag1.add_item("wood")
    assert "wood" not in Bag1.items
    assert len(Backpack.items) == 8

