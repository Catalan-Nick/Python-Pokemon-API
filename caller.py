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
