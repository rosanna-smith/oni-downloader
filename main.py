#Import libraries that will be used
import json                       # json library to read json file formats
import pprint                     # Prints in a nice way
import requests                   # Uses the requests library for REST APIs
import os                         # Loads operating system libraries
from ldaca.ldaca import LDaCA     # Loads the LDaCA ReST API wrapper
from rocrate_lang.utils import as_list # A handy utility for converting to list


# Specify the path to the collections as well as the LDaCA API and require an API token
# Specify location where collection is
LDACA_API = 'https://data.atap.edu.au/api'
COLLECTION_ID = 'arcp://name,farms-to-freeways-example-dataset'
DOWNLOAD_DIR = 'downloaded_data'
from dotenv import load_dotenv    # Loads environment variables
load_dotenv('vars.env') # Load the environment variables located in the vars.env files
API_TOKEN = os.getenv('API_KEY') # Store your environment variable
if not API_TOKEN:
    print("Set a variable in the vars.env file and name API_KEY")


# Get the collection metadata by passing the ArcPID in as a parameter to the get request
ldaca = LDaCA(url=LDACA_API, token=API_TOKEN, data_dir='data')
ldaca.retrieve_collection(collection=COLLECTION_ID, collection_type='Collection', data_dir='data')

metadata = ldaca.crate


# Find all types and find types that have linked objects
files = set()
types = list()
primary_object_types = list()

# Lets see what we can find in our metadata
for entity in ldaca.crate.contextual_entities + ldaca.crate.data_entities:
    entity_type = as_list(entity.type)  # We make sure that each type is a list
    for e_t in entity_type:
        types.append(e_t)

# Types of PRIMARY_OBJECTs ie [PRIMARY_OBJECT, X]. What kinds of Xs do we have?
for entity in ldaca.crate.data_entities:
    #print(entity.id,entity.type)  #debug check
    if 'File' in as_list(entity.type):
        print(entity.get('name'))
        #print(entity.get('@id'))
        #ldaca.download_file(entity.id, entity.id.split('&path=')[1],DOWNLOAD_DIR) #.replace('/','_'))
        #print(entity.id.split('&path=')[1])

#before zipping, make an ro-crate file, python library, save the ro-crate. write ro-crate into downloaded_data ro-crate-metadata.json
#where to find the ro-crate-metadata.json
#ldaca.crate.write_zip('ro-crate-metadata.json.zip')
for e in ldaca.crate.get_entities():
    if 'File' in as_list(e.type):
        print(e.get('@id'))
#    if e["@id"] == "arcp://name,farms-to-freeways-example-dataset":
#        print(e)
with open('downloaded_data/ro-crate-metadata.json', 'w') as f:
    json.dump(ldaca.crate.metadata.generate(), f)

# Create a zip file from the directory
import zipfile
import shutil
shutil.make_archive(base_name='downloaded_data_zipped', format='zip', root_dir='downloaded_data')

#add command to delete downloaded_data

#files.add(file)
"""
# Create a directory - option 1
from pathlib import Path
cwd = Path.cwd()
joined_path = cwd / 'downloaded_data'
joined_path.mkdir(exist_ok=True) #exist_ok to ignore file exists error if target directory already exists

# Create a directory - option 2
# Make a relative directory path for files to be downloaded into
from pathlib import Path
# Construct the path to the directory
directory_path = Path(r"downloaded_data")
# Make the directory by calling mkdir() on the path instance
directory_path.mkdir()
# Report the result
print(f"Successfully made the '{directory_path}' directory.")


# Create a zip file from a directory

from zipfile import ZipFile, ZIP_DEFLATED
import pathlib

zip_path = './downloaded_data.zip'

folder = pathlib.Path(DOWNLOAD_DIR)

with ZipFile(zip_path, 'w', ZIP_DEFLATED) as zip:
    for file in folder.iterdir():
        zip.write(file) # change to (file, arcname=file.name) if you want the zip to open the files directly rather than going to a downloaded_data folder first
"""