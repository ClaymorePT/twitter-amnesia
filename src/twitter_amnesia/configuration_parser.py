"""
    Twitter Amnesia Yaml Configuration File Parser
"""

import re
from argparse import ArgumentTypeError
from dataclasses import dataclass
from pathlib import Path

import yaml
from schema import And, Optional, Schema

__all__ = [
    "load_configurations"
]

@dataclass
class TwitterConfigurations:
    """
    Contains Twitter Required Configurations.
    """
    bearer_token: str
    username: str


@dataclass
class ServiceConfigurations:
    """
    Contains service configurations.
    """
    twitter_configurations: TwitterConfigurations
    protection_tag: str
    storage_location: Path | None
    days_to_expire: int


_PROTECTION_TAG_RE = re.compile(r'(\[[\w]+\])')

_CONFIGURATION_FILE_SCHEMA = Schema({
    "twitter": {
        "bearer_token": Schema(str, error="'bearer_token' format must be a valid string."),
        "username": Schema(str, error="'username' format must be a valid string."),
    },
    "protection_tag": Schema(And(str,  _PROTECTION_TAG_RE.match), error="'protection_tag' has the format [x] where x are alphanumeric characteres."),
    Optional("storage_location"): And(
        Schema(str, error="'storage_location' format must be a valid string."),
        Schema(lambda path: Path(path).exists(), error="'fax_information_cache' must reference an existing directory."),
        Schema(lambda path: Path(path).is_dir(), error="'fax_information_cache' must reference a directory."),
    ),
    "days_to_expire": Schema(And(int, lambda x: x > 0), error="'days_to_expire' format must be an integer bigger than 0."),
})


def _process_config_file(file_location: Path) -> dict:
    config: dict | None = None
    with open(str(file_location.absolute()), 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file.read())
    if config is None:
        raise ArgumentTypeError("Config file is empty.")

    # Validating configuration schema
    _CONFIGURATION_FILE_SCHEMA.validate(config)
    return config


def load_configurations(file_location: Path) -> ServiceConfigurations:
    """
    Loads a configuration from a given file.
    :param file_location: path to a YAML configuration file
    :return: configuration object.
    """
    service_configurations = _process_config_file(file_location)

    storage_location: Path | None = service_configurations.get("storage_location", None)
    if storage_location:
        storage_location = Path(storage_location).absolute()

    return ServiceConfigurations(
        twitter_configurations=TwitterConfigurations(
            bearer_token = service_configurations["twitter"][ "bearer_token"],
            username = service_configurations["twitter"]["username"],
        ),
        protection_tag=service_configurations["protection_tag"],
        storage_location=storage_location,
        days_to_expire=service_configurations["days_to_expire"],
    )
