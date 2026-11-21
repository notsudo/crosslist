from dataclasses import dataclass, field
from pathlib import Path
from decimal import Decimal


@dataclass
class Listing:
    sku: str
    title: str
    brand: str
    size: str
    price: Decimal
    condition: str
    description: str = ""
    photos: list[Path] = field(default_factory=list)
