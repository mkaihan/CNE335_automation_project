import os

class Server:
    

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip
        self.ping()

    def ping(self):
        # TODO - Use os module to ping the server
        print("The Server IP is", self.server_ip)
        #Get the location from where the Python script is run
        filepath = os.path.dirname(os.path.abspath(__file__))
        #Set the working directory to the path where the python source code is
        os.chdir(filepath)        
        #pingresult = os.path.join(filepath,"pingResults__.txt")
        #Create a text file Name to store the Ping results
        pingresult = "pingResults__.txt"
        pingText = 'ping ' + (self.server_ip) + ' > ' + pingresult         
        print("Command sent to the OS system for the ping is: ", pingText)
        response = os.system(pingText) 
        #A response of 0 is returned for a sucessfull server response
        f = open(pingresult, "r")
        if (response == 0):            
            print("Ping Successfull for the server", self.server_ip)            
            print(f.read())
        else:
            print("Check the server - Unsuccessfull ping response for ", self.server_ip)
            print(f.read())
            
