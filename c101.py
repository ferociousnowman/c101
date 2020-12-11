import dropbox 
class Transferdata:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def uploadfiles(self,filefrom, fileto):
        dbx=dropbox.Dropbox(self.accesstoken)

        f=open(filefrom,"rb")
        dbx.files_upload(f.read(),fileto),

def main():
    accesstoken="sl.AnOblfF22NBHObJ3zzKBnEJK1RvNP9ssBDgI8y9aNujbRx2dr6oxsLml2SOi18bdRgEhGGs4krfs0JQk8OKkG3sekbwbX2BllNY4Whl8sCrh_-bGPr06pl3ck-0_C44souP7sQw"
    transferdata=Transferdata(accesstoken)
    filefrom=input(" enter the file path to transfer")
    fileto=input("enter the full path to upload to dropbox ")
    transferdata.uploadfiles(filefrom,fileto)
    print("file has benn moved ")

main()