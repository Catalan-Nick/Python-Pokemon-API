from random import randrange

def poke_info(pokemon):
    
    id_pokemon = pokemon['id']
    print(f"\nID#: {id_pokemon}")
    
    p_name = pokemon['name']
    
    print(f"Name:\n\t{p_name.capitalize()}")
    
    # type
    print("Types:")
    for p_type in pokemon['types']:
        types = p_type.get('type')
        print(f"\t{types.get('name')}")
        
    # ability
    print("Abilities:")
    for ability in pokemon['abilities']:
        a_name = ability.get('ability')
        print(f"\t{a_name.get('name')}")
        
    #Moves
    print(f"Four random {p_name.capitalize()} Moves:")
    # print(len(pokemon['moves']))
    # move_entry = pokemon['moves']
    # print(f"move 0 is: {move_entry[0]}")     
    # for move in pokemon['moves']:
    #     move_name = move.get('move')
    #     print(move_name.get('name'))
    
    # get the length of how many moves there are,
    # use that number to make a random number
    # print the name of that move
    moves_length = len(pokemon['moves'])
    
    i = 0
    while(i < 4):
        random_num = randrange(moves_length - 1)
        move_entry = pokemon['moves']
        move_random = move_entry[random_num]
        move_random_entry = move_random.get('move')
        move_random_name = move_random_entry.get('name')
        print(f"\t{move_random_name}")
        i = i + 1
    