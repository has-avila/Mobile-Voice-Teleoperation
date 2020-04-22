O Mobile Voice Teleoperation (MVT) é um projeto inicial para executar a teleoperação por voz de uma plataforma robótica móvel utilizando o ROS.

Embora seja um projeto em fase embrionária, o sistema de controle da teleoperação foi testada tanto em software quanto em campo.

Ainda é necessário a criação de um aplicativo Mobile eficaz, utilizar técnicas de reconhecimento de voz e que seja capaz de enviar para o tópico de controle as palavras-chave: frente, tras, esquerda, direita e para.  

Requisitos Necessários:
Ubuntu 16.04
ROS Kinect Kame
Gazebo com Turtlebot ou Robô físico

Regras de movimento do robô:

Frente:

frente + frente = frente
frente + tras = tras
frente + esquerda = frente esquerda
frente + direita = frente direita
frente + para = para

Tras:

tras + frente = frente
tras + tras = tras
tras + esquerda = tras esquerda
tras + direita = tras direita
tras + para = para

Esquerda:

esquerda + frente = frente
esquerda + tras = tras
esquerda + esquerda = esquerda
esquerda + direita = direita
esquerda + para = para

Direita:

direita + frente = frente
direita + tras = tras
direita + esquerda = esquerda
direita + direita = direita
direita + para = para

Para:

para + frente = frente
para + tras = tras
para + esquerda = esquerda
para + direita = direita
para + para = para

Frente Esquerda:

frente esquerda + frente = frente
frente esquerda + tras = tras
frente esquerda + esquerda = esquerda
frente esquerda + direita = frente direita
frente esquerda + para = para

Frente Direita

frente direita + frente = frente
frente direita + tras = tras
frente direita + esquerda = frente esquerda
frente direita + direita = direita
frente direita + para = para

Tras Esquerda:

tras esquerda + frente = frente
tras esquerda + tras = tras
tras esquerda + esquerda = esquerda
tras esquerda + direita = tras direita
tras esquerda + para = para

Tras Direita:

tras direita + frente = frente
tras direita + tras = tras
tras direita + esquerda = tras esquerda
tras direita + direita = direita
tras direita + para = para

Toda vez que o ultimo comando é “para”, o robo deve parar o movimento.
