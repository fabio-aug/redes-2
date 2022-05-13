from socket import *


def getQuestion():
    numQuestion = int(input("Informe o número da questão: "))
    numAlternative = int(input("Informe o número de alternativas: "))
    response = input("Informe suas respostas: ")

    return str(numQuestion) + ";" + str(numAlternative) + ";" + response


serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = getQuestion()
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()
