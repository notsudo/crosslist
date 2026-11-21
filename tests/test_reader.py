from decimal import Decimal
from pathlib import Path

import pytest

from crosslist.models import Condition
from crosslist.reader import read_listings

HEADER = "sku,title,brand,size,price,condition,description\n"


def write_csv(tmp_path: Path, rows: str, header: str = HEADER) -> Path:
    path = tmp_path / "listings.csv"
    path.write_text(header + rows)
    return path


def test_reads_one_listing_per_row(tmp_path):
    csv_path = write_csv(
        tmp_path,
        "A1,Vintage tee,Nike,M,25,good,Faded black\n"
        "A2,Denim jacket,Levi's,L,60,very_good,\n",
    )
    listings = read_listings(csv_path, tmp_path / "photos")
    assert [l.sku for l in listings] == ["A1", "A2"]


def test_parses_fields(tmp_path):
    csv_path = write_csv(tmp_path, "A1,Vintage tee,Nike,M,25.50,good,Faded black\n")
    item = read_listings(csv_path, tmp_path / "photos")[0]
    assert item.title == "Vintage tee"
    assert item.brand == "Nike"
    assert item.size == "M"
    assert item.price == Decimal("25.50")
    assert item.condition is Condition.GOOD
    assert item.description == "Faded black"


def test_strips_whitespace(tmp_path):
    csv_path = write_csv(tmp_path, " A1 , Vintage tee ,Nike, M , 25 , good ,\n")
    item = read_listings(csv_path, tmp_path / "photos")[0]
    assert item.sku == "A1"
    assert item.title == "Vintage tee"
    assert item.price == Decimal("25")
    assert item.condition is Condition.GOOD


def test_condition_is_case_insensitive(tmp_path):
    csv_path = write_csv(tmp_path, "A1,Tee,Nike,M,25,Very_Good,\n")
    assert read_listings(csv_path, tmp_path / "photos")[0].condition is Condition.VERY_GOOD


def test_description_column_is_optional(tmp_path):
    csv_path = write_csv(
        tmp_path, "A1,Tee,Nike,M,25,good\n", header="sku,title,brand,size,price,condition\n"
    )
    assert read_listings(csv_path, tmp_path / "photos")[0].description == ""


def test_missing_required_column_names_it(tmp_path):
    csv_path = write_csv(
        tmp_path, "A1,Tee,Nike,M,good\n", header="sku,title,brand,size,condition\n"
    )
    with pytest.raises(ValueError, match="price"):
        read_listings(csv_path, tmp_path / "photos")


def test_bad_condition_reports_line_number(tmp_path):
    csv_path = write_csv(
        tmp_path,
        "A1,Tee,Nike,M,25,good,\n"
        "A2,Hoodie,Carhartt,L,40,mint,\n",
    )
    with pytest.raises(ValueError, match="line 3"):
        read_listings(csv_path, tmp_path / "photos")


def test_finds_photos_sorted_and_filtered(tmp_path):
    photos = tmp_path / "photos" / "A1"
    photos.mkdir(parents=True)
    for name in ["2.png", "1.JPG", "3.webp", "notes.txt", ".DS_Store"]:
        (photos / name).write_bytes(b"")
    csv_path = write_csv(tmp_path, "A1,Tee,Nike,M,25,good,\n")
    item = read_listings(csv_path, tmp_path / "photos")[0]
    assert [p.name for p in item.photos] == ["1.JPG", "2.png", "3.webp"]


def test_no_photo_folder_means_no_photos(tmp_path):
    csv_path = write_csv(tmp_path, "A1,Tee,Nike,M,25,good,\n")
    assert read_listings(csv_path, tmp_path / "photos")[0].photos == []
