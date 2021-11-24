import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def uploadFiles(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'Fon3fnuDRjwAAAAAAAAAAY414TA7EdryAgJyBl95tuNmss47B_O9MqAM_KMCQ35E'
    transferData = TransferData(access_token)
    file_from = input("Enter the file path which you want to transfer: ")
    file_to = input("Enter the file path to upload to dropbox: ")
    transferData.uploadFiles(file_from, file_to)
    print("File has been moved")
main()