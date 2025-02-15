from server import server

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    #The server.Server("34.209.138.165") in this case EC2 IP is 34.209.138.165
    #The IP address is passed as a string to the Server class in the server.py module     
    ec2Server = server.Server("34.209.138.165")    
    my_server_ip = "34.209.138.165"
    my_rsa_key_file = r"C:\Users\mosawark\.ssh\messi"
    username = "ubuntu"
    my_upgrade_command = 'sudo apt update && sudo apt upgrade -y'
    my_server = Server(my_server_ip, my_rsa_key_file, username, my_upgrade_command)
    print(my_server.ping())
    print("Updating server")
    ssh_result = my_server.upgrade()
    print(''.join(ssh_result))
