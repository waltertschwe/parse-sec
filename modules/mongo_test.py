import pprint
from mongo import Mongo

## set db and collection
mongo = Mongo("sec_data", "test")

## get all data
mongo.findAll()

## insert one record 
mongo.stubRecord()
