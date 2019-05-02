import oauth2
import json
import pprint
import time
#declaração das keys
consumer_key = 'IuUJv3OQyFQZjYje9Wme3XufZ'
consumer_secret = 'udy8JTINKPOoSTw55wN5EooSGW9RvNh24cUKB1krPmqCtmbGoe'
token_key = '1096953583478673408-j9Qk6xY85BVAbd9vIIoqMqiLwnuXE3'
token_secret = 'YQ9NKvM3RI7SbspMt6NdLL7NJpa8ujZEnQJyX4Su0aixu'

#Essa função pega os dados codificado, decodifica e salva os dados no diretorio informado por parametro
def salvar_arquivo(dir, dados):
    file = open(dir, 'w')
    file.write(json.dumps(dados))
    file.close()

#Essa função reforna o json decodificado do arquivo informado por parametro
def abrir_arquivo(dir):
    file = open(dir, 'r')
    return json.loads(file.readlines())

def intersecao(a1, a2):
    total = 0
    for i in a1:
        if i in a2:
            total += 1
    return total

#Autenticando na API
consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
client = oauth2.Client(consumer, token)

#Creio que um intervalo de 1 minuto deve ser suficiente. Pode ser que alguns twites não venham, já que ele só busca 15 por vez. Talvez se achar um meio de expandir a busca seja melhor


tempo = 25 #segundos
atual = []
while True:
    #Fazendo a busca na API
    requisicao = client.request('https://api.twitter.com/1.1/search/tweets.json?q=juazeiro-do-norte')
    decodificar = requisicao[1].decode()
    objeto = json.loads(decodificar)
    """
        Essas duas linhas seguintes fazem parte da análise de sobreposição.
        Se essa análise chegar a Zero, significa que nenhum arquivo foi sobreposto e é possível que alguns twits não
        tenham sido salvos devido um tempo alto entre dois loops. Altomaticamente ele vai corrigir o tempo.
    """
    anterior = atual
    atual = []
    #objeto['statuses'] é um array, então basta:
    for i in range (0, len(objeto['statuses']), 1):        
        #Caso precise mudar o título do arquivo, mude na variável abaixo ou a análise de sobreposição não vai funcionar
        #Este não é um bom titulo, pois quando o mesmo usuário postar novamente, será sobreposto nos arquivos
        titulo_do_arquivo = objeto['statuses'][i]['user']['screen_name']
        atual.append(titulo_do_arquivo)
        
        #Salvará objeto['statuses'][i] com o nome screen_home na pasta "teste" (a pasta deve ser criada antes) e com extensão .json
        salvar_arquivo('teste/'+titulo_do_arquivo+'.json', objeto['statuses'][i])

    print(intersecao(anterior, atual),' twits repetidos')
    if intersecao(anterior, atual)>5:
        tempo += 5
        print("Tempo incrementado em 5 segundos")
    elif intersecao(anterior, atual) == 0:
        tempo -= 10
        print("Tempo decrementado em 10 segundos")
    time.sleep(tempo)
