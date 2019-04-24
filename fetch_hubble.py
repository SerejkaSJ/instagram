import requests
import json
import argparse
import urllib
from load_image import load_image

directory = 'images/'


def get_extension(path):
    if '\\' in path:
        extension = path.split('\\')[-1].split('.')[1]
    elif '/' in path:
        extension = path.split('/')[-1].split('.')[1]
    else:
        extension = path.split('.')[1]
    return extension

def load_image_from_hubble_id(id_image, directory):
    url = 'http://hubblesite.org/api/v3/image/{}'
    response = requests.get(url.format(id_image))
    response.raise_for_status()
    result = response.json()
    link = result['image_files'][-1]['file_url']
    path = urllib.parse.urlparse(link).path
    extension = get_extension(path)
    load_image(link, '{}{}.{}'.format(directory, id_image, extension))
      

def load_image_from_hubble_collection(collection_name, directory):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {
        'page' : 'all',
        'collection_name' : collection_name
    }
    response = requests.get(url, json = payload)
    response.raise_for_status()
    collections = response.json()
    for number, collection in enumerate(collections):
        load_image_from_hubble_id(collection['id'], directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("collection_name")
    args = parser.parse_args()
    your_collection = args.collection_name
    try:
        load_image_from_hubble_collection(your_collection, directory)
    except  requests.exceptions.HTTPError as err:
        print("Error request http:", err)    
        