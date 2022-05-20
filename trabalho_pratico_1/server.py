from socket import *

FEEDBACK = [
    '1;4;VFVF',
    '2;5;VVVFF',
    '3;2;FF',
    '4;3;VFV',
    '5;3;FVF',
]

PONCTUATION_SUCCESS = [0] * 5
PONCTUATION_ERROR = [0] * 5

def resolveQuestion(data):
    questions = eval(data)

    userPonctuation = []
    userGrade = 0

    for i in range(0,5,1):
        if (questions[i] == FEEDBACK[i]):
            userPonctuation.append(str(f"{i+1};1;0"))
            PONCTUATION_SUCCESS[i] += 1
            userGrade += 1
        else:
            userPonctuation.append(str(f"{i+1};0;1"))
            PONCTUATION_ERROR[i] += 1

        print(str(f"Questão: {i+1} - Acerto: {PONCTUATION_SUCCESS[i]} - Erro: {PONCTUATION_ERROR[i]}"))

        responseData = {
            'user': userPonctuation,
            'grade' : str(f"Nota: {userGrade}/5")
        }

    return str(responseData)

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = resolveQuestion(connectionSocket.recv(1024).decode())
    capitalizedSentence = sentence
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()