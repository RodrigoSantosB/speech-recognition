# Speech Recognition Using CNN and Fourier Transform
[![NPM](https://img.shields.io/npm/l/react)](https://github.com/RodrigoSantosB/speech-recognition-signal-project/blob/main/LICENSE) 

# About The Project 

Speech-recognition é uma aplicação contruida para reconhecer comandos chave por meio de uma CNN, na intenção de controlar um player de música e reproduzir os espéctros de frequências em uma sequência de leds
no arduino aplincando a FFT (Fast Fourier Transform) em tempo real.

A aplicação consiste em prever um comando escolhido para startar o player como: go-> inicia uma música; up-> troca para próxima música; down-> volta para música anterior e stop para a reprodução.
Inicialmente treina-se uma CNN obtendo amostras de audio com a mfcc ( Mel-frequency cepstral coefficients ) em uma base de dados  [Mini Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands?hl=pt-br)
A extração acontence da seguinte maneira:

## Layout mfcc
![MFCC_EXTRACTOR](https://github.com/acenelio/assets/raw/main/sds1/mobile1.png) ![Mobile 2](https://github.com/acenelio/assets/raw/main/sds1/mobile2.png)

## Layout CNN
![CNN_ALGORITHM](https://github.com/acenelio/assets/raw/main/sds1/web1.png)

![Web 2](https://github.com/acenelio/assets/raw/main/sds1/web2.png)

## Modelo conceitual
![Modelo Conceitual](https://github.com/acenelio/assets/raw/main/sds1/modelo-conceitual.png)

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
Pré-requisitos: python 3.10.11
```bash
## OBS: se a versão global do python não estiver como padrão do sistema, coloque-a como padrão
# clonar repositório em um workspace: [ex: C:\Users\seu-user\workspace
git clone [repo]

# entrar na pasta do projeto
cd workspace

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
## Treinamento do modelo
Primeiro, faça o download dos arquivos necessário para o treinamento da rede e extraçao de features:
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
./mvnw spring-boot:run
```

## Front end web
Pré-requisitos: npm / yarn

```bash
# clonar repositório
git clone https://github.com/devsuperior/sds1-wmazoni

# entrar na pasta do projeto front end web
cd front-web

# instalar dependências
yarn install

# executar o projeto
yarn start
```

# Autor

Rodrigo Santos Batista

www.linkedin.com/in/rodrigo-santos-16029986
