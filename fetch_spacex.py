import requests
import json

directory = 'images/'


def load_image(url, path):
  response = requests.get(url)
  with open(path, 'wb') as file:
    file.write(response.content)


def fetch_spacex_last_launch(folder, flight_number = "latest"):
    if not flight_number:
        flight_number = "latest"
    url = "https://api.spacexdata.com/v3/launches/{}"
    response = requests.get(url.format(flight_number))
    result = response.json()
    for number, link in enumerate(result['links']['flickr_images']):
        load_image(link, folder + 'space{}.jpg'.format(number))
      
      
if __name__ == "__main__":
    fetch_spacex_last_launch(directory)