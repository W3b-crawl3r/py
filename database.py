import mysql.connector
from config import DB_CONFIG

def create_tables():
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            score INT DEFAULT 0
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS saved_games (
            id INT AUTO_INCREMENT PRIMARY KEY,
            player_id INT,
            game_state TEXT,
            FOREIGN KEY (player_id) REFERENCES players(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS matches (
            id INT AUTO_INCREMENT PRIMARY KEY,
            player1 VARCHAR(50),
            player2 VARCHAR(50),
            winner VARCHAR(50),
            date_played TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

def save_player(name):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

def save_game(player_id, state):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO saved_games (player_id, game_state) VALUES (%s, %s)", (player_id, state))
    conn.commit()
    cursor.close()
    conn.close()

def save_match(player1, player2, winner):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO matches (player1, player2, winner) VALUES (%s, %s, %s)",(player1, player2, winner))
    conn.commit()
    cursor.close()
    conn.close()

def load_latest_game(player_id):
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT game_state FROM saved_games WHERE player_id = %s ORDER BY id DESC LIMIT 1", (player_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None
