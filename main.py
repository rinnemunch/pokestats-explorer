from poke_api import get_pokemon

pokemon = get_pokemon("Pikachu")
if pokemon:
    print(f"Name: {pokemon['name'].title()}")
    print("Stats: ")
    for stat in pokemon['stats']:
        print(f" {stat['stat']['name'].title()}: {stat['base_stat']}")
