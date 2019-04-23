from instabot import Bot 
import PIL
import os
from dotenv import load_dotenv


def upload_photo(login, password, directory):
    bot = Bot()
    bot.login(username=login, password = password)
    for root, dirs, filenames in os.walk(directory):
        for f in filenames:
            bot.upload_photo(os.path.join(root, f)) 

      
if __name__ == "__main__":
    load_dotenv()
    directory = 'images/'
    login = os.getenv("login")
    password = os.getenv("password")
    upload_photo(login, password, directory)