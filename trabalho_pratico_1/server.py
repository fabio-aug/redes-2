from socket import *

# Gabarito contendo todas as respostas;
# Por padrão foram definidas 5 questões;
FEEDBACK = [
    '1;4;VFVF',
    '2;5;VVVFF',
    '3;2;FF',
    '4;3;VFV',
    '5;3;FVF',
]

# Pontuação global de acertos das questões;
PONCTUATION_SUCCESS = [0] * 5
# Pontuação global de erros das questões;
PONCTUATION_ERROR = [0] * 5


# Função responsável por avaliar as respostas do aluno e calcular o resultado final;
def resolveQuestion(data):
    # Transforma a string em uma expressão python, nesse caso, um array enviado pelo aluno;
    questions = eval(data)

    userPonctuation = []
    userGrade = 0

    # Percorrendo todas as questões do gabarito e respostas enviadas pelo aluno;
    # Avaliamos TODA a questão, ou seja, se errar UMA alternativa consideramos a questão como ERRADA;
    # De acordo que o aluno acerta e erra as questões adicionamos as respostas ao array de correção 'userPonctuation';
    for i in range(0, 5, 1):
        if (questions[i] == FEEDBACK[i]):
            userPonctuation.append(str(f"{i+1};1;0"))
            PONCTUATION_SUCCESS[i] += 1
            userGrade += 1
        else:
            userPonctuation.append(str(f"{i+1};0;1"))
            PONCTUATION_ERROR[i] += 1

        # Mostra o resultado para o professor no servidor;
        print(str(
            f"Questão: {i+1} - Acerto: {PONCTUATION_SUCCESS[i]} - Erro: {PONCTUATION_ERROR[i]}"))

    # Cria um dicionário com o resultado final (array com o resultado de cada questão e a soma total da pontuação do aluno);
    # Logo em seguida transformamos em uma string para o envio;
    responseData = {
        'questionScore': userPonctuation,
        'finalGrade': str(f"Nota: {userGrade}/5")
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
