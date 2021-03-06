from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in file_list:
    print(file['title'])
    file.Trash()
