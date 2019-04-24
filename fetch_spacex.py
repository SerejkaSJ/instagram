import requests
import json
from load_image import load_image
directory = 'images/'


def fetch_spacex_last_launch(folder, flight_number = "latest"):
    if not flight_number:
        flight_number = "latest"
    url = "https://api.spacexdata.com/v3/launches/{}"
    response = requests.get(url.format(flight_number))
    response.raise_for_status()
    result = response.json()
    for number, link in enumerate(result['links']['flickr_images']):
        load_image(link, folder + 'space{}.jpg'.format(number))
      
      
if __name__ == "__main__":
    try:
        fetch_spacex_last_launch(directory)
    except  requests.exceptions.HTTPError as err:
        print("Error request http:", err)     