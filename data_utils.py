def filter_by_type(df, poke_type):
    return df[df["Type(s)"].str.contains(poke_type.title())]


def sort_by_stat(df, stat_name, top_n=5):
    if stat_name.title() in df.columns:
        return df.sort_values(by=stat_name.title(), ascending=False).head(top_n)
    else:
        print("Stat not found.")
        return df


def export_to_csv(df, filename="pokemon_data.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"✅ Data exported to {filename}")
    except Exception as e:
        print(f"❌ Export failed: {e}")
