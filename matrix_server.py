import unicornhathd
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
        print("Waiting for new client...")
        self.sock, self.addr = self.server_sock.accept()
        print("Client connected from", self.addr, ".")

    def read_pixel(self):
        try:
            data = tuple(self.sock.recv(5))

            if len(data) == 0:
                raise socket.error()

            return data

        except socket.error:
            print("Error communicating with client. Disconnecting.")
            self.sock.close()
            self.sock.shutdown(2)
            self.wait_for_client()
            return None


unicornhathd.rotation(0)
unicornhathd.brightness(0.6)
u_width, u_height = unicornhathd.get_shape()
client = Client("", 28891)

running = True
while running:
    pixel = client.read_pixel()

    if pixel[0] == 255:
        unicornhathd.show()
    else:
        unicornhathd.set_pixel(*pixel)

unicornhathd.show()
