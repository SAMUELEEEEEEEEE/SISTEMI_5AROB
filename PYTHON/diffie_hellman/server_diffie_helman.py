import socket as sck
import random

BUFSIZE = 4096
SERVER_ADDRESS = ("127.0.0.1", 8000)

def main():
    N = 929
    g = random.randint(100, N)
    
    #N e g -> public keys

    server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)

    server.listen()

    connection, client_address = server.accept()

    connection.sendall(f"{N}-{g}".encode())

    a = random.randint(1, N ** N)
    print(f"Calcolato a : {g ** a % N}")
    connection.sendall(f"{g ** a % N}".encode())

    B = int(connection.recv(BUFSIZE).decode())
    print(f"Arrivato B : {B}")
    chiave_privata = B ** a % N

    print(chiave_privata)
    
    connection.close()
    server.close()

if __name__ == "__main__":
    main()