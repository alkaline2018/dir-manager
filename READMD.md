# Directory Manager

This project provides utility functions to manage directories in a dynamic and flexible way. The main functionality includes generating a base path based on the current year and month, optionally appending a directory name, and creating folders if they don't exist.

## Features

- **Dynamic Directory Creation**: Automatically generates a directory structure based on the current year and month.
- **Optional Directory Name**: Allows for optional inclusion of a subdirectory name.
- **Robust Folder Management**: Folders are created if they don't exist, with detailed logging.

## File Structure
├─dir_manager─ dir_manager.py # Main utility file for managing directories 
├─tests─ test_dir_manager.py # Unit tests for the directory manager 
└── README.md 

# Documentation of the project

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/directory-manager.git
   ```
2. Navigate to the project directory:
   ```bash
   cd directory-manager
   ```
3. Install the required dependencies:
   This project does not have external dependencies, but ensure you have Python installed.

# Usage
## Setting up the BASE_DIR Environment Variable
The project looks for the BASE_DIR environment variable to determine the root directory. If the variable is not set, it defaults to D:/send.

You can set the BASE_DIR environment variable like this:

On macOS/Linux:
   ```bash
   export BASE_DIR="/path/to/your/base"
   ```
On Windows:
   ```bash
   set BASE_DIR="D:/path/to/your/base"
   ```

## Using the Directory Manager
You can use the get_base_path() function to dynamically create a directory path based on the current year and month. For example:
   ```python
    from dir_manager import get_base_path    
    # Generate a base path
    base_path = get_base_path("my_directory")
    print(base_path)  # Output: /path/to/your/base/2024/09/my_directory
   ```

## Running Unit Tests
Unit tests for the dir_manager can be found in test_dir_manager.py. To run the tests:

Ensure you have the unittest module available (it's part of the Python standard library).
Run the tests using the following command:

   ```python
    python -m unittest test_dir_manager.py
   ```

Logging
The directory manager uses Python's built-in logging module for informative messages about folder creation and errors. By default, logging is set to the INFO level.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Feel free to submit issues or pull requests for improvements or additional features. Contributions are welcome!

yaml
코드 복사

---

### Summary

1. **`dir_manager.py`**: Contains the core functionality for creating directories and managing paths.
2. **`test_dir_manager.py`**: Unit tests to ensure the directory manager functions correctly.
3. **`README.md`**: Documentation that explains the project, its usage, and instructions for setting up, running, and testing the code.

This setup should work well for a GitHub project!