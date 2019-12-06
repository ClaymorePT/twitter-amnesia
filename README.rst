Twitter Amnesia
===============

.. image:: https://badge.fury.io/py/twitter-amnesia.svg
    :target: https://badge.fury.io/py/twitter-amnesia

Introduction
~~~~~~~~~~~~

A service which can be deployed to erase tweets older than a specific
date and not marked with a custom tag

Requirements
~~~~~~~~~~~~

-  Python 3.8
-  Required Python modules.

   -  python-twitter==3.5
   -  python-dateutil==2.8.1

Installation
~~~~~~~~~~~~

**Note: Use a virtual environment**

Inside the folder to where the repository was cloned, simply execute:
``$ pip install .``

The name of the package is ``twitter_amnesia``

Usage
~~~~~

When installed, twitter-amnesia can be executed by calling the
executable in the terminal.

Example:

::

   $ twitter-amnesia -ck abcdefghijklmnopqrstuvwxy -cs abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWX -tk 12345678-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNO -ts abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS

twitter-amnesia will immediately remove all tweets older than 1 month
(default).

Options
~~~~~~~

Other options can be cnsulted using the ``--help``

::

   $ twitter-amnesia --help
   usage: twitter-amnesia [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}] [-d DAYS]
                          [-m MONTHS] [-y YEARS] [-t PROTECTION_TAG]
                          [-f SAVING_DIRECTORY] -ck CONSUMER_KEY -cs
                          CONSUMER_SECRET -tk TOKEN_KEY -ts TOKEN_SECRET

   optional arguments:
     -h, --help            show this help message and exit
     -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logLevel {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                           Logging Level (default: INFO)
     -d DAYS, --days DAYS  Tweets older than 0 days (default value)
     -m MONTHS, --months MONTHS
                           Tweets older than 1 months (default value)
     -y YEARS, --years YEARS
                           Tweets older than 0 years (default value)
     -t PROTECTION_TAG, --protection_tag PROTECTION_TAG
                           Protection Tag (default: [P])
     -f SAVING_DIRECTORY, --saving_directory SAVING_DIRECTORY
                           Directory location to where deleted tweets are
                           exported (default: None)
     -ck CONSUMER_KEY, --consumer_key CONSUMER_KEY
                           Consumer Key
     -cs CONSUMER_SECRET, --consumer_secret CONSUMER_SECRET
                           Consumer Secret
     -tk TOKEN_KEY, --token_key TOKEN_KEY
                           Access Token Key
     -ts TOKEN_SECRET, --token_secret TOKEN_SECRET
                           Access Token Secret

Copyright
~~~~~~~~~

This project is protected under the GPLv3 License.