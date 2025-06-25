# ThoughtfulAI
Thoughtful AI Assignment

# Package Sorter

This project provides a Python module and command-line tool to sort packages into categories based on their dimensions and mass.

## Rules

- A package is **bulky** if its volume (Width × Height × Length) is **≥ 1,000,000 cm³** or if **any dimension is ≥ 150 cm**.
- A package is **heavy** if its mass is **≥ 20 kg**.

### Categories

- **STANDARD**: Not bulky and not heavy.
- **SPECIAL**: Bulky or heavy (but not both).
- **REJECTED**: Both bulky and heavy.


## Usage

### 1. As a Command-Line Tool

From the project root, run:

```bash
python src/sort_packages.py <width> <height> <length> <mass>
```

For Example
```bash
python src/sort_packages.py 100 100 100 5
```

### 2. As a Python Module

You can import and use the `sort` function in your own Python code:

```python
from src.sort_packages import sort

result = sort(100, 100, 100, 5)
print(result)  # Output: SPECIAL
```


## Running Tests

Install `pytest` if you haven't already:

```bash
pip install pytest
```

Then run the tests:

```bash
PYTHONPATH=src pytest
```

## Input Validation

- All dimensions and mass must be **positive numbers**.
- Non-numeric or non-positive values will raise an error.

## File Structure

```
src/
  sort_packages.py   # Main logic and CLI
tests/
  sort_package_test.py  # Unit tests
```

