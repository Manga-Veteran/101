import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

    def main():
        access_token = 'sl.BF2Kipkwr5V6DNFb3cxdpzUBMCt0yJftgCht1ehMTjB3vpI3rrqwcBc6gb3QehAn2F7_V18Ck34joFgHEegFqaMLQ0qPEalHFWEDqG6WEjPL4BsuLooovPBrIkAu3VcdNHGMNik'
        transferData = TransferData(access_token)
        file_from = input("enter the full path to transfer: ")
        file_to = input("enter the full path to upload to the dropbox: ")
        transferData.upload_file(file_from, file_to)
        print("file has been moved !!!")