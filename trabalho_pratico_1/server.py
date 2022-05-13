from socket import *
"""
questionCount = [
    {question: 1, error: 0, right: 0},
    {question: 2, error: 0, right: 0},
    {question: 3, error: 0, right: 0},
    {question: 4, error: 0, right: 0},
    {question: 5, error: 0, right: 0},
]

FEEDBACK = [
    {question: 1, quantity: 4, response: 'VFVF'},
    {question: 2, quantity: 5, response: 'VVVFF'},
    {question: 3, quantity: 2, response: 'FF'},
    {question: 4, quantity: 3, response: 'VFV'},
    {question: 5, quantity: 3, response: 'FVF'},
]
"""


def resolveQuestion(data):
    """
    response = data.split(";")

    responseFinal = ''

    for ask in FEEDBACK:
        if(response[0] == ask.question):
            if(response[1] == ask.quantity):
                sumNote = 0
                for i in (0, ask.quantity, 1):
                    if (response[2][i] == ask.response[i]):
                        sumNote = sumNote + 1
            else:
                responseFinal = 'Número de alternativas errada'
        else:
            responseFinal = 'Resposta não encontrada'
    """
    return data.replace(";", " oi luana ")


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
