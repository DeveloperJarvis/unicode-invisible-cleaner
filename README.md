# Unicode Invisible Cleaner

## Overview

The Unicode Invisible Cleaner is a Python project designed to detect and remove invisible Unicode text characters from strings. This tool is particularly useful for cleaning up text data that may contain hidden characters that can cause issues in processing, display, or storage.

## Features

- Detects invisible Unicode characters in text.
- Provides options to remove or replace detected characters.
- Command-line interface for easy usage.
- Programmatic API for integration into other applications.

## Installation

To install the Unicode Invisible Cleaner, clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/unicode-invisible-cleaner.git
cd unicode-invisible-cleaner
pip install -r requirements.txt
```

## Usage

### Command-Line Interface

You can use the command-line interface to clean text files or strings directly from the terminal. For example:

```bash
python -m unicode_invisible_cleaner.cli --input "Your text here" --remove
```

### Programmatic API

You can also use the API in your Python scripts:

```python
from unicode_invisible_cleaner.api import detect, clean

text = "Your text with invisible characters"
detected = detect(text)
cleaned = clean(text)
```

## System Architecture

The project is structured into several modules, each responsible for different aspects of the functionality:

- **detector.py**: Contains the `InvisibleTextDetector` class for detecting invisible characters.
- **cleaner.py**: Contains the `InvisibleTextRemover` class for removing detected characters.
- **normalizer.py**: Contains the `InputProcessor` class for normalizing input text.
- **algorithm**: Contains algorithms for efficient detection and removal, including a trie and regex patterns.
- **utils.py**: Provides utility functions to support various operations.
- **types.py**: Defines key data types used throughout the project.

## Testing

The project includes unit tests for the detector and cleaner functionalities, as well as integration tests to ensure the components work together seamlessly. To run the tests, use:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Creating tag

```bash
# 1. Check existing tags
git tag
# 2. Create a valid tag
git tag -a v1.0.0 -m "Release version 1.0.0"
# or lightweight tag
git tag v1.0.0
# push tag to remote
git push origin v1.0.0
```
