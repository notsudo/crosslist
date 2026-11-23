import csv
from decimal import Decimal

from crosslist.models import Listing


def read_listings(csv_path):
    listings = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            listing = Listing(
                sku=row['sku'],
                title=row['title'],
                brand=row['brand'],
                size=row['size'],
                price=Decimal(row['price']),
                condition=row['condition'],
                description=row.get('description','')
            )
            listings.append(listing)
    return listings
