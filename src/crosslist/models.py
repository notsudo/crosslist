"""The one shape every listing takes before it becomes a Vinted, Grailed or Depop post."""

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from pathlib import Path


class Condition(Enum):
    NEW_WITH_TAGS = "new_with_tags"
    NEW_WITHOUT_TAGS = "new_without_tags"
    VERY_GOOD = "very_good"
    GOOD = "good"
    FAIR = "fair"


@dataclass
class Listing:
    sku: str  # your own ID for the item; also the name of its photo folder
    title: str
    brand: str
    size: str
    price: Decimal  # Decimal, not float: 0.1 + 0.2 != 0.3 with floats
    condition: Condition
    description: str = ""
    photos: list[Path] = field(default_factory=list)
