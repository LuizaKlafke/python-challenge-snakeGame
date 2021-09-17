#
# Programa que executa funções secundárias ao jogo.
#

import csv


# Remove itens repetidos de uma lista.

def removeRepetido(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)

    return l


# Cria, Lê ou escreve arquivo CSV.

def manipulaCsv(operacao, filePath, lista):
    with open(filePath, operacao, newline='') as csvfile:

        if operacao == 'w':
            writer = csv.writer(
                csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(lista)

        elif operacao == 'r':
            reader = csv.reader(
                csvfile, delimiter=' ', quotechar='|')
            for row in reader:
                for str in row:
                    lista.append(int(str))
                return lista

# Faz varredura de pontos, remove valor repetido, e escreve no banco de dados CSV.


def finalizarJogo(scores, highScores, filePath):
    for score in scores:
        highScores.append(score)

    highScores = removeRepetido(highScores)

    manipulaCsv('w', filePath, highScores)
