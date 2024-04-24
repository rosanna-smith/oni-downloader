# Oni Downloader

This downloader uses the Oni API to allow you to select (coming soon) and download data from available collections.

## Load a Virtual Environment

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

Create a file named vars.env and add the following:
```
API_KEY=ENTER_API_KEY_HERE
COLLECTION='ENTER_COLLECTION_ID_HERE'
```

## Enter your API key in vars.env
Sign into the LDaCA data portal and get an API key from your User Info page. You may need to authenticate and request access via REMS first. Edit the vars.env file and add the API_KEY. An example is shown below of the required format.

API_KEY=153b2db8-4536-4016-8bd6-311e8817e764

## Enter the collection in vars.env

Edit the vars.env file and add the collection you want to download in COLLECTION. The collection ID is available from https://data.ldaca.edu.au under the @id on a collection page of your choice.

## To run script

python main.py