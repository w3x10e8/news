from pymongo import MongoClient
import requests
import json

client = MongoClient(port=27017)
db=client.temp


''' 
	Sample Data
		{
  "by" : "relate",
  "descendants" : 3,
  "id" : 16801470,
  "kids" : [ 16816533, 16816244, 16816366 ],
  "score" : 25,
  "time" : 1523369358,
  "title" : "Generative Adversarial Networks for Extreme Learned Image Compression",
  "type" : "story",
  "url" : "https://data.vision.ee.ethz.ch/aeirikur/extremecompression/"
		}

'''

db.news1.remove({})


ids=requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
ids=json.loads(ids.text)
for i in ids:
	data=requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(i)+'.json?print=pretty')
	data=json.loads(data.text)
	try:
		db.news1.insert({'by':data['by'],'h_id':data['id'],'title':data['title'],'url':data['url'],'by':data['by'],'type':data['type']})
	except:
		print("[+] Skipped")
	print(data['title'])