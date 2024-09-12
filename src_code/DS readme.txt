
# RPC File Server

This program is to implement a simple file upload and download service and a computation service using remote procedure call (RPC) based communication.
File server supports four basic operations: UPLOAD, DOWNLOAD, DELETE, and RENAME a file, add(i, j) and sort(array A) using synchronous, asynchronous RPCs.
In synchronous RPC, the client makes the RPC call and waits for the result from the server. In asynchronous RPC, the client makes the RPC call and waits for an acknowledgment from the server, and continues after receiving an acknowledgment.
On the other hand, after completing the computation the server sends the result of the call back to the client.

The file transfer between the client and the server made transparent to users and automatically handled by a helper thread. 
This creates a Dropbox-like synchronized storage service.
Whenever changes are made to the synchronized folder at the client side, e.g., creating a new file, updating a file, or deleting a file, the helper thread will establish a connection with the server and automatically send the corresponding operation to the server to update the folder at the server side.
We configured the helper thread to periodically check if there are changes made to the synchronized folder.
If the last update time to a file is later than the last check, the file will be synchronized. To simplify the design, we didn't consider incremental updates. Thus, if the content of a file is updated, the entire file should be sent to the server to overwrite the original copy at the server.



## Acknowledgements

This project is developed by Jagini Prathima(1002088570) and Niharika Gaddam(1002079425).

## Requirements
- python 3
- Notepad++
- Pip installing Python Libraries 

## Detailed Instructions to Execute Code
- Reload the Whole Project in the notepad++
- Compile using commands in the command prompt.
- Change the Server directory Folder Path in the command prompt using the command 
    >cd directory\foldername\filename
- Change the Client directory Folder Path in the command prompt using the command 
    >cd directory\foldername\filename
- To execute the client and server run “Python filename.py” command in the command prompt.
- ClientDownloads  (Client-Repo) and ServerUploads (Server-Repo)are created when we run the client and server python files automatically.
- For the 1st part, User is displayed with the below operations. They need to select the respective number  for desired operations
- For  2nd part, User  is displayed with all the activities that helper thread will done to synchronize client and server repos


# Commands
Directroryand commands are as following:
- For Upload :  Enter filename.extension
- For Rename : Enter Oldfilename.extension , Newfilename.extension
- For Download: Enter filename.extension
- For Delete : Enter filename.extension
- For Add: 0 Arguments by user
- For Sort: 0 Arguments by user

