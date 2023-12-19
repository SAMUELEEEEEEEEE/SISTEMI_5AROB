import socket as sck

BUFSIZE = 4096
SERVER_ADDRESS = ("127.0.0.1", 8000)

def codifica(messaggio_chiaro, c, n):
    messaggio_criptato = ""
    for lettera in messaggio_chiaro:
        messaggio_criptato += f"{ord(lettera) ** c % n}-"
    return messaggio_criptato[:-1]

def main():
    client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

    client.connect(SERVER_ADDRESS)

    chiavi_pubbliche = client.recv(BUFSIZE).decode()

    n, c = int(chiavi_pubbliche.split("-")[0]), int(chiavi_pubbliche.split("-")[1])
    while True:
        messaggio_chiaro = input("Inserire il messaggio da inviare: ")
        messaggio_criptato = codifica(messaggio_chiaro, c, n)
        client.sendall(messaggio_criptato.encode())

        if messaggio_chiaro == "esci":
            break
    
    client.close()

if __name__ == "__main__":
    main()