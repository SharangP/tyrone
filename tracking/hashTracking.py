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
        T = int(time.time())
        high = C.highvalue(limit=100)
        hot = C.realtime_hot_phrases()
        bursting = C.realtime_bursting_phrases()

        print 'new'
        for V in high['values']:
            HighPhrases[V] = True
            DB.high_phrase(V.split('bit.ly/')[1],T)
            print V, T

        for P in hot:
            phrase = P['phrase']
            HotPhrases[phrase] = sum(map(lambda x:x['visitors'],P['ghashes']))
            DB.hot_phrase(phrase,T,HotPhrases[phrase])
            print phrase, T, HotPhrases[phrase]

        for P in bursting:
            phrase = P['phrase']
            BurstingPhrases[phrase] = sum(map(lambda x:x['visitors'],P['ghashes']))
            DB.bursting_phrase(phrase,T,BurstingPhrases[phrase],P['mean'],P['rate'],P['std'])
            print phrase, T, BurstingPhrases[phrase], P['mean'], P['rate'], P['std']

        errors = 0

        sleep_time = T - int(time.time()) + 5*60 
        print 'SLEEPING FOR ', sleep_time
        time.sleep(sleep_time) #repeat every 5 mins

    except Exception,er:
        errors += 1
        print '####################'
        print str(er)
        if errors > 10:
            break
