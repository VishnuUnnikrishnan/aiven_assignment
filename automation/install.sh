#!/bin/bash

# Setup environment for the application to run
echo "Setting up environment"
mkdir ".secrets"
mkdir "logs"
touch ".secrets/dbpass"
curl -o settings.json "https://raw.githubusercontent.com/VishnuUnnikrishnan/avien_assignment/main/automation/settings.json"

#Download the PageUp distribution and install it
curl -L -o PageUp-0.0.5.tar.gz "https://github.com/VishnuUnnikrishnan/avien_assignment/raw/main/dist/PageUp-0.0.5.tar.gz"
pip3 install PageUp-0.0.5.tar.gz

#Setup file path in bash scripts to be used in cron jobs (allows to change directory)

echo "Setup Script"
HEAD=$'#!/bin/bash\n';
CHANGE='cd ';
WEBCHECK=$'\nweb_check.py\n';
DBCHECK=$'\ndb_upload.py\n';

echo $HEAD > pageCheck.sh
echo "PATH="$PATH >> pageCheck.sh
echo $CHANGE" "$PWD >> pageCheck.sh



#Setup scripts that wil be run from cron and setup cron job.

if [[ ( $1 == 1 ) ]];then
echo $WEBCHECK >> pageCheck.sh

elif [[ ( $1 == 2 ) ]];then
echo $DBCHECK >> pageCheck.sh


elif [[ ( $1 == 3 ) ]];then
echo $WEBCHECK >> pageCheck.sh
echo $DBCHECK >> pageCheck.sh

else
echo "Error in options"
exit 1


fi

chmod +x pageCheck.sh

echo "Setup CRON job"
crontab -l > temp_cron
echo "*/1 * * * * "$PWD"/pageCheck.sh" >> temp_cron
crontab temp_cron
rm temp_cron

