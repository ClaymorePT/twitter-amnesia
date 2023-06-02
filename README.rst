Twitter Amnesia
===============

.. image:: https://badge.fury.io/py/twitter-amnesia.svg
    :target: https://badge.fury.io/py/twitter-amnesia

.. image:: https://circleci.com/gh/ClaymorePT/twitter-amnesia.svg?style=svg
    :target: https://circleci.com/gh/ClaymorePT/twitter-amnesia

Introduction
~~~~~~~~~~~~

A service which can be deployed to erase tweets older than a specific
date and not marked with a custom tag

Requirements
~~~~~~~~~~~~

-  Python 3.11
-  For required Python modules, check requirements.txt

Installation
~~~~~~~~~~~~

**Note: Use a virtual environment**

This package is available in Pypi.
To install, just use pip.
``$ pip install twitter-amnesia``

Usage
~~~~~

When installed, twitter-amnesia can be executed by calling the
executable in the terminal. This service requires a configuration file.

Example:
::

   $ twitter-amnesia -c <service yaml config file location>


Example of a configuration YAML file contents. There's one available at `config-example/service-config.yaml <config-example/service-config.yaml>`_ .
::

    twitter:
        bearer_token: "<Bearer Token>" # Tweeter API Bearer Token. This requires at least a Free API Development Account
        username: "<Twitter Username>" # Your Twitter Handle

    protection_tag: "<Protection Tag>" # Format Example: [P]
    storage_location: "./storage" # Optional Configuration: Location to where to store Tweets before deleting them.
    days_to_expire: 30 # Tweets lifetime. Tweets older than X Days will be deleted.




Options
~~~~~~~

Other options can be cnsulted using the ``--help``

::

   $ twitter-amnesia.exe --help
   usage: twitter_amnesia [-h] -c CONFIGURATION_FILE [-l {INFO,WARNING,ERROR,CRITICAL}]

   Twitter Amnesia Service

   options:
   -h, --help            show this help message and exit
   -c CONFIGURATION_FILE, --configuration_file CONFIGURATION_FILE
                           YAML Configuration file to be used.
   -l {INFO,WARNING,ERROR,CRITICAL}, --logLevel {INFO,WARNING,ERROR,CRITICAL}
                           Logging Level (default: INFO)

Copyright
~~~~~~~~~

This project is protected under the GPLv3 License.