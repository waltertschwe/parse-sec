from pymongo import MongoClient
from datetime import datetime

class Mongo():

	def __init__(self, db, collection):
		self.client = MongoClient()	
		self.db = getattr(self.client, db)
		self.collection = getattr(self.db, collection)
		
	def findAll(self):
		cursor = self.collection.find()
		for document in cursor:
			print(document)

	def stubRecord(self):
		post = { "foo": "bar sec data",
	       "date": datetime.utcnow()
	    }

		post_id = self.collection.insert_one(post)
	    #print(post_id)

##db = client.sec_data

## access collection objects
##coll = db.dataset

##result = db.sec_data.insert_one( { "foo" : "bar" } )
##id = result.inserted_id

##cursor = db.sec.find()
##print( id )

##print(cursor)
