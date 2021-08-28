import pip._vendor.requests as requests
import json
import time as t

while True:
    try:
        open("Valor Cardano.txt", 'x') #cria o arquivo de armazenamento
    except:
        print("") #caso ele ja exista, apenas faz nada
    r = requests.get("https://api.coingecko.com/api/v3/coins/cardano?localization=false&tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true")
    
    hora = t.localtime()
    dados = json.loads(r.text) #transforma as informações do site de um dicionario python para json
    valor = dados["market_data"]["current_price"]["brl"] 
    
    mensagem = "o valor de um cardano as "+ str(hora.tm_hour) +":"+str(hora.tm_min) +" do dia "+str(hora.tm_mday)+"/"+ str(hora.tm_mon)+"/"+ str(hora.tm_year) +" é de: R$ " + str(valor)
    
    print(mensagem)
    f = open("Valor Cardano.txt", "a")
    f.write("\n" + mensagem)

    t.sleep(300)
    continue
