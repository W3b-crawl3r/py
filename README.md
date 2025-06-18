# 🏁 Moroccan Checkers Game (Python + Pygame + MySQL)

This is a Moroccan-style checkers game (dames marocaines) developed in Python using `pygame` for visuals and `mysql-connector-python` to store players and match data.

---

## 🎮 Features
- 10x10 checkers board based on Moroccan rules
- Player vs Player or Player vs AI (Minimax algorithm)
- Sultan (king) piece support
- "Neffakh" and "Koul" capturing rules logic
- MySQL database integration to store players and match history

---

## 🧱 Requirements
- Python 3.8+
- Pygame
- MySQL Server (locally installed or remote)
- `mysql-connector-python`

Install dependencies in a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pygame mysql-connector-python
```

---

## 🚀 Running the Game
1. Create the MySQL database manually:
```sql
CREATE DATABASE checkers_db;
```

2. Update `config.py` with your MySQL credentials:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'checkers_db'
}
```

3. Run the game:
```bash
python main.py
```

---

## 📁 Project Structure
```
checkers_game/
├── main.py            # Main game loop and mode selection
├── game.py            # Handles game logic and rendering
├── board.py           # Board and move rules
├── pieces.py          # Piece movement and drawing
├── ai.py              # Minimax AI algorithm
├── database.py        # Save/load players and match results
├── config.py          # MySQL configuration
├── requirements.txt   # Dependencies list
```

---

## 🧠 Game Logic
- `main.py`: asks player to choose game mode (PvP or PvAI)
- `game.py`: manages selection, movement, and turn switching
- `ai.py`: AI player logic using Minimax (search depth: 2)
- `database.py`: stores player names and match results

---

## 🏆 Match Recording
After every completed match, the winner is stored in the `matches` table along with player names and date.

---

## ✍️ Authors
Developed as a CS project to demonstrate:
- Game development with Pygame
- AI using Minimax
- MySQL-Python integration

---

## 📜 License
This project is open for educational purposes. Modify and reuse with credit!
