import os.path as fileChecker
import xmlrpc.client
import os
import threading
import time


Connection_Proxy_ = xmlrpc.client.ServerProxy("http://localhost:8880/")


def write(filename,filecontent):

    Directory = curDir+'/'+filename
    print(Directory)
    file_tobedownloaded = open(Directory,"w")
    file_tobedownloaded.writelines(filecontent)
    return "File Downloaded Check Download folder"

def readFileClientSide():
    
    File_Loc_Path_ = input("enter file name with extension : ")
    File_Contents_ = list()
    File_Loc_Path_ = curDir + '/' + File_Loc_Path_
    if fileChecker.isfile(File_Loc_Path_):
        File_Contents_Wrapper_ = open(File_Loc_Path_,"r")
        File_name = File_Loc_Path_.split('/')[-1]
        for x in File_Contents_Wrapper_:
            File_Contents_.append(x)
        output = Connection_Proxy_.uploadToServer(File_Contents_,File_name)
        print("File Uploaded to the Server")

    else:
        print ("Upload Failed : File doesn't exist")
        
def downloadFileServerSide():
    
    File_Name_ = input("enter file name with extension : ")
    output_file_content = Connection_Proxy_.DownloadToClient(File_Name_)
    print("Receiving Data")
    for x in output_file_content:
        print(x)
    write(File_Name_,output_file_content)
    print("File Downloaded check ClientsDownloads Folder")
    
def delete():

    File_Name_ = input("enter file name with extension : ")
    output = Connection_Proxy_.DeleteOnServer(File_Name_)
    print(output)
 
def rename():

    old_file_name_ = input("enter old file name with extension: ")
    new_file_name_ = input("enter new file name with extension: ")
    output = Connection_Proxy_.RenameOnServer(old_file_name_,new_file_name_)
    print(output)
    
 
if __name__ == '__main__':

    curDir = os.path.dirname(os.path.realpath(__file__))
    newDir = os.path.join(curDir,"ClientsDownloads")
    if not os.path.exists(newDir):
        curDir = os.mkdir(newDir)
    else:
        curDir = os.path.join(curDir,"ClientsDownloads")

    Iteration = True


    print("Operations")
    print("1.Upload file to server")
    print("2.Download file from server")
    print("3.Delete file from server")
    print("4.Renaming file at server")
    print("5.Stop operation")
    while Iteration:
        service_number = int(input("Choose Operation from above"))
        if service_number == 1:
            t = threading.Thread(target = readFileClientSide)
            t.start()
            t.join()
        elif service_number == 2:
            t = threading.Thread(target = downloadFileServerSide)
            t.start()
            t.join()
        elif service_number == 3:
            t = threading.Thread(target = delete)
            t.start()
            t.join()
        elif service_number == 4:
            t = threading.Thread(target = rename)
            t.start()
            t.join()
        elif service_number == 5:
            Iteration = False
    
        
    
