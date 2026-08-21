# clide

Clide (pronounced "Clyde", like the river) is custom CLI tool for managing my personal computer.

## Prerequisites

Python

## Installation

Clone the repo and install in editable mode using pipx, so clide is available system-wide without needing to activate a virtual environment:

```
git clone https://github.com/<your-username>/clide.git
cd clide
pipx install -e .
```

Verify the installation was successful:

```
clide --version
# or
clide -v
```

## Usage

```
clide [COMMAND] [OPTIONS]
```

### Global options

| Flag | Description |
| ---- | ----------- |
| `--version`, `-v` | Print the installed version of `clide`. |
| `--help` | Show help for `clide` or any subcommand. |

## Development

Create and activate a virtual environment (`venv`):

```
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Testing

Run all tests:

```
pytest
```

Run a specific test file or test:

```
pytest tests/test_cli.py
pytest tests/test_cli.py::test_version_long_flag
```
