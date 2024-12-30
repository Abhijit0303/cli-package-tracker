# Package Tracker 🚀

A Python CLI tool to track installed packages and automatically generate a `requirements.txt` file.

---

## Features ✨

- **Automatic Tracking**: Automatically updates a `requirements.txt` file whenever a package is installed or uninstalled.
- **Logging**: Logs installation and uninstallation activities to a `log.txt` file (optional).
- **Easy to Use**: Simple and intuitive command-line interface.

---

## Installation 🛠️

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package manager)

### Steps

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Abhijit0303/cli-package-tracker.git
   cd package-tracker
   ```

1. **Install Dependencies**:
   Install the required dependencies using the provided `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

1. **Install the Package**:
   Install the `package-tracker` tool in editable mode:

   ```bash

   pip install -e .
   ```

---

## Usage 🚀

### Initialize the Tracker

Before using the tool, initialize it by specifying the path to the `requirements.txt` file and enabling logging (optional):

```bash
package-tracker init
```

### Install a Package

Install a package and automatically update the `requirements.txt` file:

```bash
package-tracker install <package_name>
```

### Uninstall a Package

Uninstall a package and automatically update the `requirements.txt` file:

```bash
package-tracker uninstall <package_name>
```

### Check the `requirements.txt` File

View the contents of the `requirements.txt` file:

```basH
cat requirements.txt
```

### Check the `log.txt` File (if logging is enabled)

View the installation and uninstallation logs:

```bash
cat log.txt
```

---

## Example Workflow 📝

1.  **Initialize the Tracker**:

    ```bash
    package-tracker init
    ```

2.  **Install a Package**:

    ```bash
    package-tracker install requests
    ```

3.  **Check the `requirements.txt` File**:

    ```bash
    cat requirements.txt
    ```

    Output:

        requests==2.31.0

4.  **Uninstall a Package**:

    ```bash
    package-tracker uninstall requests
    ```

5.  **Check the `requirements.txt` File Again**:

    ```bash
    cat requirements.txt
    ```

    Output:

        # Empty or only contains other installed packages

---

## Logging 📜

To enable logging, specify a log file during initialization:

```bash
package-tracker init --log-file log.txt
```

Logs will be stored in the specified file and will include details about package installations and uninstallations.

---

## Contributing 🤝

Contributions are welcome! If you’d like to contribute, please follow these steps:

1.  Fork the repository.

2.  Create a new branch (`git checkout -b feature/YourFeatureName`).

3.  Commit your changes (`git commit -m 'Add some feature'`).

4.  Push to the branch (`git push origin feature/YourFeatureName`).

5.  Open a pull request.

---

## License 📄

This project is licensed under the Apache License Version 2.0. See the [LICENSE](https://github.com/Abhijit0303/cli-package-tracker/blob/d2af9c71a168222542780ca6480250d2701ec4e3/LICENSE) file for details.

---

## Author 👨‍💻

- **Abhijit**

  - X: [AbhijitCodex](https://x.com/AbhijitCodex)

  - GitHub: [Abhijit0303](https://github.com/Abhijit0303)

---

## Acknowledgments 🙏

- Thanks to the Python community for creating amazing tools like `pip` and `click`.

---

Enjoy tracking your Python packages with **Package Tracker**! 🎉
