import os 
import os.path as fileChecker
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client

def uploadToServer(filecontent,filename):
    

    Directory = str()
    Directory = newDir+'/'+filename
    if fileChecker.isfile(Directory):
        file_tobeuploaded = open(Directory,"w")   
        file_tobeuploaded.writelines(filecontent)
    return "File Successfully Uploaded to Server" 
    else:
    return "File Doesn't Exist"
    
def DownloadToClient(filename):
    
    Directory = curDir+'/'+filename
    output_file_content = str()
    if fileChecker.isfile(Directory):
        File_Contents_Wrapper_ = open(Directory,"r")
        content = File_Contents_Wrapper_.readlines()
        return content
    else:
        return "File Doesn't Exist"
        
        
def DeleteOnServer(filename):

    Directory = curDir+'/'+filename
    if fileChecker.isfile(Directory):
        os.remove(Directory)
        return "File Deleted Successfully on SeverSide"
    else:
        return "File Doesn't exist"
     
def RenameOnServer(old_filename,new_filename):
 
    Directory = curDir+'/'+old_filename
    if fileChecker.isfile(Directory):
        old_filename = curDir + '/'+old_filename
        new_filename = curDir + '/'+new_filename
        os.rename(old_filename,new_filename)
        return "File Renamed Successfully on SeverSide"
    else:
        return "File Doesn't Exist"
    
curDir = os.path.dirname(os.path.realpath(__file__))
newDir = os.path.join(curDir,"ServerUploads")

if not os.path.exists(newDir):
    curDir = os.mkdir(newDir)

else:

    curDir = os.path.join(curDir,"ServerUploads")

        
Server_Connection_ = SimpleXMLRPCServer(("localhost",8880))
print("Server is listening on port 8880....")
Server_Connection_.register_function(uploadToServer,"uploadToServer")
Server_Connection_.register_function(DownloadToClient,"DownloadToClient")
Server_Connection_.register_function(DeleteOnServer,"DeleteOnServer")
Server_Connection_.register_function(RenameOnServer,"RenameOnServer")

Server_Connection_.serve_forever()
### need to close the server connection after some time



