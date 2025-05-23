from poke_api import get_pokemon_stats_as_df

df = get_pokemon_stats_as_df("Charizard")
if df is not None:
    print(df)
