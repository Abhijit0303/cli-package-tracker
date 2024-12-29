# Package Tracker

A Python CLI tool to track installed packages and automatically generate a `requirements.txt` file.

## Features

- Automatically updates a `requirements.txt` file whenever a package is installed or uninstalled.
- Logs installation and uninstallation activities (optional).
- Stores configuration so you don't need to specify file paths repeatedly.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abhijit0303/package_tracker.git
   cd package_tracker
   ```
1. Install the package:

   ```bash
   pip install
   ```

## Usage

1.  **Initialize the tracker**:
    ```python
    package-tracker init --requirements-file requirements.txt
    ```
2.  **Install a package**:
    ```python
    package-tracker install <package_name>
    ```
3.  **Uninstall a package**:
    ```python
    package-tracker uninstall <package_name>
    ```
4.  **Check the `requirements.txt` file**:
    ```python
     cat requirements.txt
    ```

## Logging

To enable logging, specify a log file during initialization:

```python
 package-tracker init --requirements-file requirements.txt --log-file log.txt
```
