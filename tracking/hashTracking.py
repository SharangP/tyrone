import bitly_api
import time
from db import Database

C = bitly_api.Connection(access_token='61c2b3d767d10e5a58b62d0c7ee1bfa856ac69f8')
DB = Database('tracking.db')

HighPhrases = {}
HotPhrases = {}
BurstingPhrases = {}
errors = 0

while True:
    try:
        high = C.highvalue(limit=100)
        hot = C.realtime_hot_phrases()
        bursting = C.realtime_bursting_phrases()

        print 'new'
        for V in high['values']:
            HighPhrases[V] = True
            DB.high_phrase(V.split('bit.ly/')[1],time.time())
            print V, time.time()

        for P in hot:
            phrase = P['phrase']
            HotPhrases[phrase] = sum(map(lambda x:x['visitors'],P['ghashes']))
            DB.hot_phrase(phrase,time.time(),HotPhrases[phrase])
            print phrase, time.time(), HotPhrases[phrase]

        for P in bursting:
            phrase = P['phrase']
            BurstingPhrases[phrase] = sum(map(lambda x:x['visitors'],P['ghashes']))
            DB.bursting_phrase(phrase,time.time(),BurstingPhrases[phrase],P['mean'],P['rate'],P['std'])
            print phrase, time.time(), BurstingPhrases[phrase], P['mean'], P['rate'], P['std']

        errors = 0

        time.sleep(5*60) #repeat every 5 mins

    except Exception,er:
        errors += 1
        print '####################'
        print str(er)
        if errors > 10:
            break
