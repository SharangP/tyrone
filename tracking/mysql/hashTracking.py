import bitly_api
import os
import time
from db import Database


log = open('cronerrors.log','w')
C = bitly_api.Connection(access_token='61c2b3d767d10e5a58b62d0c7ee1bfa856ac69f8')
DB = Database()

HighPhrases = {}
HotPhrases = {}
BurstingPhrases = {}

while True:
    try:
        Time = time.time()
        T = int(Time)
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

        time.sleep(5*60-(time.time()-Time))

    except Exception,er:
        print str(er)
        log.write(str(er) + "\n")
        os.system('echo "ERRORRRRRRRRRRRRRR ' + str(er) + '" | espeak')
