# 🧬 PokeStats Explorer

A command-line data analysis tool that fetches real-time Pokémon stats using [PokeAPI](https://pokeapi.co/), processes them with `pandas`, and visualizes them with `matplotlib`.

Built with: Python, pandas, matplotlib

---

## 🚀 Features

✅ Pull real-time stats for any Pokémon  
✅ Filter by type (e.g., Electric, Fire, Ghost)  
✅ Sort and display top Pokémon by stat (e.g., Speed, Attack)  
✅ Visualize top stats with bar charts  
✅ Show type distribution with pie charts  
✅ Export data to CSV  
✅ Local caching to speed up repeated requests  
✅ Clear cache with one command

---

## 🖼️ Preview

Coming soon — screenshots or GIFs of CLI and visual charts

---

## 💻 How to Run

1. **Clone the repo:**
   ```bash
   git clone https://github.com/rinnemunch/pokestats-explorer.git
   cd pokestats-explorer

2. Create a virtual environment: 
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

3. Install dependencies: 
pip install -r requirements.txt

4. Run the program: 
python main.py

Project Structure:

poke_api.py      # Fetches + caches API data
data_utils.py    # Filtering, sorting, and export logic
visuals.py       # Chart and graph rendering
main.py          # CLI interface
cache/           # Stored Pokémon data (JSON)

📝 Notes 
Requires internet connection for initial fetches

Cached data is saved in cache/ folder

Tested with Python 3.10+