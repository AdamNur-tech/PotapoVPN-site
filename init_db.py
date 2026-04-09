import sqlite3

conn = sqlite3.connect("vpn.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    link TEXT,
    device TEXT,
    used INTEGER
)
""")

cur.execute("INSERT INTO links (link, device, used) VALUES ('vless://test_android', 'android', 0)")
cur.execute("INSERT INTO links (link, device, used) VALUES ('vless://test_ios', 'ios', 0)")

conn.commit()
conn.close()