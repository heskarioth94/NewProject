import os
import hashlib
import shutil
import stat
import threading
import time

# Funzione per calcolare l'hash di un file
def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Funzione per spostare il file nella cartella "Quarantena"
def move_to_quarantine(file_path, quarantine_folder):
    filename = os.path.basename(file_path)
    new_path = os.path.join(quarantine_folder, filename)
    shutil.move(file_path, new_path)
    print(f"Il file è stato messo in quarantena: {new_path}")
    os.chmod(quarantine_folder, 0o555)
    os.chmod(new_path, stat.S_IREAD | stat.S_IWRITE)

# Funzione per scansionare una cartella alla ricerca di file dannosi
def scan_folder(folder_path, malicious_hashes, quarantine_folder):
    found_suspicious_file = False
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if scan_file_for_virus(file_path, malicious_hashes):
                found_suspicious_file = True
                move_to_quarantine(file_path, quarantine_folder)
    return found_suspicious_file

# Funzione per la protezione in tempo reale
def real_time_protection(folder_path, malicious_hashes, quarantine_folder):
    print("Protezione in tempo reale attivata.")
    while True:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                if scan_file_for_virus(file_path, malicious_hashes):
                    move_to_quarantine(file_path, quarantine_folder)
                    print(f"File sospetto trovato: {file_path}")
        time.sleep(60)  # Scansiona ogni minuto

# Funzione per la scansione di un file alla ricerca di virus (da implementare)
def scan_file_for_virus(file_path, malicious_hashes):
    # Qui puoi implementare la logica di scansione antivirus del file
    # Utilizza l'hash del file per verificare se è sospetto
    file_hash = calculate_file_hash(file_path)
    return file_hash in malicious_hashes

if __name__ == "__main__":
    malicious_hashes = set([
        "aa9efb1b3f03f69951c6294ac44099dc89d62421cabd7a242a0dd01c0bc98757",
        # Aggiungere altri hash se necessario
    ])

    desktop_folder = os.path.join(os.path.expanduser("~"), "Desktop")
    quarantine_folder = os.path.join(desktop_folder, "Quarantena")

    os.makedirs(quarantine_folder, exist_ok=True)

    # Avvia la protezione in tempo reale in un thread separato
    real_time_thread = threading.Thread(target=real_time_protection, args=(desktop_folder, malicious_hashes, quarantine_folder))
    real_time_thread.daemon = True  # Termina il thread quando il programma termina
    real_time_thread.start()

    print("Scansione iniziale della cartella...")

    # Scansiona inizialmente la cartella e controlla se è stato trovato un file sospetto
    if scan_folder(desktop_folder, malicious_hashes, quarantine_folder):
        print("È stato trovato almeno un file sospetto.")
    else:
        print("Nessun file sospetto trovato.")
    while True:
        time.sleep=(60)

