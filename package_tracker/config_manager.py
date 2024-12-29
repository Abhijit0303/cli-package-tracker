import configparser
from pathlib import Path

CONFIG_FILE = Path.home() / ".package_tracker_config.ini"

def get_config():
    """Read the configuration file."""

    config = configparser.ConfigParser()
    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE)
    return config

def save_config(config):
    """Save the configuration file."""

    with open(CONFIG_FILE, 'w') as f:
        config.write(f)

def get_requirements_file():
    """Get the path to the requirements file from the config."""

    config = get_config()
    return config.get('DEFAULT', 'requirements_file', fallback=None)

def set_requirements_file(file_path):
    """Set the path to the requirements file in the config."""

    config = get_config()
    if 'DEFAULT' not in config:
        config['DEFAULT'] = {}
    config['DEFAULT']['requirements_file'] = file_path
    save_config(config)
