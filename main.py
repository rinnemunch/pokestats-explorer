from poke_api import get_multiple_pokemon
from data_utils import filter_by_type, sort_by_stat
from visuals import plot_top_stat, plot_type_distribution

names = ["Pikachu", "Charizard", "Bulbasaur", "Gengar", "Jolteon", "Machamp"]
df = get_multiple_pokemon(names)

if not df.empty:
    electric_df = filter_by_type(df, "Electric")
    print("\nElectric Type Pokémon:")
    print(electric_df)

    top_speed = sort_by_stat(df, "Speed", top_n=3)
    print("\nTop 3 by Speed:")
    print(top_speed)

plot_top_stat(df, "Attack", top_n=5)
plot_type_distribution(df)
