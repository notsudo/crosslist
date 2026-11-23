import csv
from decimal import Decimal, InvalidOperation

from crosslist.models import Listing, Condition


def read_listings(csv_path):
    listings = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for line_number,row in enumerate(reader, start=2):
            try:
                condition = Condition(row['condition'])
            except ValueError:
                raise ValueError(f"Line {line_number}: unknown condition '{row['condition']}'")
            try:
                price = Decimal(row['price'])
            except InvalidOperation:
                raise ValueError(f"Line {line_number}: invalid price '{row['price']}'")
            listing = Listing(
                sku=row['sku'],
                title=row['title'],
                brand=row['brand'],
                size=row['size'],
                price=price,
                condition=condition,
                description=row.get('description','')
            )
            listings.append(listing)
    return listings
