import socket as sck
import random

BUFSIZE = 4096
SERVER_ADDRESS = ("127.0.0.1", 8000)

def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    client.connect(SERVER_ADDRESS)

    chiavi_pubbliche = client.recv(BUFSIZE).decode()

    N, g = int(chiavi_pubbliche.split("-")[0]), int(chiavi_pubbliche.split("-")[1])
    print("Arrivate N, g")
    A = int(client.recv(BUFSIZE).decode())
    print(f"Arrivato A : {A}")
    b = random.randint(1, N ** N)

    client.sendall(f"{g ** b % N}".encode())
    print("Inviato B")
    chiave_privata = A ** b % N

    print(chiave_privata)
    
    client.close()

if __name__ == "__main__":
    main()