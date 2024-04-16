import pyaudio
import socket

# Definir constantes
TAMANHO_CHUNK = 1024
FORMATO = pyaudio.paInt16
CANAIS = 8
TAXA = 44100
IP_SERVER = '192.168.100.107'  # Altere isso para o endereço IP do seu servidor
PORTA = 12345  # Escolha um número de porta

audio = pyaudio.PyAudio()

# Use Para mostrar os dispositivo para transmissão
# for i in range(audio.get_device_count()):
#     device_info = audio.get_device_info_by_index(i)
#     print(device_info['index'], device_info['name'])

index_device =  0  # Por exemplo, 0 para o primeiro dispositivo listado

# Abrir um fluxo com o dispositivo de entrada desejado
flux_audio = audio.open(
   format=FORMATO,
   channels=CANAIS,
   rate=TAXA, 
   input=True,
   frames_per_buffer=TAMANHO_CHUNK,
   input_device_index=index_device)


audio = pyaudio.PyAudio()

SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

SERVER_LOCATION = (IP_SERVER, PORT)

print("Transmissão iniciada...")

try:
    while True:
        #Ler os dados de aúdio
        data = flux_audio.read(TAMANHO_CHUNK)
        
        #Enviar os dados de aúdio
        soquete.sendto(dados, SERVER_LOCATION)
finally:
    # Limpar recursos
    flux_audio.stop_stream()
    flux_audio.close()
    audio.terminate()
    SOCKET.close()
