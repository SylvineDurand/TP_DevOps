import os
import requests
import time

# Retrieve the value of the environment variable "NAME" or use a default value
name = os.environ.get('NAME', 'default_name')

print(f"Bonjour {name}, voici une blague de Chuck Norris :")

# utilisation d'une librairie
def get_random_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    
    if response.status_code == 200:
        joke_data = response.json()
        joke = joke_data["value"]
        print(f"Chuck Norris Joke: {joke}")
    else:
        print(f"Failed to fetch Chuck Norris joke. Status code: {response.status_code}")

if __name__ == "__main__":
    get_random_chuck_norris_joke()

# création d'une boucle infinie
start_time = time.time()

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    print(f"Time elapsed: {elapsed_time:.2f} seconds")

    # Sleep for 5 seconds
    time.sleep(5)