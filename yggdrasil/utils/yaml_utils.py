"""YAML utilities.
This module provides functions for loading and dumping YAML files.
"""

import yaml


def import_yaml_content(file_path: str) -> dict:
    """Loads a YAML file and returns its content as a dictionary."""
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
