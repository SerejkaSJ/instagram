import requests

def load_image(url, path):
    response = requests.get(url)
    if response.ok:
        with open(path, 'wb') as file:
            file.write(response.content)
    else:
        print("Error load image")
   