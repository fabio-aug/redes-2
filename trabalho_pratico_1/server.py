from socket import *

FEEDBACK = [
    '1;4;VFVF',
    '2;5;VVVFF',
    '3;2;FF',
    '4;3;VFV',
    '5;3;FVF',
]

def resolveQuestion(data):
    question = data.split('-')
    print(question)
    print(data)
    return "Connection OK!"

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = resolveQuestion(connectionSocket.recv(1024).decode())
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
