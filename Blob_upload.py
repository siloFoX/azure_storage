from azure.storage.blob import BlockBlobService, PublicAccess
import time
import os


PATH = 'Blob_data'


def Blob_upload(path = PATH) :
    account_name = 'mailsys'
    account_key = 'Ql9zTFbmOolovYH7wnVCKqzSV9aQg3owEKviAXCANK1RiRmSp++kWy5HbReqsSPMZv4M8EUtKUGGuwvCubHn6w=='
    container_name = 'surgerydata'

    # Create the BlockBlockService that is used to call the Blob service for the storage account.
    service = BlockBlobService(account_name = account_name, account_key = account_key)

    # Create a container called 'surgerydata'.
    if not service.exists(container_name) :
        print("create container : ", container_name)
        service.create_container(container_name)

    else :
        print("container name : " + container_name)
 
    print("accounnt : " + account_name)
    
    # Set the permission so the blobs are public.
    service.set_container_acl(container_name, public_access = PublicAccess.Container)

    # get data path and list
    abs_path = os.path.join(os.getcwd(), path)
    list_video = os.listdir(abs_path)

    for name in list_video :
        path_tmp = os.path.join(abs_path, name)

        print("Temp file : " + path_tmp)
        print("\nUploading to Blob storage as blob : " + name)
        print("\nUploading...\n")

        start_time = time.time()

        service.create_blob_from_path(container_name, name, path_tmp)
        
        print("Upload complete!!")
        print("Time taken {} sec" .format(time.time() - start_time))

        os.remove(path_tmp)

    return list_video


def start_Blob_upload() :
    try :
        list_video = Blob_upload()
    
    except Exception as e:
        print(e)

    return list_video


if __name__ == '__main__' :
    start_Blob_upload()