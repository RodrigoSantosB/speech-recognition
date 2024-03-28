
import os
import librosa
import numpy as np
import librosa.display as ld
from IPython.display import Audio

import music as mc



def make_inference(model, path, predict, commands, serialPort='COM9'):
    # Lista todos os arquivos no diretório e subdiretórios
    dir_music = []
    for root, dirs, files in os.walk(path):
        for file in files:
            dir_music.append(os.path.join(root, file))


    n_files = len(dir_music)
    #print(n_files)
    rnd = np.random.randint(0, n_files)
    #print(rnd)
    path_music = dir_music[rnd]
    predict(model, path_music, commands)
    audio, sample_rate = librosa.load(path_music, sr = 16000)
    predict_command = path_music.split('\\')[-2]
    bar = '|'
    print('\n\n')
    print('-'*100)
    print(bar + ' Arquivo: ', rnd)
    print('-'*100)
    print(bar + ' Path: ', path_music)
    print(bar + ' Command: ', predict_command)
    print('-'*100)
    print('\n\n')


    current_index = 0

    # print(current_index)
    mc.play_music(predict_command)
    # print(current_index)
    # play_music(predict_command, serialPort)

    Audio(data = audio, rate = sample_rate)


