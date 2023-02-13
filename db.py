import sqlite3

class Database:
    # In python, the init is similar to constructors in lets say Java. Self is like "this"
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS parts(id INTEGER PRIMARY KEY, part text, customer text retailer text, price text)")

        self.conn.commit()

        def fetch(self):
            self.cur.execute("SELECT * FROM parts")
            rows = self.cur.fetchall()
            return rows

        def insert(self, part, customer, retailer, price):
            self.cur.execue("INSERT INTO parts VALUES(NULL, ?, ?, ?, ?)", (part, customer, retailer, price)) 
            self.conn.commit()

        def remove(self, id):
            self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
            self.conn.commit()

        def update(self, id, part, customer, retailer, price):
            self.conn.execute("UPDATE parts SET part=?, customer=?, retailer=?, price=? WHERE id=?", (part, customer, retailer, price, id))
            self.conn.commit()

        def __del__(self):
            self.conn.close()   

db = Database('store.db')
db.insert("4GB DDR4 RAM", "Wa Kamau", "Kegisto", "$150")
db.insert("2GB SSD RAM", "Johnte Power", "Best Buy", "$90")
db.insert("24' LENOVO Monitor ", "5 Second of Fame", "Kegisto", "$250")
db.insert("NVDIA RTX 2020", "Power Play", "Newegg", "$500")