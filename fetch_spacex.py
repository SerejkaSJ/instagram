import requests
import json
from load_image import load_image
directory = 'images/'


def fetch_spacex_last_launch(folder, flight_number = "latest"):
    if not flight_number:
        flight_number = "latest"
    url = "https://api.spacexdata.com/v3/launches/{}"
    response = requests.get(url.format(flight_number))
    if response.ok:
        result = response.json()
        for number, link in enumerate(result['links']['flickr_images']):
            load_image(link, folder + 'space{}.jpg'.format(number))
    else:
        print("Error loading pictures")
      
      
if __name__ == "__main__":
    fetch_spacex_last_launch(directory)