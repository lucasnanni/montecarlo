# -- coding: utf-8 --

import urllib
import json
import random
import pickle

path = "areas/"

parametros = {
  "key" : "AIzaSyAw6JZsXlV79d9cqrNvjdAa4GRoqlIkP1o",
  "location" : "-23.410563,-51.943887",
  "radius" : "250",
  "sensor" : "false"
}

def persiste_resultado(dados, nome):
  arq = open(path+nome,"wb")
  json.dump(dados,arq,indent=2,encoding="utf-8")
  arq.close()
  
def persiste_amostras(amostras, nome):
  arq = open(path+nome,"wb")
  pickle.dump(amostras,arq)
  arq.close()

def obter_resultados(coordenada):
  parametros["location"] = "%6f,%6f"%coordenada
  url = "https://maps.googleapis.com/maps/api/place/search/json?"+urllib.urlencode(parametros)
  return json.load(urllib.urlopen(url))

areas = []
min_lati, max_lati = -23.481511, -23.372514
min_long, max_long = -52.014828, -51.872692
quadros = 15
passo_lati = (max_lati - min_lati)/quadros
passo_long = (max_long - min_long)/quadros

for i in xrange(quadros):
  for j in xrange(quadros):
    areas.append(
      [
        (min_lati + i*passo_lati, min_long + i*passo_long),
        (min_lati + (i+1)*passo_lati, min_long + (i+1)*passo_long)
      ]
    )

num_amostras = 10
amostras_areas = []

for area in areas:
  lati1,long1 = area[0]
  lati2,long2 = area[1]
  amostras = []
  for i in xrange(num_amostras):  
    latitude = random.uniform(lati1,lati2)
    longitude = random.uniform(long1,long2)
    amostras.append((latitude, longitude))
  amostras_areas.append(amostras)

for i,amostras_area in list(enumerate(amostras_areas))[:]: #[i:j) faixa das areas.
  dados = map(obter_resultados,amostras_area)
  persiste_resultado(dados,"area_%i.json"%(i))
