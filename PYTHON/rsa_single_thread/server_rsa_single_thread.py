import math
import socket as sck

BUFSIZE = 4096
SERVER_ADDRESS = ("127.0.0.1", 8000)

#Funzioni per il funzionamento dell'algoritmo criptografico di rsa
def find_n(p, q):
    return p * q

def find_m(p, q):
    return math.lcm(p - 1, q - 1)

def find_c(m):
    found = False
    c = 2
    while found is False:
        if math.gcd(c, m) == 1:
            found = True
        else:
            c += 1
    return c

def find_d(c, m):
    found = False
    d = 1
    while found is False:
        if (c * d) % m == 1:
            found = True
        else:
            d += 1
    return d

def codifica(messaggio_chiaro, c, n):
    messaggio_criptato = ""
    for lettera in messaggio_chiaro:
        messaggio_criptato += f"{int(ord(lettera) ** c) % n}-"
    return messaggio_criptato[:-1]

def decodifica(messaggio_criptato, d, n):
    messaggio_chiaro = ""
    list_messaggio_criptato = messaggio_criptato.split("-")
    for numero in list_messaggio_criptato:
        print(numero)
        messaggio_chiaro += chr((int(numero) ** d) % n)
    return messaggio_chiaro

def main():
    p = 881
    q = 9029

    n = find_n(p, q)
    m = find_m(p, q)
    c = find_c(m)
    d = find_d(c, m)

    #n e c -> public keys
    #m e d -> private keys

    server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    server.bind(SERVER_ADDRESS)

    server.listen()

    connection, client_address = server.accept()

    connection.sendall(f"{n}-{c}".encode())

    while True:
        messaggio_criptato = connection.recv(BUFSIZE).decode()
        messaggio_chiaro = decodifica(messaggio_criptato, d, n)
        
        if messaggio_chiaro == "esci":
            break

        print(messaggio_chiaro)
    
    connection.close()
    server.close()

if __name__ == "__main__":
    main()