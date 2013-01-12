import bitly_api
import time
from db import Database

C = bitly_api.Connection(access_token='20dbd7d26d6f4d7c9c6d70b22236797b48a7b7af')
Links = {}
Clicks = {}
DB = Database('bitly1.db')

while True:
    hot = C.highvalue(limit=300)

    for link in hot['values']:
        key = link.split('bit.ly/')[1]
        if not Links.has_key(key):
            Links[key] = True
            print "new link!", key, Links[key]
            # insert (key) into LINKS table? we dont have one right now
            for category in C.link_category(link):
#                print '\t',category, DB.category_id(category)
                DB.add_category(key,DB.category_id(category))

    for key,lid in Links.iteritems():
        print key, lid
        Time = int(time.time())
#        print "THE LENGTH IS:", len(C.link_clicks('https://bit.ly/'+key)[0]['link_clicks'])
        clicks = C.clicks_by_minute(hash=key)[0]['clicks']
        print len(clicks)
        for i,clk in enumerate(clicks):#, C.info(link=link)[0]['title']
            print key, clk, Time-i
            DB.add_click(key,clk,Time-i)
            if i >= 29:
                break

    time.sleep(30*60) #repeat every 30 mins
