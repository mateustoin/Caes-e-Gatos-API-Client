# This Python file uses the following encoding: utf-8
import requests
from random import randint


class AnimalFetch:
    def __init__(self):
        self.current_extension = None
        self.response = None

        # Cat field -> Origin cat API: https://cataas.com/#/
        self.cat_url = 'https://cataas.com/cat'
        self.previous_cat_url = []

        # Dog field -> Origin API
        self.dog_url_1 = 'https://place.dog/600/600'
        self.dog_url_2 = 'https://dog.ceo/api/breeds/image/random'
        self.dog_url_3 = 'https://random.dog/woof.json'
        self.previous_dog_url = []

        # Fox field -> Origin API: https://randomfox.ca/floof/
        self.fox_url = 'https://randomfox.ca/floof/'
        self.previous_fox_url = []

        # Duck field -> Origin API: https://random-d.uk/
        self.duck_url = 'https://random-d.uk/api/random'
        self.previous_duck_url = []

    def get_dog_1_content(self):
        self.response = requests.get(self.dog_url_1)
        # print(self.response.json())
        self.current_extension = 'jpg'
        return self.response.content
        # current_url =
        # self.previous_dog_url

    def get_dog_2_content(self):
        self.response = requests.get(self.dog_url_2)
        url = self.response.json()['message']
        self.previous_dog_url.append(url)
        self.current_extension = url.split('.')[-1]
        self.response = requests.get(url)
        return self.response.content

    def get_dog_3_content(self):
        self.response = requests.get(self.dog_url_3)
        url = self.response.json()['url']
        self.previous_dog_url.append(url)
        self.current_extension = url.split('.')[-1]
        self.response = requests.get(url)
        return self.response.content

    def get_duck_content(self):
        self.response = requests.get(self.duck_url)
        url = self.response.json()['url']
        self.previous_dog_url.append(url)
        self.current_extension = url.split('.')[-1]
        self.response = requests.get(url)
        return self.response.content

    def get_fox_content(self):
        self.response = requests.get(self.fox_url)
        url = self.response.json()['image']
        self.previous_dog_url.append(url)
        self.current_extension = url.split('.')[-1]
        self.response = requests.get(url)
        return self.response.content

    def get_cat_content(self):
        self.response = requests.get(self.cat_url)
        # print(self.response.json())
        self.current_extension = 'jpg'
        return self.response.content

    def get_name_and_image_extension(self):
        return str(randint(0, 100000)), self.current_extension
