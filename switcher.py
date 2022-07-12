# TODO: 
    # option 3 messes up sometimes - maybe fixed
    #when 404 need to give option to exit
 
from random import randrange
from subprocess import call
from caller import call_api
# takes name or id and places it in url
def option1():
    user_request = input("What Pokemon do you want information on? ")
    url = (f"https://pokeapi.co/api/v2/pokemon/{user_request.lower()}")
    return url
# gives list of all pokemon and asks for a selection
def option2():
    all_pokemon = "https://pokeapi.co/api/v2/pokemon/?offset=0&limit=1000"
    pokemon = call_api(all_pokemon)
    for result in pokemon['results']:
        print(result['name'])
    user_request = input("What Pokemon do you want information on? ")
    url = (f"https://pokeapi.co/api/v2/pokemon/{user_request.lower()}")
    return url
# gives random pokemon url
def option3():
    random_num = randrange(904)
    url = f"https://pokeapi.co/api/v2/pokemon/{random_num}"
    return url
# exits
def option4():
    return "Goodbye"

def default():
    return "Please read options and pick again"

switcher = {
    1: option1,
    2: option2,
    3: option3,
    4: option4,
}
    # switch takes the users choice,
    # gets the option name from switcher object,
    # and uses that string to call on the function that corresponds with user choice. 
def switch(option_num):
    return switcher.get(option_num, default)()

    # validates user entered an int, default() invalidates everything except 1-4
def validation(user_choice):
    try:
        user_choice = int(user_choice)
        if user_choice > 0 and user_choice < 5:
            return user_choice
        else:
            user_choice = input("Invalid input, type 1, 2, 3, or 4: ")
            user_choice = validation(user_choice)
            return user_choice
    except:
        user_choice = input("Invalid input, type 1, 2, 3, or 4: ")
        user_choice = validation(user_choice)
        return user_choice
