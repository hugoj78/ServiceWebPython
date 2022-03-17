from typing import Optional

from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/museum")
def read_museum():
	r = requests.get('https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&q=&facet=date_start&facet=date_end&facet=address_name&facet=address_zipcode&facet=address_city&facet=deaf&facet=price_type&facet=access_type&facet=updated_at&facet=programs')
	return r.json()

@app.get("/museum/{museum_id}")
def read_museum_by_id(museum_id: str):
	r = requests.get(f'https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&q=&facet=date_start&facet=date_end&facet=address_name&facet=address_zipcode&facet=address_city&facet=deaf&facet=price_type&facet=access_type&facet=updated_at&facet=programs&refine.recordid={museum_id}')
	return r.json()

value = {
	"DonneBouchon" : "Data",
	"isYouAreBeautiful" : True
}

@app.get("/bouchon/{id}")
def read_item(id: str):
	if id == "michel":
		return value
	else :
		return {"no Json"}

@app.get("/museum/position/{lon}/{lat}/{dist}")
def read_museum_by_position(lon: str, lat: str, dist: str):
	r = requests.get(f'https://opendata.paris.fr/api/records/1.0/search/?dataset=que-faire-a-paris-&q=&facet=date_start&facet=date_end&facet=tags&facet=address_name&facet=address_zipcode&facet=address_city&facet=pmr&facet=blind&facet=deaf&facet=transport&facet=price_type&facet=access_type&facet=updated_at&facet=programs&geofilter.distance={lon},{lat},{dist}')
	return r.json()





from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb://admin:admin@clusterynov-shard-00-00.pipqs.mongodb.net:27017,clusterynov-shard-00-01.pipqs.mongodb.net:27017,clusterynov-shard-00-02.pipqs.mongodb.net:27017/ServiceWeb?ssl=true&replicaSet=atlas-fekj21-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.ServiceWeb
col = db.Data
# Issue the serverStatus command and print the results
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)

lists = col.find()
print(lists)

for doc in lists:
	print(doc)