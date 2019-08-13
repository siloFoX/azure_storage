from Cosmos_upload import  Cosmos_upload, load_json
from Blob_upload import Blob_upload


def record(name_list) :
    data = load_json()

    for idx, name in enumerate(name_list, 1) :
        for datum in data :
            datum["동영상" + str(idx)] = name

            print(idx, " : ", name)
            
    return data


def start() :
    name_list = Blob_upload()
    data = record(name_list)
    Cosmos_upload(data = data)


if __name__ == '__main__' :
    try :
        start()

    except Exception as e:
        print(e) 