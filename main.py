#Import libraries that will be used
import json                       # json library to read json file formats
import pprint                     # Prints in a nice way
import requests                   # Uses the requests library for REST APIs
import os                         # Loads operating system libraries
from ldaca.ldaca import LDaCA     # Loads the LDaCA ReST API wrapper
from rocrate_lang.utils import as_list # A handy utility for converting to list


# Specify the path to the collections as well as the LDaCA API and require an API token
# Specify location where collection is
LDACA_API = 'https://data.ldaca.edu.au/api'
COLLECTION_ID = 'arcp://name,doi10.4225%2F35%2F555d661071c76'
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
    if 'File' in as_list(entity.type):
        print(f"entity id: {entity.get('@id')}")
        ldaca.download_file(entity.id, entity.id.split('&path=')[1],DOWNLOAD_DIR) #.replace('/','_'))

#before zipping, make an ro-crate file, python library, save the ro-crate. write ro-crate into downloaded_data ro-crate-metadata.json
#where to find the ro-crate-metadata.json
ldaca.crate.write('downloaded_data')
for e in ldaca.crate.get_entities():
    if 'File' in as_list(e.type):
        print(e.get('@id'))

# Create a zip file from the directory
import zipfile
import shutil
shutil.make_archive(base_name='downloaded_data', format='zip', root_dir='downloaded_data')

#add command to delete downloaded_data