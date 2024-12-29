import subprocess
import pkg_resources
# from pathlib import Path
import logging
from .config_manager import get_requirements_file


class PackageTracker:
    def __init__(self, log_file=None):
        self.requirements_file = get_requirements_file()
        self.log_file = log_file
        if self.log_file:
            self._setup_logging()

    def _setup_logging(self):
        """Set up logging to a file."""

        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def get_installed_packages(self):
        """Get a dictionary of installed packages and their versions."""

        return {pkg.key: pkg.version for pkg in pkg_resources.working_set}

    def update_requirements_file(self):
        """Update the requirements.txt file with the current installed packages."""

        if not self.requirements_file:
            raise ValueError("Requirements file path is not set. Run 'package-tracker init' first.")
        installed_packages = self.get_installed_packages()
        with open(self.requirements_file, 'w') as f:
            for pkg, version in installed_packages.items():
                f.write(f"{pkg}=={version}\n")

    def track_install(self, package_name):
        """Install a package and update the requirements.txt file."""

        try:
            subprocess.run(['pip', 'install', package_name], check=True)
            self.update_requirements_file()
            if self.log_file:
                logging.info(f"Installed package: {package_name}")
        except subprocess.CalledProcessError as e:
            if self.log_file:
                logging.error(f"Failed to install package: {package_name}. Error: {e}")
            raise

    def track_uninstall(self, package_name):
        """Uninstall a package and update the requirements.txt file."""

        try:
            subprocess.run(['pip', 'uninstall', '-y', package_name], check=True)
            self.update_requirements_file()
            if self.log_file:
                logging.info(f"Uninstalled package: {package_name}")
        except subprocess.CalledProcessError as e:
            if self.log_file:
                logging.error(f"Failed to uninstall package: {package_name}. Error: {e}")
            raise
