from pymongo import MongoClient

def insert_to_db(json_object):
    client = MongoClient()
    db = client.publications
    
    db.table.insert_one(json_object)

def does_exist(id):
    client = MongoClient()
    db = client.publications

    if db.table.find({'_id':id}).count() == 0:
        return False
    else:
        return True

def retrieve_fig_by_uri(uri):
    client = MongoClient()
    db = client.publications

    cursor = db.table.find({'uri':id})

    return cursor


def retrieve_from_db(id):
    client = MongoClient()
    db = client.publications

    cursor = db.table.find({'_id':id})

    return cursor

if __name__=="__main__":
    print('In QueryAndLoadMongo')
