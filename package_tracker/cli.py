import click
from .tracker import PackageTracker
from .config_manager import get_requirements_file, set_requirements_file
import os

# Basic details
APP_NAME = "Package Tracker"
AUTHOR = "Abhijit"
X = "x.com/Abhijitcodex"
VERSION = "0.2"

def show_basic_details():
    """Display basic details about the app."""
    click.echo(f"Welcome to {APP_NAME}!")
    click.echo(f"Author: {AUTHOR}")
    click.echo(f"X: {X}")
    click.echo(f"Version: {VERSION}")
    click.echo("--------------------------")

@click.group()
def cli():
    """A CLI tool to track installed Python packages and generate a requirements.txt file."""
    show_basic_details()

@cli.command()
@click.option('--requirements-file', prompt='Enter the name of the requirements file', default='requirements.txt', help='Name of the file to store package information.')
@click.option('--enable-logging', prompt='Enable logging?', default=True, help='Enable logging (yes/no).')
@click.option('--log-file', prompt='Enter the name of the log file', default='log.txt', help='Name of the log file.')
def init(requirements_file, enable_logging, log_file):
    """Initialize the package tracker with a file path."""
    if not enable_logging:
        log_file = None
    elif not os.path.exists(log_file):
        confirm = click.confirm(f"Create log file at {log_file}?")
        if not confirm:
            log_file = None
    set_requirements_file(requirements_file)
    tracker = PackageTracker(log_file)
    tracker.update_requirements_file()
    click.echo(f"Package tracker initialized. Tracking packages in {requirements_file}.")
    if log_file:
        click.echo(f"Logging enabled. Logs will be stored in {log_file}.")

@cli.command()
@click.argument('package_name')
def install(package_name):
    """Install a package and update the requirements file."""
    requirements_file = get_requirements_file()
    log_file = None  # Default to no logging
    if os.path.exists("log.txt"):  # Check if logging is enabled
        log_file = "log.txt"
    tracker = PackageTracker(log_file)
    try:
        tracker.track_install(package_name)
        click.echo(f"Package {package_name} installed and tracked.")
    except Exception as e:
        click.echo(f"Error: {e}")

@cli.command()
@click.argument('package_name')
def uninstall(package_name):
    """Uninstall a package and update the requirements file."""
    requirements_file = get_requirements_file()
    log_file = None  # Default to no logging
    if os.path.exists("log.txt"):  # Check if logging is enabled
        log_file = "log.txt"
    tracker = PackageTracker(log_file)
    try:
        tracker.track_uninstall(package_name)
        click.echo(f"Package {package_name} uninstalled and removed from tracking.")
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    cli()
