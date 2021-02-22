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

### Automation

1. Download the [install.sh](https://raw.githubusercontent.com/VishnuUnnikrishnan/avien_assignment/main/automation/install.sh) script to the folder you want the application to be installed in.
2. Change permissions of the downloaded file to allow execution 
  ```shell
  chmod +x install.sh
  ```
3. Run script, The script will create the required environment folders and install the CRON job using 
```shell
./install.sh 3.
```
4. Add the required certificates and keys to the .secret folder. In that folder you will also find a file called dbpass, add your password to that file.
5. Update the settings.json file. This file is very important as it controls everything.

The default cron job is set to run once per minute and consequently the db table will be updated every minute.

#### Distributed Mode
It is possible to install in distributed mode. 

1. ./install.sh 1 -- will install only the web page checker and Kafka producer component.
```shell
  ./install.sh 1
```
2. ./install.sh 2 -- will install only the kafka consumer and Database writer portion.
```shell
  ./install.sh 1
```
You will need to update settings.json for each componnet, but you only need to update the relevant sections.  

### Manual
1. Download the latests release by going to the dist folder and downloading the tar.gz file. This is a source distribution.
2. Run pip install xxxx.tar.gz
3. You will be able to now use any of the available classes and scripts to build your own implementation.
4. You will need to manually setup the environment folders etc for the available scriipts to run.

### Settings.json
This file contains all user configuration. Consequently this file should be one of two files edited by the user. This file needs to be in JSON format.
|Key|Default Value|Description|
|-|-|-|
|"URL"|"https://www.google.com"| Required This is the page that will be checked|
|"REGEX"|""|Required This is the Regex that will be checked on page. The default will always be matched|
|"KAFKA_SERVER"|"localhost"| Required, The kafka server hostname|
|"KAFKA_PORT" | 9092|Required, The kafka server port |
|"KAFKA_TOPIC" | "PageUp"|Required, The kafka topic |
|"KAFKA_PROTOCOL" | "SSL"|Optional, The kafka connection protocol. SSL is reccommended as it is secure, if this is removed it will drop to non-SSL  comms |
|"KAFKA_CLIENT_ID" | "assn_client"|Required, The kafka consumer client id |
|"KAFKA_GROUP_ID" | "assn_client"|Required, The kafka consumer group id |
|"KAFKA_CA_FILE"| ".secrets/ca.pem"|Required if KFKA_PROTOCOL is set|
|"KAFKA_CERT_FILE"|".secrets/service.cert"|Required if KFKA_PROTOCOL is set|
|"KAFKA_KEY_FILE"|.secrets/service.key"|Required if KFKA_PROTOCOL is set|
|"DB_PROTOCOL" | "SSL"|Optional, The DB connection protocol. SSL is reccommended as it is secure, if this is removed it will drop to non-SSL  comms |
|"DB_NAME" | "pageup"|Required, the DB name|
|"DB_USER" | "postgres"|Required the DB username|
|"DB_PASSWORD" | ".secrets/dbpass"|Required the DB password. This is a file location as it is bad practice to have passwords in source code.|
|"DB_HOST" | "localhost"|Required Database server hostname|
|"DB_PORT" | 5432|Required Database port|
|"DB_TABLE" | "pageup"|Required DB table name|

### .secrets/
Add certificates, keys into this folder. Ideally in a secure environment this should be replaced with hashicorp vault, cyberark or some are secrets locker solution. If you want to use a different folder or location, just edit the corresponding setting in settings.json. You will notice that the .secrets file has not been uploaded to github, this is for security purposes.

### .secrets/dbpass
This file contains the db password. This also needs to be updated by the user. What this does is prevent the password being exposed in source code.

## Testing
Unit testing was carried out for all of the main modules.




