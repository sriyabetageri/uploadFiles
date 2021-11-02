from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)

def main():
    access_token="sl.A61f27e98o5NgYlzkJGQk1qKZmxrS7Xas5yPZRwPPW5A_NmAOOq0hQ0h9wreALbfZeH-9RycsH8lO2e-gQ_DkJ2OLOzIDS61kGgD5oUCfq5Hv0li-xq2BF757Z6jtMORqjAp6Qo"
    transferData=TransferData(access_token)

    file_from = input("enter the file/path to transfer: ")
    file_to = input("enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File has been moved")
   
main()