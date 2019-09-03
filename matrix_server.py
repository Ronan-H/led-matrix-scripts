import socket


class Client:
    def __init__(self, host, port):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind((host, port))
        self.server_sock.listen()
        self.sock = None
        self.addr = None
        self.wait_for_client()

    def wait_for_client(self):
        self.sock, self.addr = self.server_sock.accept()

    def read_line(self):
        text = ""
        try:
            while True:
                data = str(self.sock.recv(1))
                data = data[2:-1]
                print("data: " + data)
                print("len(data): " + str(len(data)))

                if data == "\\r":
                    print("\\r found; breaking...")
                    # consume the following \n character
                    self.sock.recv(1)
                    break

                text += data
        except socket.error:
            self.wait_for_client()
            return None

        return text


client = Client("127.0.0.1", 28891)

running = True
while running:
    line = client.read_line()
    parts = line.split(":")
    operationId = int(parts[0])
    inputs = parts[1].split(",")

    if operationId == 0:
        pass
