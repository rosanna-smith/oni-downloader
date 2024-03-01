# Oni Downloader

This downloader uses the Oni API to allow you to select (coming soon) and download data from available collections.

## Load a Virtual Environment (this section is just needed for testing currently)

#### Create the virtual environment space in your current directory by running the followibng Terminal command:
python -m venv venv

This will create the folder venv/

#### To activate the virtual environment, run:
. venv/bin/activate

#### To close the virtual environment, run:
deactivate

#### To remove the virtual environment completely, run:
rm -rf venv

## Install all the requirements needed using the requirements.txt file
pip install -r requirements.txt

pip install setuptools

## Enter your API key
Sign into the ATAP data portal and get an API key from your User Info page. You may need to authenticate and request access via REMS first. Edit the vars.env file and add the API_KEY. An example is shown below of the required format.

API_KEY=153b2db8-4536-4016-8bd6-311e8817e764