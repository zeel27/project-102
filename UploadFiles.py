import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Bc5eXCeA9RIK1InwxAWpnMjZTV5RJEGl67fg_YuxZMIma8iyEoKanfyuFVxpccMb48ZwPuyx2QRTUhNVqB_DyIoUqqDLeKmC-EYg1biylmOI0x25eJi2e8pzeIkyB0FvdElDSkjYC3UO'
    transferData = TransferData(access_token)

    file_from = "C:/Users/Admin/Desktop/tasks.txt"
    file_to = "/project_folder/p102"

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
