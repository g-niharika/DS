import os.path as fileChecker
import xmlrpc.client
import os
import threading
import time

class synchronizationHelper:
    def __init__(self, folder_path, server_hostport):
        self.folder_path = folder_path
        self.server_url = server_hostport
        self.last_check = 0

    def helperCheckRun(self):
    
        Clientfolder = os.listdir(self.folder_path+'\Client\ClientsDownloads')
        Serverfolder = os.listdir(self.folder_path+'\Server\ServerUploads')
        # Uploading files of client side to server side
        File_Contents_ = list()
        for filename in Clientfolder:
            if filename not in Serverfolder:
                Path = self.folder_path+'\Client\ClientsDownloads\\'+filename
                File_Contents_Wrapper_ = open(Path,"r")
                for x in File_Contents_Wrapper_:
                    File_Contents_.append(x)
                print(filename,end=" ")
                print(Connection_Proxy_.uploadToServer(File_Contents_,filename))
       
        #Deleting files of server side which are not present at client side  
        for filename in Serverfolder:
            if filename not in Clientfolder:
                    print(filename,end=" ")
                    print(Connection_Proxy_.DeleteOnServer(filename))
                        
 
        for filename in Clientfolder:
            file_path = self.folder_path+'\Client\ClientsDownloads\\' +filename
            file_content=list()
            if os.path.isfile(file_path):
                modification_time = os.path.getmtime(file_path)
                if modification_time > self.last_check:
                    file_n = open(file_path, 'r')
                    for x in file_n:
                        file_content.append(x)
                    Connection_Proxy_.uploadToServer(file_content,filename)
                  
        print("All the files date and contents are modified")
        self.last_check = time.time()
        time.sleep(50)  # adjust the frequency of the check here

if __name__ == '__main__':
    
    ###Helper Thread
    
    Connection_Proxy_ = xmlrpc.client.ServerProxy("http://localhost:8880/")
    client_sub_folder = os.path.dirname(os.path.realpath(__file__))
    helper = synchronizationHelper(client_sub_folder, 'http://localhost:8880/')
    helper.helperCheckRun()



