# convbase

![PyPI - Status](https://img.shields.io/pypi/status/convbase)
![PyPI - Version](https://img.shields.io/pypi/v/convbase)
![PyPI - License](https://img.shields.io/pypi/l/convbase)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/convbase)
[![Actions status](https://github.com/jkomalley/convbase/workflows/CI/badge.svg)](https://github.com/jkomalley/convbase/actions)

Base conversion command line utility.

## Installation

You can install `convbase` using `uv` or `pip`:

```bash
uv pip install convbase
# or
pip install convbase
```

## Usage

`convbase` provides four command-line tools for quick base conversions:

### `bin` - Convert to Binary

Converts a decimal, octal (prefix `0o`), or hexadecimal (prefix `0x`) value to binary.

```bash
$ bin 10
0b1010
$ bin 0xFF
0b11111111
```

### `oct` - Convert to Octal

Converts a value to octal.

```bash
$ oct 10
0o12
$ oct 0b1010
0o12
```

### `dec` - Convert to Decimal

Converts a value to decimal.

```bash
$ dec 0b1010
10
$ dec 0xFF
255
```

### `hex` - Convert to Hexadecimal

Converts a value to hexadecimal.

```bash
$ hex 10
0xa
$ hex 0b1111
0xf
```
