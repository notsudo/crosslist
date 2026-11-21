"""Turn a CSV of items plus a folder of photos into Listing objects.

YOUR EXERCISE: implement read_listings so every test in tests/test_reader.py passes.

Rules (the tests check each one):
1. The CSV has a header row. Required columns: sku, title, brand, size, price, condition.
   `description` is optional. A missing required column -> ValueError naming the column.
2. Strip whitespace around every value.
3. price becomes a Decimal ("45" -> Decimal("45")).
4. condition becomes a Condition. Accept the value case-insensitively ("Very_Good" works).
   An unknown condition -> ValueError that mentions the CSV line number
   (the header is line 1, so the first item is line 2).
5. Photos for an item live in photos_dir/<sku>/. Keep only .jpg, .jpeg, .png and .webp
   files (any letter case), sorted by file name. No folder -> empty list.

Hints: csv.DictReader, pathlib.Path.iterdir(), Path.suffix, Condition(value).
"""

from pathlib import Path

from crosslist.models import Listing

REQUIRED_COLUMNS = ("sku", "title", "brand", "size", "price", "condition")
PHOTO_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


def read_listings(csv_path: Path, photos_dir: Path) -> list[Listing]:
    raise NotImplementedError("Your turn: see the rules at the top of this file.")
