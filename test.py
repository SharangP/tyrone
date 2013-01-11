from db import Database
from random import random, choice
import string

def rstring(N):
  return ''.join(choice(string.ascii_uppercase + string.digits) for x in range(N))

db = Database('test.db')
cats = db.categories

for i in range(1,100):
  h = rstring(7)
  print ('Entering %s' % h)
  for j in range(int(random() * 4)):
    cat = int(random() * len(cats))
    db.add_category(h, cat)
    print i, j, ('adding cat %s' % cat)

  for j in range(int(random() * 200)):
    click = int(random() * 200)
    db.add_click(h, click, j)
    print i, j, ('adding click %s' % click)
