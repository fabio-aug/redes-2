from socket import *
from urllib import response


# Função responsável por pegar as respostas do aluno;
def getQuestions():
    # Array para guardar as respostas do aluno;
    questions = []

    # Estrutura para pegar as 5 questões;
    # Pergunta o número de alternativas;
    # Logo em seguida pega as respostas de acordo com o número de alternativas;
    for i in range(0, 5, 1):
        numAlternative = int(
            input(f"Informe o número de alternativas da questão {(i+1)}: "))
        alternatives = ''
        for j in range(0, numAlternative, 1):
            value = input(f"Informe a resposta da alternativa {(j+1)}: ")
            alternatives = alternatives + value
        questions.append(str(f"{i+1};{numAlternative};{alternatives}"))

    # Antes de enviar, transforma o array de respostas em uma string e joga tudo em maiúsculo;
    return str(questions).upper()


# Função mostrar o resultado do aluno recebido do servidor;
def showResult(data):
    # Transforma a string em uma expressão python, nesse caso, um dicionário enviado pelo servidor;
    responseData = eval(data)

    # Percorre todas as respostas corrigidas pelo servidor;
    # Forma uma string só, quebrando linha para cada respostas;
    # No fim junta com a pontuação final;
    printUser = '\nGabarito do usuário: \n'
    for responseQuestion in responseData['questionScore']:
        result = responseQuestion.split(";")
        printUser = printUser + \
            str(f"Questão: {result[0]} - Acerto: {result[1]} - Erro: {result[2]} \n")
    printUser = printUser + responseData['finalGrade']

    # Mostra as respostos corrigidas e a nota final;
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
