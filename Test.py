import oauth2
import json
import pprint
#import twitter

consumer_key = 'IuUJv3OQyFQZjYje9Wme3XufZ'
consumer_secret = 'udy8JTINKPOoSTw55wN5EooSGW9RvNh24cUKB1krPmqCtmbGoe'

token_key = '1096953583478673408-j9Qk6xY85BVAbd9vIIoqMqiLwnuXE3'
token_secret = 'YQ9NKvM3RI7SbspMt6NdLL7NJpa8ujZEnQJyX4Su0aixu'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)

client = oauth2.Client(consumer, token)

#requisicao = client.request('https://api.twitter.com/1.1/search/tweets.json?q=geocode=-7.255572,-39.360915,20km')#&lang=pt&result_type=recent')
requisicao = client.request('https://api.twitter.com/1.1/search/tweets.json?q=geocode=-23.550520,-46.637429,20km')

decodificar = requisicao[1].decode()

objeto = json.loads(decodificar)

#for i in range (0,9999999999,1):
pprint.pprint(objeto) #['statuses'][i]['user']['screen_name'])
    #pprint.pprint(objeto['statuses'][i]['text'])
