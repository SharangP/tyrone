import bitly_api
import time

C = bitly_api.Connection(access_token='61c2b3d767d10e5a58b62d0c7ee1bfa856ac69f8')

hotphrases = C.highvalue(limit=10000)
print 'BEGIN NEW SET OF PHRASES'
for link in hotphrases['values']:
  print C.clicks_by_day(shortUrl=link)[0]['clicks'], C.info(link=link)[0]['title']
