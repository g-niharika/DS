from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
import threading

# Define the computation server class
class ComputationServer:
    def add(self, i, j):
        return i + j

    def sort(self, A):
        return sorted(A)

    def async_add(self, i, j):
        # Use a separate thread to perform the computation
        result = self.add(i, j)
        return result

    def async_sort(self, A):
        # Use a separate thread to perform the computation
        result = self.sort(A)
        return result

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create the server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_instance(ComputationServer())

    # Start the server in a separate thread
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server started.")

    # Keep the server running until interrupted
    try:
        server_thread.join()
    except KeyboardInterrupt:
        print("Server stopped.")
