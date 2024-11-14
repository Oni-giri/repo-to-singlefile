# Repo to Text

A command-line tool that converts code repositories into text format, making them suitable for use as context in Large Language Models (LLMs). Supports both local repositories and GitHub remote repositories.

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install repo-to-text
```

### Option 2: Install from source

1. Clone the repository:
```bash
git clone https://github.com/yourusername/repo-to-text.git
cd repo-to-text
```

2. Install using pip in editable mode:
```bash
pip install -e .
```

## Usage

After installation, you can use the tool directly from the command line:

### Basic Usage

1. Convert a local repository:
```bash
repo-to-text /path/to/local/repo output.txt
```

2. Convert a public GitHub repository:
```bash
repo-to-text https://github.com/owner/repo output.txt
```

3. Convert a private GitHub repository:
```bash
repo-to-text https://github.com/owner/repo output.txt --github-token YOUR_GITHUB_TOKEN
```

### Output Format

The generated text file will contain the contents of all text files in the repository, with clear headers separating each file:

```
### File: src/main.py ###
[content of main.py]

### File: src/utils.py ###
[content of utils.py]

...
```

## Development

### Setup Development Environment

1. Install Poetry:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

### Running Tests

```bash
poetry run pytest
```

### Building the Package

```bash
poetry build
```

### Local Installation for Testing

```bash
pip install dist/*.whl
```

[Rest of the README remains the same...]