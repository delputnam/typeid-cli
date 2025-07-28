# TypeID CLI

A command-line tool for generating TypeIDs and converting between TypeID and UUID formats.

## Installation

### From GitHub (Recommended)
```bash
pipx install git+https://github.com/delputnam/typeid-cli.git
```

### From Source
```bash
git clone https://github.com/delputnam/typeid-cli.git
cd typeid-cli
pipx install .
```

### Alternative (pip)
```bash
pip install --user git+https://github.com/delputnam/typeid-cli.git
```

## Usage

The CLI provides five commands:

### Generate a new TypeID
```bash
typeid generate user
```
Output:
```
typeid: user_01k18q5gpffnjv13z28k6z7t7c
uuid: 01985172-c2cf-7d65-b08f-e244cdf3e8ec
```

### Convert TypeID to UUID
```bash
typeid typeid-to-uuid contact_01k0g0hzrsed3scjp07tsz36y8
```

### Convert UUID to TypeID
```bash
typeid uuid-to-typeid 01234567-89ab-cdef-0123-456789abcdef contact
```

### Convert Hex to TypeID
```bash
typeid hex-to-typeid 0x01977609240070008000000000000000 contact
typeid hex-to-typeid 01977609240070008000000000000000 contact
```

### Convert Hex to UUID
```bash
typeid hex-to-uuid 0x01977609240070008000000000000000
typeid hex-to-uuid 01977609240070008000000000000000
```

## Development

Install development dependencies:
```bash
pip install -e .[dev]
```

Run tests:
```bash
pytest
```

Run linting:
```bash
ruff check
```

Run type checking:
```bash
pyright
```