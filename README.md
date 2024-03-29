# Speech Recognition Using CNN and Fourier Transform
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/RodrigoSantosB/speech-recognition-signal-project/blob/main/LICENSE) 

# About The Project 

Speech-recognition é uma aplicação contruida para reconhecer comandos chave por meio de uma CNN, na intenção de controlar um player de música e reproduzir os espéctros de frequências em uma sequência de leds
no arduino aplicando a FFT (Fast Fourier Transform) em tempo real.

A aplicação consiste em prever um comando escolhido para startar o player como: go-> inicia uma música; up-> troca para próxima música; down-> volta para música anterior e stop para a reprodução.
Inicialmente treina-se uma CNN obtendo amostras de audio com a mfcc ( Mel-frequency cepstral coefficients ) em uma base de dados  [Mini Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands?hl=pt-br)
A extração acontence da seguinte maneira:

## Layout mfcc
![MFCC_EXTRACTOR](https://github.com/RodrigoSantosB/speech-recognition/blob/main/images/mfcc_img.png)

## Layout CNN
![CNN_ALGORITHM](https://github.com/RodrigoSantosB/speech-recognition/blob/main/images/cnn_estructure.png) 
### A tabela abaixo mostra as configurações usadas para treinar a CNN, vale destacar que é possível personalizá-la com a finalidade de que a acurácia aumente.  
![CNN_TABLE](https://github.com/RodrigoSantosB/speech-recognition/blob/main/images/model_table.png)


## Modelo conceitual
![CONCEPT_MODEL](https://github.com/RodrigoSantosB/speech-recognition/blob/main/images/concept_model.png)

# Tecnologias utilizadas
## Extração de Features
- MFCC
- PLP
- LPC
- LPCC
## Treinamento da rede
- TensorFlow
- Keras
- Data-base-speech-commands
## Visualização
- Ploty (gráficos)
- Leds + Arduino (espéctro do sinal)

# Como executar o projeto

## Preparando o ambiente
#### Pré-requisitos: python 3.10.11. 
Certifique-se de adicionar uma pasta dentro da pasta do projeto que contenha música.mp3, além disso troque no script `music.py` a string da variável `file_path = 'Foo-Fighters'` para o nome da sua pasta que contém as músicas
```bash
## OBS: se a versão global do python não estiver como padrão do sistema, coloque-a como padrão
# Vá até a Áre de trabalho (Desktop), crie uma pasta chamada `workspace`

# entrar na pasta do projeto
cd workspace

# clonar repositório em workspace: [ex: C:\Users\seu-user\workspace
git clone https://github.com/RodrigoSantosB/speech-recognition-signal-project.git

# criar ambinte virtual em python 3.10.11
python -m venv "nome-do-ambiente"

# Ativar ambiente
Windows:
  .\nome_do_ambiente\Scripts\Activate
Linux:
  source nome_do_ambiente/bin/activate

# Executar o arquivo requirements.txt para instalar as dependências 
pip intall -r requirements.txt

```


## Montando o circuito
Pré-requisitos: Arduino UNO, Arduino IDE. O circuito em questão foi montado com a sequência de pinagem correspondente de 5-13, caso troque a sequência, é necessário fazer o ajuste no código `script.ino`.
Além disso, os resistores utilizados foram de 330 ohms, uma alternativa é usar um potenciômetro com a resistência equivalente a 9 resistores em paralelo. Ademais 9 leds também foram usados, seque o esquema abaixo:

![ARDUINO](https://github.com/RodrigoSantosB/speech-recognition/blob/main/images/circuito_ardu.png)

```bash
# Adicionar o código arduino na IDE arduiono

# Baixar e instalar dependência pacote FFT do arduino 

# Selecionar a COM_ID correspondente na qual a placa está conectada

```


## Treinamento do modelo
Primeiro, faça o download dos arquivos necessários para o treinamento da rede e extração de features:
Certifique-se de que ele esteja no mesmo diretório em que o código esteja inserido, além disso atualize as variáveis de path para os paths correspondente de sua máquina 
```
NO WINDOWS
Invoke-WebRequest -Uri "http://storage.googleapis.com/download.tensorflow.org/data/mini_speech_commands.zip" -OutFile "mini_speech_commands.zip"
```

```
NO LINUX
!wget http://storage.googleapis.com/download.tensorflow.org/data/mini_speech_commands.zip -O mini_speech_commands.zip
```

```bash
# Ajustar os caminhos para os caminho de sua máquina
# Executar o script .ipynb

# executar o projeto
./signal_and_systems_project.ipynb

ou RUN ALL na célula do VSCODE
```

## DEMONSTRAÇÃO

O modelo treinado prevê qual comando foi lido, então com base nele invoca o script que dá play na música e exibe isso no espéctro da frequência  por meio do arduino. 



![DEMO](https://github.com/RodrigoSantosB/speech-recognition/blob/main/images/demonstracao_gif.gif)


# Autor

Rodrigo Santos Batista

www.linkedin.com/in/rodrigo-santos-16029986
