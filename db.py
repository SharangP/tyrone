import sqlite3 as lite

class Database(object):
  def __init__(self, db_file):
    self.conn = lite.connect(db_file)
    self.cur = self.conn.cursor()
    with self.conn:
      self.cur.execute('CREATE TABLE IF NOT EXISTS links (l_id INTEGER PRIMARY KEY, hash VARCHAR(10));')
      self.cur.execute('CREATE TABLE IF NOT EXISTS clicks (l_id INTEGER NOT NULL, num INTEGER, time INTEGER, PRIMARY KEY(l_id, time), FOREIGN KEY(l_id) REFERENCES links(l_id));')
      self.cur.execute('CREATE TABLE IF NOT EXISTS categories (c_id INTEGER PRIMARY KEY, name VARCHAR(100));')
      self.cur.execute('CREATE TABLE IF NOT EXISTS link_categories (l_id INTEGER NOT NULL, c_id INTEGER NOT NULL, PRIMARY KEY(l_id, c_id), FOREIGN KEY(l_id) REFERENCES links(l_id), FOREIGN KEY(c_id) REFERENCES categories(c_id));')
      self.categories = ["advertising", "agriculture", "art", "automotive", "aviation", "banking", "business", "celebrity", "computer", "disasters", "drugs", "economics", "education", "energy", "entertainment", "fashion", "finance", "food", "games", "health", "hobbies", "humor", "intellectual property", "labor", "legal", "lgbt", "marriage", "military", "mobile devices", "news", "philosophy", "politics", "real estate", "reference", "science", "sexuality", "shopping", "social media", "sports", "technology", "travel", "weapons", "weather", "none"]

      self.cur.execute('SELECT * FROM categories;')
      if len(self.cur.fetchall()) == 0:
        for category in self.categories:
          with self.conn:
            self.cur.execute('INSERT INTO categories(name) VALUES(?)', [category])

  def add_link(self, link_hash):
    with self.conn:
      self.cur.execute('INSERT INTO links(hash) VALUES(?)', [link_hash])

  def link_id(self, link_hash):
    with self.conn:
      self.cur.execute("SELECT * FROM links WHERE hash=?", [link_hash])
      all = self.cur.fetchall()
      return -1 if len(all) == 0 else all[0][0]

  def category_id(self, category):
    try:
      return self.categories.index(category)
    except ValueError, e:
      return self.categories.index("none")

  def categories(self):
    return self.categories
