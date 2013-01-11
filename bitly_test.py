import bitly_api
import time

C = bitly_api.Connection(access_token='61c2b3d767d10e5a58b62d0c7ee1bfa856ac69f8')
Links = {}
# Categories = db.getCategories() # get the category mapping table

linkId = 1
# linkId = db.maxId()# get the max id from the db if running this again

while True:
    hot = C.highvalue(limit=100)
    for link in hot['values']:
        key = link.split('bit.ly/')[1]
        if not Links.has_key(key):
            Links[key] = linkId
            print "new link!", key, Links[key]
            # insert (linkId,key) into LINKS table
            for category in C.link_category(link):
                print '\t',category
                # insert (linkId,catID) into CATEGORIES table
            linkId += 1
#        print C.clicks_by_day(shortUrl=link)[0]['clicks'], C.info(link=link)[0]['title']
    time.sleep(10) #repeat every 30 mins
