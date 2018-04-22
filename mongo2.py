from pymongo import MongoClient
client = MongoClient(port=27017)
db=client.temp

db.users4.insert({'username':'test1@gmail.com','password':'passwd1'})
db.users4.insert({'username':'test2@gmail.com','password':'passwd2'})
db.users4.insert({'username':'test3@gmail.com','password':'passwd3'})
db.users4.insert({'username':'test4@gmail.com','password':'passwd4'})
db.users4.insert({'username':'test5@gmail.com','password':'passwd5'})

#printing
username=db.users4.find_one({'username':'t'})
print(username)