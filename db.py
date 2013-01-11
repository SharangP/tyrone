import sqlite3 as lite

class Database(object):
  def __init__(self, db_file):
    self.conn = lite.connect(db_file)
    self.cur = self.conn.cursor()
    with self.conn:
      self.cur.execute('CREATE TABLE links (id INTEGER NOT NULL, hash VARCHAR(10), PRIMARY KEY(id));')
      self.cur.execute('CREATE TABLE clicks (id INTEGER NOT NULL, l_id INTEGER NOT NULL, num INTEGER, time INTEGER, PRIMARY KEY(id), FOREIGN KEY(l_id) REFERENCES links(id));')
      self.cur.execute('CREATE TABLE categories (id INTEGER NOT NULL, name VARCHAR(100), PRIMARY KEY(id));')
      self.cur.execute('CREATE TABLE link_categories (id INTEGER NOT NULL, l_id INTEGER NOT NULL, c_id INTEGER NOT NULL, PRIMARY KEY(id), FOREIGN KEY(l_id) REFERENCES links(id), FOREIGN KEY(c_id) REFERENCES categories(id));')
      categories = ["advertising", "agriculture", "art", "automotive", "aviation", "banking", "business", "celebrity", "computer", "disasters", "drugs", "economics", "education", "energy", "entertainment", "fashion", "finance", "food", "games", "health", "hobbies", "humor", "intellectual property", "labor", "legal", "lgbt", "marriage", "military", "mobile devices", "news", "philosophy", "politics", "real estate", "reference", "science", "sexuality", "shopping", "social media", "sports", "technology", "travel", "weapons", "weather"]

      n = 1
      for category in categories:
        with self.conn:
          self.cur.execute('INSERT INTO categories VALUES(?,?)', (n, category))
        n = n + 1
