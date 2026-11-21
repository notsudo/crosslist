from crosslist.models import Listing
from decimal import Decimal

def test_listing_has_empty_defaults():
    item = Listing("001","Denim Jacket", "Levis", "Large",Decimal("100.21"),"good")
    assert item.description == ""
    assert item.photos == []

def test_price_add_up():
    first = Listing("002","Denim Jacket", "Levis", "Large",Decimal("0.10"),"good")
    second = Listing("003","Denim Jacket", "Nike", "Small",Decimal("0.20"),"good")
    total = first.price + second.price

    assert total == Decimal("0.30")
