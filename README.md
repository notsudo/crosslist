# crosslist

Write your clothing listings once in a CSV, then turn them into posts for Vinted, Grailed, Depop and more.

> Work in progress. Right now it reads a CSV plus photo folders into listings. Posting to each site comes next.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Input format

`listings.csv` (see `examples/listings.csv`):

| column      | required | example                 |
|-------------|----------|-------------------------|
| sku         | yes      | CL001                   |
| title       | yes      | Vintage 90s Nike Windbreaker |
| brand       | yes      | Nike                    |
| size        | yes      | L                       |
| price       | yes      | 45                      |
| condition   | yes      | new_with_tags, new_without_tags, very_good, good, fair |
| description | no       | No stains, small pull on cuff |

Photos go in `photos/<sku>/` (for example `photos/CL001/1.jpg`). They're used in file-name order.
