import json
import pickle
import itertools


class TipoEstabelecimento:
    def __init__(self):
        self.quantidade = 0
        self.rating = 0
    def __str__(self):
        return "%5i %0.2f" % (self.quantidade, self.rating)


tipos = ["accounting", "airport", "amusement_park", "aquarium", "art_gallery", "atm", "bakery", "bank", "bar", "beauty_salon", "bicycle_store", "book_store", "bowling_alley", "bus_station", "cafe", "campground", "car_dealer", "car_rental", "car_repair", "car_wash", "casino", "cemetery", "church", "city_hall", "clothing_store", "convenience_store", "courthouse", "dentist", "department_store", "doctor", "electrician", "electronics_store", "embassy", "establishment", "finance", "fire_station", "florist", "food", "funeral_home", "furniture_store", "gas_station", "general_contractor", "grocery_or_supermarket", "gym", "hair_care", "hardware_store", "health", "hindu_temple", "home_goods_store", "hospital", "insurance_agency", "jewelry_store", "laundry", "lawyer", "library", "liquor_store", "local_government_office", "locksmith", "lodging", "meal_delivery", "meal_takeaway", "mosque", "movie_rental", "movie_theater", "moving_company", "museum", "night_club", "painter", "park", "parking", "pet_store", "pharmacy", "physiotherapist", "place_of_worship", "plumber", "police", "post_office", "real_estate_agency", "restaurant", "roofing_contractor", "rv_park", "school", "shoe_store", "shopping_mall", "spa", "stadium", "storage", "store", "subway_station", "synagogue", "taxi_stand", "train_station", "travel_agency", "university", "veterinary_care", "zoo"]
geral = {}
for tipo in tipos:
    geral[tipo] = False

tabela = []

areas = ["areas/area_%i.json"%(i) for i in xrange(225)]

"""
for area in areas:
    linha = {}
    arquivo = open(area, "r")
    dados = json.load(arquivo)
    for tipo in tipos:
        linha[tipo] = TipoEstabelecimento()
    for req in dados:
        for estabelecimento in req['results']:
            for tipo in estabelecimento['types']:
                if tipo in tipos:
                    geral[tipo] = True
                    linha[tipo].quantidade += 1
                    if "rating" in estabelecimento.keys(): linha[tipo].rating += estabelecimento['rating']
    for tipo in tipos:
        if linha[tipo].quantidade: linha[tipo].rating = linha[tipo].rating / linha[tipo].quantidade
    tabela.append(linha)
"""


chaves = [set(chave) for chave in itertools.combinations(tipos, 4)]
tabela = {}
for i,area in enumerate(areas):
    print "Area:",i
    amostras = json.load(open(area))
    tipos_area = set()
    for amostra in amostras:
        for estab in amostra['results']:
            for tipo in estab['types']:
                if tipo in tipos:
                    tipos_area.add(tipo)
    
    for chave in chaves:
        if chave.issubset(tipos_area):
            #chave_norm = tuple(sorted(list(chave)))
            chave_norm = ".".join(sorted(list(chave)))
            tabela[chave_norm] = tabela.get(chave_norm, 0) + 1

pickle.dump(tabela, (open("tabela.pickle","wb")))
json.dump(tabela, open("tabela.json","wb"))

"""

titulo = "area"     
ds = "d"
for tipo in tipos:
    if geral[tipo]:
        titulo += "\t" + tipo
        ds += "\t" + "d"
print(titulo)
print(ds)
area = 1
for linha in tabela:
    l = str(area)
    for tipo in tipos:
        if geral[tipo]:
            l += "\t" + str(linha[tipo].quantidade)
    print(l)
    area += 1
"""