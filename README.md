# Oni Downloader

This downloader uses the Oni API to allow you to select (coming soon) and download data from available collections.

## Load a Virtual Environment

#### Create the virtual environment space in your current directory by running the following Terminal command:
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

Create a file named vars.env and add the following:
```
API_KEY=ENTER_API_KEY_HERE
COLLECTION='ENTER_COLLECTION_ID_HERE'
```

## Enter your API key in vars.env
Sign into the LDaCA data portal and get an API key from your User Info page. You may need to authenticate and request access via REMS first. Edit the vars.env file and add the API_KEY. An example is shown below of the required format.

API_KEY=153b2db8-4536-4016-8bd6-311e8817e764

## Enter the collection in vars.env

Copy a collection @id from https://data.ldaca.edu.au - this is available on any collection page of your choice under the @id section. Add the collection to the vars.env file. An example is shown below of the required format.

COLLECTION='arcp://name,doi10.4225%2F35%2F555d661071c76'

## To run script

python main.py