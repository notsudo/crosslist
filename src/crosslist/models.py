from dataclasses import dataclass, field
from pathlib import Path
from decimal import Decimal
from enum import Enum


class Condition(Enum):
    NEW_WITH_TAGS = 'new_with_tags'
    NEW_WITHOUT_TAGS = 'new_without_tags'
    VERY_GOOD = 'very_good'
    GOOD = 'good'
    FAIR = 'fair'


@dataclass
class Listing:
    sku: str
    title: str
    brand: str
    size: str
    price: Decimal
    condition: Condition
    description: str = ""
    photos: list[Path] = field(default_factory=list)
