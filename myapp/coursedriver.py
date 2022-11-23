from pymongo import MongoClient
from pyparsing import col
import dns
cluster = MongoClient("mongodb+srv://Gaurav27:gaurav@cluster0.h0kk1.gcp.mongodb.net/coursedetails?retryWrites=true&w=majority")
db = cluster.get_database('coursedetails')
collection = db.desc

def fetch_data():
    data = collection.find({})
    temp= {}
    for i in data:
        temp[i['course_name']] = i
    return temp 


def save_data(data):
    collection = db.user_record
    collection.insert_one(data)
    return "Done"
        
