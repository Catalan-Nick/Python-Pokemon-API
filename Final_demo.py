from caller import call_api
from switcher import validation, switch 
from display import poke_info
user_choice = 0  
while user_choice != 4:

    user_choice = input("\nHello and welcome to the wonderful world of Pokemon!\nPlease pick an option from the following:\n1. 'I know the name of the pokemon I want information on'\n2. 'I want a list of all pokemon to choose one from'\n3. 'Show me information on a random pokemon'\n4. 'I don't want information on pokemon, EXIT' ")
    
    user_choice = validation(user_choice)
    url = switch(user_choice)
    if user_choice != 4:
        pokemon = call_api(url)
        if type(pokemon) == dict:
            poke_info(pokemon)
        else:
            print("\nGoodbye\n")
            break
    else:
        print("\nGoodbye\n")