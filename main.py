from poke_api import get_multiple_pokemon

pokemon_names = ["Pikachu", "Charizard", "Bulbasaur", "Gengar"]
df = get_multiple_pokemon(pokemon_names)

if not df.empty:
    print(df)
else:
    print("No valid Pokémon found.")
