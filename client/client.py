import socket 
import json

BUFFER_SIZE = 1940


class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.client_socket.connect((host, port))
 
    def send_command(self, command, parameters):
        send_data = {'command': command, 'parameters': parameters}
        print("    The client sent data => {}".format(send_data))
        self.client_socket.send(json.dumps(send_data).encode())

    def wait_response(self):
        data = self.client_socket.recv(BUFFER_SIZE)
        raw_data = data.decode()
        print("    The client received data => {}".format(raw_data))

        return json.loads(raw_data)

if __name__ == '__main__':
    client = SocketClient(host, port)

    keep_going = True
    while keep_going:
        command = input(">>>")
        client.send_command(command)
        keep_going = client.wait_response() 
    