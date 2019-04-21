import requests
import json
import argparse

directory = 'images/'


def load_image(url, path):
  response = requests.get(url)
  with open(path, 'wb') as file:
    file.write(response.content)


def get_extension(path_or_file):
    if '\\' in path_or_file:
        extension = path_or_file.split('\\')[-1].split('.')[1]
    elif '/' in path_or_file:
        extension = path_or_file.split('/')[-1].split('.')[1]
    else:
        extension = path_or_file.split('.')[1]
    return extension

def load_image_from_hubble_id(id_image, directory):
    url = 'http://hubblesite.org/api/v3/image/{}'
    response = requests.get(url.format(id_image))
    result = response.json()
    link = result['image_files'][-1]['file_url']
    extension = get_extension(link)
    load_image(link, '{}{}.{}'.format(directory, id_image, extension))
      

def load_image_from_hubble_collection(collection_name, directory):
    url = 'http://hubblesite.org/api/v3/images'
    payload = {
        'page' : 'all',
        'collection_name' : collection_name
    }
    response = requests.get(url, json = payload)
    collections = response.json()
    for number, collection in enumerate(collections):
        print(number, collection)
        load_image_from_hubble_id(collection['id'], directory)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("collection_name")
    args = parser.parse_args()
    your_collection = args.collection_name
    load_image_from_hubble_collection(your_collection, directory)