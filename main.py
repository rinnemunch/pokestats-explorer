from poke_api import get_multiple_pokemon
from data_utils import filter_by_type
from visuals import plot_top_stat, plot_type_distribution


def main():
    print("🧬 Welcome to PokeStats Explorer!")

    names = input("Enter Pokémon names (comma-separated): ").split(",")
    names = [name.strip() for name in names]

    df = get_multiple_pokemon(names)

    if df.empty:
        print("❌ No data found.")
        return

    while True:
        print("\nChoose an option:")
        print("1. Show full DataFrame")
        print("2. Filter by type")
        print("3. Show top Pokémon by stat")
        print("4. Show type distribution pie chart")
        print("5. Exit")
        print("6. Export DataFrame to CSV")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print(df)

        elif choice == "2":
            poke_type = input("Enter a Pokémon type (e.g., Fire, Electric): ")
            filtered = filter_by_type(df, poke_type)
            print(filtered if not filtered.empty else "No Pokémon of that type.")

        elif choice == "3":
            stat = input("Enter stat name (HP, Attack, Defense, Speed, etc.): ")
            top_n = input("How many top Pokémon to show? ")
            try:
                top_n = int(top_n)
                plot_top_stat(df, stat, top_n)
            except ValueError:
                print("Invalid number.")

        elif choice == "4":
            plot_type_distribution(df)

        elif choice == "5":
            print("👋 Exiting. Thanks for using PokeStats Explorer!")
            break
        elif choice == "6":
            filename = input("Enter filename (default: pokemon_data.csv): ").strip()
            if filename == "":
                filename = "pokemon_data.csv"
            from data_utils import export_to_csv
            export_to_csv(df, filename)

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
