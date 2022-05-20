from socket import *
from urllib import response

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

def showResult(data):
    responseData = eval(data)

    printUser = '\nGabarito do usuário: \n'
    for responseQuestion in responseData['user']:
        result = responseQuestion.split(";")
        printUser = printUser + str(f"Questão: {result[0]} - Acerto: {result[1]} - Erro: {result[2]} \n")
    printUser = printUser + responseData['grade']
    print(printUser)

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = getQuestions()
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
showResult(modifiedSentence.decode())
clientSocket.close()