import matplotlib.pyplot as plt


def plot_top_stat(df, stat_name, top_n=5):
    stat_col = stat_name.title()
    if stat_col not in df.columns:
        print("Stat not found.")
        return

    top_df = df.sort_values(by=stat_col, ascending=False).head(top_n)

    plt.figure(figsize=(10, 6))
    plt.bar(top_df["Name"], top_df[stat_col], color="skyblue")
    plt.title(f"Top {top_n} Pokémon by {stat_col}")
    plt.xlabel("Pokémon")
    plt.ylabel(stat_col)
    plt.tight_layout()
    plt.show()


def plot_type_distribution(df):
    type_counts = {}

    for types in df["Type(s)"]:
        for t in types.split(", "):
            type_counts[t] = type_counts.get(t, 0) + 1

    labels = list(type_counts.keys())
    sizes = list(type_counts.values())

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title("Type Distribution")
    plt.tight_layout()
    plt.show()
