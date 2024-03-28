import os
import pygame
import pyaudio
import time
import serial
import numpy as np
import matplotlib.pyplot as plt
import struct


time.sleep(1)

CHUNK = 4096 # número de pontos lidos em tempo real
RATE = 44100 # resolução de tempo do dispositivo de gravação (Hz)


def fft_mode_song(serialPort='COM9'):
    arduino = None
    try:
        arduino = serial.Serial(serialPort, 115200, timeout=.1)
    
        np.set_printoptions(suppress=True) # Não usa notaçao cietífica

        p=pyaudio.PyAudio() # instancia classe PyAudio 
        stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
                    frames_per_buffer=CHUNK) #uses default input device

        # cria uma matriz numpy contendo uma única leitura de dados de áudio
        while True: # faz isso algumas vezes
            data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
            data = data * np.hanning(len(data)) # suaviza a FFT exibindo dados em janelas
            fft = abs(np.fft.fft(data).real)
            fft = fft[:int(len(fft)/2)] # mantem apenas o primeiro tempo
            freq = np.fft.fftfreq(CHUNK,1.0/RATE)
            freq = freq[:int(len(freq)/2)] # mantem apenas o primeiro tempo
            freqPeak = freq[np.where(fft==np.max(fft))[0][0]]+1
            print("peak frequency: %d Hz"%freqPeak)
            if (freqPeak > 300 and freqPeak <= 500):
                arduino.write(struct.pack('>B', 1))
            elif (freqPeak > 500 and freqPeak <= 800):
                arduino.write(struct.pack('>B', 2))
            elif (freqPeak > 800 and freqPeak <= 1000):
                arduino.write(struct.pack('>B', 3))
            elif (freqPeak > 1000 and freqPeak <= 1150):
                arduino.write(struct.pack('>B', 4))
            elif (freqPeak > 1150 and freqPeak <= 1200):
                arduino.write(struct.pack('>B', 5))
            elif (freqPeak > 1200 and freqPeak <= 1300):
                arduino.write(struct.pack('>B', 6))
            elif (freqPeak > 1300 and freqPeak <= 1400):
                arduino.write(struct.pack('>B', 7))
            elif (freqPeak > 1400 and freqPeak <= 1500):
                arduino.write(struct.pack('>B', 8))
            elif (freqPeak > 1500 ):
                arduino.write(struct.pack('>B', 9))
            else:
                arduino.write(struct.pack('>B', 0))

            # uncomment this if you want to see what the freq vs FFT looks like
            # plt.plot(freq,fft)
            # plt.axis([0,4000,None,None])
            # plt.show()
            # plt.close()

    except serial.SerialException as e:
        print("Erro ao tentar abrir a porta serial:", e)
    finally:
        if arduino is not None:
            arduino.close()

        # close the stream gracefully
        if 'stream' in locals() and stream.is_active():
            stream.stop_stream()
            stream.close()
        if 'p' in locals():
            p.terminate()


file_path = 'Foo-Fighters'
current_index = 0

def play_music(command, serialPort='COM9'):
    global current_index
    print(current_index)
    pygame.mixer.init()
    arquivos = [f for f in os.listdir(file_path) if f.lower().endswith(('.mp3', '.wav'))]
    if not arquivos:
        print("Nenhum arquivo de áudio encontrado na file_path.")
        return

    pygame.mixer.music.load(os.path.join(file_path, arquivos[0]))
    pygame.mixer.music.play()
    
    
    try:
        if command == "go":
            pygame.mixer.music.stop()
            current_index = (current_index + 1) % len(arquivos)
            pygame.mixer.music.load(os.path.join(file_path, arquivos[current_index]))
            pygame.mixer.music.play()
            fft_mode_song(serialPort)
            
        elif command == "stop":
            pygame.mixer.music.stop()
            # fft_mode_song(serialPort)
            
        elif command == "up":
            current_index = (current_index - 1) % len(arquivos)
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join(file_path, arquivos[current_index]))
            pygame.mixer.music.play()
            fft_mode_song(serialPort)
            
        elif command == "down":
            current_index = (current_index + 1) % len(arquivos)
            pygame.mixer.music.stop()
            pygame.mixer.music.load(os.path.join(file_path, arquivos[current_index]))
            pygame.mixer.music.play()
            fft_mode_song(serialPort)
            
        else:
            print("Comando não reconhecido. Encerrando a reprodução.")
            pygame.mixer.music.stop()
            # fft_mode_song(serialPort)
            
    except serial.SerialException as e:
        print("Erro ao tentar abrir a porta serial:", e)


# if __name__=="__main__":
#     play_music('down',serialPort='COM9')
    