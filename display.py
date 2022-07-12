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
        