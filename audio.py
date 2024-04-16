import pyaudio
import socket

# Definir constantes
FRAMES = 1024
FORMAT = pyaudio.paInt32
CHANNELS = 8
RATE = 44100
PORT = 12345  # Certifique-se de que isso corresponda ao número da porta usado no script transmissor

# Inicializar PyAudio
audio = pyaudio.PyAudio()

# Abrir um fluxo de saída
flux_audio = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, output=True, frames_per_buffer=FRAMES)

# Criar um socket UDP
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket à porta
SERVER_LOCATION = ('', PORT)
SOCKET.bind(SERVER_LOCATION)

print("Ouvindo áudio recebido...")

try:
    while True:
        # Receber dados de áudio
        data, location = SOCKET.recvfrom(65536)  
        
        # Reproduzir os dados de áudio
        flux_audio.write(location)
finally:
    # Limpar recursos
    flux_audio.stop_stream()
    flux_audio.close()
    audio.terminate()
    SOCKET.close()
