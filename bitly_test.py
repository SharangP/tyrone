import bitly_api
import time

C = bitly_api.Connection(access_token='20dbd7d26d6f4d7c9c6d70b22236797b48a7b7af')

while True:
    hotphrases = C.realtime_hot_phrases()
    print 'BEGIN NEW SET OF PHRASES'
    for phrase in hotphrases:
        print 'START'
        print phrase#, C.realtime_clickrate(phrase)
        print 'END'
    time.sleep(2)
