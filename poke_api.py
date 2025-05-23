import requests
import pandas as pd
import os
import json

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)


def get_pokemon(name):
    name = name.lower()
    cache_path = os.path.join(CACHE_DIR, f"{name}.json")

    if os.path.exists(cache_path):
        with open(cache_path, "r") as file:
            print(f"📁 Loaded {name} from cache")
            return json.load(file)

    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(cache_path, "w") as file:
            json.dump(data, file)
        print(f"🌐 Fetched {name} from API and cached it")
        return data
    else:
        print(f"❌ Pokémon '{name}' not found.")
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


def clear_cache():
    for filename in os.listdir(CACHE_DIR):
        file_path = os.path.join(CACHE_DIR, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    print("🧹 Cache cleared.")
