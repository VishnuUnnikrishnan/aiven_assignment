# Aiven Assignment: Page Up

## Summary:
This application checks if a webpage is available or not then pushes that information through a Kafka topic to a Postgres database. 

## Functional Overview

Page Up comprises of 3 major modules and 2 support modules. These are:
1. web_connect.py -- this module attempts to connect to a web page and returns the HTTP status, time elapsed, and an optional regex pattern match and if it is not able to it will return the error message associated with the exception that was raised.
2. kafka.py -- This module contains a wrapper for the python kafka consumer and producer classes provided by KafkaPython. It handles communications with a remote kafka instance and supports both SSL and non-SSL (for testing).
3. Database.py -- this module connects to a postgres database and writes to it. It uses pyscopg2 to handle communications with the database and will support SSL and non SSL communications. 
4. log.py -- The fourth module is for logging. To prevent file write conflicts, this module is shared as a single instance among the other classes.
5. settings_classes.py -- This module loads the settings.json file which contains all of teh configuration details for the application. 

### Scripts:
Two scripts are available as part of the page up package.Two scripts exist too allow for both distributed and non-distributed mode operation.

1. web_check.py -- This script will check if a page is available and upload the information to a Kafka topic
2. db_upload.py -- This script will download data from a kafka topic and upload it to a postgres database


## Assumptions

The following assumptions were made during the development of the code.

1. The database and database tables already exist and do not need to be set up.
2. The Kafka instance and topic have already been set up.

## Installation

There are two methods that can be used for installation, manually or through automation.

### Requirements

1. Linux distribution 
2. Python 3 and pip installed
3. 

### Automation

1. Download the [install.sh](https://raw.githubusercontent.com/VishnuUnnikrishnan/avien_assignment/main/automation/install.sh) script to the folder you want the application to be installed in.
2. Change permissions of the downloaded file to allow execution chmod +x install.sh
3. Run script

The script will create the required environment and install the 
