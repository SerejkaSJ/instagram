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
    if response.ok:
        result = response.json()
        link = result['image_files'][-1]['file_url']
        path = urllib.parse.urlparse(link).path
        extension = get_extension(path)
        load_image(link, '{}{}.{}'.format(directory, id_image, extension))
    else:
        print("Error loading pictures")
      

def load_image_from_hubble_collection(collection_name, directory):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {
        'page' : 'all',
        'collection_name' : collection_name
    }
    response = requests.get(url, json = payload)
    if response.ok:
        collections = response.json()
        for number, collection in enumerate(collections):
            load_image_from_hubble_id(collection['id'], directory)
    else:
        print("Error retrieving collection information")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("collection_name")
    args = parser.parse_args()
    your_collection = args.collection_name
    load_image_from_hubble_collection(your_collection, directory)