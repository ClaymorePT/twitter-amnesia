"""
Define the command line arguments and the parser for it.

"""
from argparse import ArgumentParser, ArgumentTypeError,  Namespace
from pathlib import Path


__all__ = [
    "parse_arguments"
]


def _validate_config_file_location(file_location):
    if isinstance(file_location, str):
        file_location = Path(file_location)
        if file_location.exists():
            if file_location.is_file():
                return file_location
            else:
                raise ArgumentTypeError(
                    "Location must point to a file"
                )
        else:
            raise ArgumentTypeError(
                "File must exist."
            )

    raise ArgumentTypeError(
        f"Invalid configuration file location [{file_location}]. Must be a valid file location."
    )

def parse_arguments() -> Namespace:
    """
    Return the parsed arguments
    """

    parser = ArgumentParser(
        prog="twitter_amnesia",
        description=" Twitter Amnesia Service"
    )

    parser.add_argument(
        "-c",
        "--configuration_file",
        help="YAML Configuration file to be used.",
        type=_validate_config_file_location,
        required=True,
    )

    parser.add_argument(
        "-l", "--logLevel",
        help="Logging Level (default: %(default)s)",
        type=str,
        choices=["INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO"
    )

    return parser.parse_args()
