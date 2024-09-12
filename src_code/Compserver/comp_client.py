import xmlrpc.client

# Connect to the server
with xmlrpc.client.ServerProxy("http://localhost:8000/RPC2") as proxy:
    # Call the synchronous methods
    print("output of synchronous")
    print("---------------------")
    print(proxy.add(2, 3))      
    print(proxy.sort([9,2,1,3,4])) 
    print("---------------------")

    # Call the asynchronous methods
    _async_add_res = proxy.async_add(4, 6)
    _async_sort_res = proxy.async_sort([5,6,8,1,0,2])


    # Print the results
    print("Output of asynchronous")
    print("----------------------")
    print("async_add result:",_async_add_res)  
    print("async_sort result:",_async_sort_res)  
