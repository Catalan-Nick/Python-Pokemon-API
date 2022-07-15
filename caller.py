import requests

def call_api(url):
    try:
        req = requests.get(url)
        pokemon = req.json()
        return pokemon
    except:
        print(f"\nError: {req.status_code} {url}")
        print("Couldn't find that pokemon, check spelling and try again")
        user_request = input("What Pokemon do you want information on? Or type 'exit' ")
        if user_request.lower() != 'exit':
            url = (f"https://pokeapi.co/api/v2/pokemon/{user_request.lower()}")
            pokemon = call_api(url)
        else:
            pokemon = None
        return pokemon
def get_accuracy(url):
    try:
        req = requests.get(f"{url}")
        move = req.json()
        accuracy = move['accuracy']
        if accuracy == None:
            accuracy = "Status"
        return accuracy
    except:
        accuracy = "No Move Found"
        return accuracy

def get_power(url):
    try:
        req = requests.get(f"{url}")
        move = req.json()
        power = move['power']
        if power == None:
            power = 0
        return power
    except:
        power = "No Move Found"
        return power