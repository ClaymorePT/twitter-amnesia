
import argparse
import re

consumer_key_re = re.compile('([a-zA-Z1-9]+)')
consumer_secret_re = re.compile('([a-zA-Z1-9]+)')
access_token_key_re = re.compile('([0-9]+-[a-zA-Z1-9]+)')
access_token_secret_re = re.compile('([a-zA-Z1-9]+)')


def validate_days(days):
    if isinstance(days, int) and days > 0:
        return days
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid day value. Must be int and bigger than 0 (current value {days})"
        )

def validate_consumer_key(token):
    if consumer_key_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer key token -> {token})"
        )

def validate_consumer_secret(token):
    if consumer_secret_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer secret token -> {token})"
        )

def validate_access_token_key(token):
    if access_token_key_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer secret token -> {token})"
        )

def validate_access_token_secret(token):
    if access_token_secret_re.match(token):
        return token
    else:
        raise argparse.ArgumentTypeError(
            f"Invalid consumer secret token -> {token})"
        )


def parse_arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--logLevel",
        help="Logging Level (default: %(default)s)",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO"
    )

    parser.add_argument(
        "-d", "--days",
        help="Tweets older than %(default)d days (default value)",
        type=validate_days,
        default=7
    )

    parser.add_argument(
        "-ck", "--consumer_key",
        help="Consumer Key",
        required=True,
        type=validate_consumer_key
    )


    parser.add_argument(
        "-cs", "--consumer_secret",
        help="Consumer Secret",
        required=True,
        type=validate_consumer_secret
    )

    parser.add_argument(
        "-tk", "--token_key",
        help="Access Token Key",
        required=True,
        type=validate_access_token_key
    )

    parser.add_argument(
        "-ts", "--token_secret",
        help="Access Token Secret",
        required=True,
        type=validate_access_token_secret
    )

    return parser.parse_args()