from ldaca.ldaca import LDaCA
from dotenv import load_dotenv
import os
import shutil

load_dotenv('vars.env')
API_TOKEN = os.getenv('API_KEY')
URL = 'https://data.ldaca.edu.au/api'
COLLECTION = os.getenv('COLLECTION')
print(f"URL: {URL}")

data_dir = 'oni_data'
ldaca = LDaCA(url=URL, token=API_TOKEN, data_dir=data_dir)
ldaca.set_collection(COLLECTION)
ldaca.set_collection_type('Collection')

ldaca.retrieve_collection(
    collection=COLLECTION,
    collection_type='Collection',
    data_dir=data_dir)

all_files = ldaca.store_data(entity_type='RepositoryObject')
print(f"Files downloaded, zipping directory.")

# Create a zip file from the directory
shutil.make_archive(base_name=data_dir, format='zip', root_dir=data_dir)