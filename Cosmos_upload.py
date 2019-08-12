from pymongo import MongoClient
import json
import os


JSON_PATH = 'Json_data'
DB_NAME = 'surgerydata'
COLLECTION_NAME = 'test_server'


def Cosmos_upload(data, db_name = DB_NAME, collection_name = COLLECTION_NAME, mode = 'insert') :
    server_path = "mongodb://mail:4HwIbdqzrEqqn0v2NdZXwbwJ8Oc7uKNaitgOr2VJ2CElpsi7MlIezIUdDbBiSpSLvSEtCtFkBvULEOSglcHKMQ==@mail.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    account_name = 'mail'
    account_key = '4HwIbdqzrEqqn0v2NdZXwbwJ8Oc7uKNaitgOr2VJ2CElpsi7MlIezIUdDbBiSpSLvSEtCtFkBvULEOSglcHKMQ=='
    
    client = MongoClient(server_path)
    
    db = client.get_database(name = db_name)
    db.authenticate(name = account_name, password = account_key)

    collection = db.get_collection(name = collection_name)
    
    if mode is 'insert' :
        for datum in data :
            collection.insert(datum)

    elif mode is 'update' :
        pass

    elif mode is 'remove' :
        pass


def load_json(path = JSON_PATH) :
    file_list = os.listdir(path)
    data = []

    for file in file_list :
        path = os.path.join(path, file)
    
        with open(path, encoding = 'UTF8') as data_file :
            data.append(json.load(data_file))
            
            print("{} is stored" .format(path))

        os.remove(path)

    return data

def start_Json_upload() :
    try :
        Cosmos_upload(data = load_json())

    except Exception as e:
        print(e)    


if __name__ == '__main__' :
    start_Json_upload()