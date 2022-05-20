from socket import *

def getQuestions():
    questions = []
    for i in range(0, 5, 1):
        numAlternative = int(input(f"Informe o número de alternativas da questão {(i+1)}: "))
        alternatives = ''
        for j in range(0, numAlternative, 1):
            value = input(f"Informe a resposta da alternativa {(j+1)}: ")
            alternatives = alternatives + value
        questions.append(str(f"{i+1};{numAlternative};{alternatives}"))
    return str(questions).upper()

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = getQuestions()
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server:', modifiedSentence.decode())
clientSocket.close()