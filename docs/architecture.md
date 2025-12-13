# System Architecture Overview

## Project Overview

The Unicode Invisible Cleaner is a Python project designed to detect and remove invisible Unicode text characters from strings. This tool is particularly useful for cleaning up text data that may contain hidden characters that can cause issues in processing, display, or storage.

## Core Use Cases

1. **Text Cleaning**: Users can input text containing invisible characters and receive a cleaned version without those characters.
2. **Detection**: Users can check if their text contains any invisible Unicode characters before deciding to clean it.
3. **Integration**: The library can be integrated into other applications or workflows that require text sanitization.

## System Architecture

The architecture of the Unicode Invisible Cleaner is modular, consisting of several components that work together to provide the desired functionality.

### Components

1. **CLI (Command-Line Interface)**:

   - Located in `src/unicode_invisible_cleaner/cli.py`
   - Allows users to interact with the application via command line, providing options for input text and cleaning preferences.

2. **API**:

   - Located in `src/unicode_invisible_cleaner/api.py`
   - Provides a programmatic interface for detecting and cleaning invisible characters, enabling integration with other software.

3. **Detector**:

   - Located in `src/unicode_invisible_cleaner/detector.py`
   - Implements the `InvisibleTextDetector` class, which contains the logic for identifying invisible Unicode characters using algorithms.

4. **Cleaner**:

   - Located in `src/unicode_invisible_cleaner/cleaner.py`
   - Implements the `InvisibleTextRemover` class, responsible for removing detected invisible characters based on user-defined rules.

5. **Normalizer**:

   - Located in `src/unicode_invisible_cleaner/normalizer.py`
   - Defines the `InputProcessor` class, which normalizes input text to ensure consistent encoding and removes unwanted characters.

6. **Algorithms**:

   - Located in `src/unicode_invisible_cleaner/algorithm/`
   - Contains algorithms for detection and removal, including:
     - `trie.py`: Implements a trie data structure for efficient character lookup.
     - `regex_map.py`: Contains regex patterns for identifying invisible characters.

7. **Utilities**:

   - Located in `src/unicode_invisible_cleaner/utils.py`
   - Provides utility functions that support various operations throughout the project.

8. **Types**:
   - Located in `src/unicode_invisible_cleaner/types.py`
   - Defines key data types such as `UnicodeCharDef`, `DetectedItem`, and `DetectionReport`.

## Performance Considerations

- **Efficiency**: The use of a trie data structure allows for fast lookups of invisible characters, improving the performance of the detection process.
- **Scalability**: The modular design enables easy updates and enhancements to individual components without affecting the overall system.
- **Memory Usage**: Careful management of data structures and algorithms ensures that memory usage remains efficient, even with large text inputs.
- **Testing**: Comprehensive unit and integration tests ensure that the system performs reliably under various conditions and inputs.

This architecture provides a robust foundation for the Unicode Invisible Cleaner, ensuring that it meets the needs of users while maintaining high performance and reliability.
