from decimal import Decimal
from crosslist.models import Condition
from crosslist.reader import read_listings
import pytest


def test_reads_one_listing_per_row(tmp_path):
    csv_file = tmp_path / "listing.csv"
    csv_file.write_text("sku,title,brand,size,price,condition,description\nCL001,Tee,NiKe,S,23,good,red with a shark on it\nCL002,Kmrii Sweater,Kmrii,L,25.32,new_with_tags,japenese kmrii sweater yellow and black")
    listings = read_listings(csv_file)
    assert len(listings) == 2
    assert listings[0].sku == 'CL001'
    assert listings[1].sku == 'CL002'


def test_price_becomes_decimal(tmp_path):
    csv_file = tmp_path / "listing.csv"
    csv_file.write_text("sku,title,brand,size,price,condition,description\n"
    "CL001,Tee,NiKe,S,23,good,red with a shark on it\n"
    )
    listings = read_listings(csv_file)
    assert listings[0].price == Decimal('23')


def test_description_is_optional(tmp_path):
    csv_file = tmp_path / "listing.csv"
    csv_file.write_text("sku,title,brand,size,price,condition\n"
    "CL001,Tee,NiKe,S,23,good\n"
    )
    listings = read_listings(csv_file)
    assert listings[0].description == ''

def test_condition_becomes_enum(tmp_path):
    csv_file = tmp_path / "listing.csv"
    csv_file.write_text("sku,title,brand,size,price,condition,description\n"
    "CL001,Tee,NiKe,S,23,good,red with blue dragon\n"
    )
    listings = read_listings(csv_file)
    assert listings[0].condition is Condition.GOOD

def test_bad_condition_reports_line_number(tmp_path):
    csv_file = tmp_path / "listing.csv"
    csv_file.write_text("sku,title,brand,size,price,condition,description\n"
        "CL001,Tee,NiKe,S,23,good,red with blue dragon\n"
        "CL002,Burberry Fur Zip Up,Burberry,S,53.21,mint,red with blue dragon\n"
        )
    with pytest.raises(ValueError, match="Line 3"):
        read_listings(csv_file)

def test_bad_price_reports(tmp_path):
    csv_file = tmp_path / "listings.csv"
    csv_file.write_text("sku,title,brand,size,price,condition,description\n"
        "CL001,Tee,NiKe,S,forty,good,red with blue dragon\n")
    with pytest.raises(ValueError, match="Line 2"):
        read_listings(csv_file)

def test_missing_column_names_it(tmp_path):
    csv_file = tmp_path / "listings.csv"
    csv_file.write_text("sku,title,brand,size,condition,description\n")
    with pytest.raises(ValueError, match="price"):
        read_listings(csv_file)
