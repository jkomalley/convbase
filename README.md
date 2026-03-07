# convbase

![PyPI - Status](https://img.shields.io/pypi/status/convbase)
![PyPI - Version](https://img.shields.io/pypi/v/convbase)
![PyPI - License](https://img.shields.io/pypi/l/convbase)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/convbase)
[![CI](https://github.com/jkomalley/convbase/workflows/CI/badge.svg)](https://github.com/jkomalley/convbase/actions)

A command-line utility for converting integers between binary, octal, decimal, and hexadecimal bases.

## Installation

```bash
pip install convbase
```

Or with `uv`:

```bash
uv tool install convbase
```

## Commands

| Command | Output base |
|---------|-------------|
| `bin`   | Binary (`0b`) |
| `oct`   | Octal (`0o`) |
| `dec`   | Decimal |
| `hex`   | Hexadecimal (`0x`) |

## Input formats

All commands accept `VALUE` in any of the following formats:

| Format | Prefix | Example |
|--------|--------|---------|
| Decimal | _(none)_ | `10` |
| Binary | `0b` | `0b1010` |
| Octal | `0o` | `0o12` |
| Hexadecimal | `0x` | `0xA` |

## Examples

```bash
$ bin 10
0b1010
$ bin 0xFF
0b11111111

$ oct 0b1010
0o12
$ oct 0xA
0o12

$ dec 0b1010
10
$ dec 0xFF
255

$ hex 10
0xa
$ hex 0b11111111
0xff
```

## Error handling

Passing a value that cannot be parsed as an integer exits with a non-zero status and prints an error:

```bash
$ bin hello
Error: Invalid value for 'VALUE': invalid integer: 'hello'
```

## Development

```bash
git clone https://github.com/jkomalley/convbase
cd convbase
just setup
just all       # lint, type-check, and test
```

## License

MIT
