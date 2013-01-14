import sqlite3 as lite

class Database(object):
  def __init__(self, db_file):
    self.conn = lite.connect(db_file)
    self.cur = self.conn.cursor()
    with self.conn:
      try:
        self.cur.execute('CREATE TABLE IF NOT EXISTS hvalues (hash VARCHAR(255), time INTEGER, PRIMARY KEY(hash, time));')
        self.cur.execute('CREATE TABLE IF NOT EXISTS phrases (phrase VARCHAR(255), visitors INTEGER, time INTEGER, PRIMARY KEY(phrase, time));')
        self.cur.execute('CREATE TABLE IF NOT EXISTS bursting_phrases (phrase VARCHAR(255), visitors INTEGER, time INTEGER, mean REAL, rate REAL, std REAM, PRIMARY KEY(phrase, time));')

      except Exception, err:
        print ('SQL BROKE: %s\n' % str(err))

  def high_phrase(self, hash_v, time):
    with self.conn:
      try:
        self.cur.execute('INSERT INTO hvalues VALUES(?,?)', [hash_v, int(time)])
      except Exception, err:
        print ('SQL BROKE: %s\n' % str(err))

  def hot_phrase(self, phrase, time, visitors):
    with self.conn:
      try:
        self.cur.execute('INSERT INTO phrases VALUES(?,?,?)', [phrase, visitors, int(time)])
      except Exception, err:
        print ('SQL BROKE: %s\n' % str(err))

  def bursting_phrase(self, phrase, time, visitors, mean, rate, std):
    with self.conn:
      try:
        self.cur.execute('INSERT INTO bursting_phrases VALUES(?,?,?,?,?,?)', [phrase, visitors, int(time), mean, rate, std])
      except Exception, err:
        print ('SQL BROKE: %s\n' % str(err))
