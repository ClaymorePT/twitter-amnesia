"""
Twitter Amnesia

A service which can be deployed to erase tweets older than a specific date and not marked with a custom tag
"""

import datetime
import logging
import pickle
import sys
from datetime import datetime, timezone

import rfc3339
from dateutil.relativedelta import relativedelta
from pytwitter import Api

from twitter_amnesia.arg_parsing import parse_arguments
from twitter_amnesia.configuration_parser import load_configurations
from twitter_amnesia.helpers import custom_logging_callback, logger_module_name

# Initialize Exception Hook
sys.excepthook = (lambda tp, val, tb: custom_logging_callback(logging.getLogger(), logging.ERROR, tp, val, tb))


# Initialize logger for this module
_LOG_FORMAT = '[{asctime:^s}][{levelname:^8s}]: {message:s}'
_LOG_FORMAT_DEBUG = '[{asctime:^s}][{levelname:^8s}][{name:s}|{funcName:s}|{lineno:d}]: {message:s}'
_LOG_DATE_FORMAT = '%Y/%m/%d|%H:%M:%S (%Z)'
_log = logging.getLogger(logger_module_name(__file__))


def main():
    """
    The main entry point for this service
    """

    parsed_args = parse_arguments()
    if sys.flags.debug:
        logging.basicConfig(format=_LOG_FORMAT_DEBUG, datefmt=_LOG_DATE_FORMAT, style='{', level=logging.DEBUG)
    else:
        logging.basicConfig(format=_LOG_FORMAT, datefmt=_LOG_DATE_FORMAT, style='{', level=parsed_args.logLevel)

    if sys.flags.debug:
        _log.debug(
            ''.join(['CLI arguments: ']+list((f'  {key:s}: {data:s}' for (key, data) in vars(parsed_args).items())))
        )


    service_configurations = load_configurations(parsed_args.configuration_file)
    username = service_configurations.twitter_configurations.username
    storage_location = service_configurations.storage_location
    protection_tag = service_configurations.protection_tag
    date_until = (datetime.now(timezone.utc) - relativedelta(days=service_configurations.days_to_expire))

    _log.info(
        "Tweeter Amnesia Service Configs: "
        f"Username [{storage_location}]; "
        f"Protection Tag [{storage_location}]; "
        f"Storage Location [{protection_tag}]; "
        f"Deleting Tweets created before than [{date_until.strftime('%Y/%m/%d %H:%M:%S'):s}]"
    )

    api = Api(
        bearer_token=service_configurations.twitter_configurations.bearer_token,
        sleep_on_rate_limit=False
    )

    response = api.get_user(username=username)
    user_id = response.data.id
    _log.info(f"Username is [{username}] with User ID [{user_id}]")

    continue_fecthing = True
    search_parameters = {
        "user_id": user_id,
        "end_time": rfc3339.rfc3339(date_until),
        "tweet_fields": "id,text,created_at"
    }

    removed_tweets_counter = 0
    while continue_fecthing:
        response = api.get_timelines(**search_parameters)

        for tweet in response.data:
            if protection_tag in tweet.text:
                _log.info(f"Tweet with ID [{tweet.id}] skipped. Protection tag present.")
                continue
            else:
                if storage_location:
                    _log.info(f"Saving tweet with ID [{tweet.id}].")
                    with open(f"{storage_location}/{tweet.id}", "wb") as file:
                        pickle.dump(tweet.__dict__, file)

                api.delete_tweet(tweet.id)
                removed_tweets_counter += 1
                _log.warning(f"Tweet [{tweet.id}] deleted.")

        continue_fecthing = response.meta.next_token
        search_parameters = {
            "user_id": user_id,
            "tweet_fields": "id,text,created_at",
            "pagination_token": response.meta.next_token
        }
    _log.info(f"Total number of deleted tweets is [{removed_tweets_counter:d}].")
    _log.info("It's done!")
    exit(0)
