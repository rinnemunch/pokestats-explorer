import requests
import pandas as pd


def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Pokémon not found.")
        return None


def get_pokemon_stats_as_df(name):
    data = get_pokemon(name)
    if not data:
        return None

    stats = {
        "Name": name.title(),
        "Type(s)": ", ".join([t["type"]["name"].title() for t in data["types"]])
    }

    for stat in data["stats"]:
        stat_name = stat["stat"]["name"].title()
        stats[stat_name] = stat["base_stat"]

    return pd.DataFrame([stats])


def get_multiple_pokemon(names):
    all_data = []

    for name in names:
        df = get_pokemon_stats_as_df(name)
        if df is not None:
            all_data.append(df)

    if all_data:
        return pd.concat(all_data, ignore_index=True)
    else:
        return pd.DataFrame()
