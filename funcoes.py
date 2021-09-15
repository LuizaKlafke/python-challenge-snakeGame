import csv
import math
from os import O_APPEND


class Funcoes():

    def removeRepetido(self, lista):
        l = []
        for i in lista:
            if i not in l:
                l.append(i)

        return l

    def manipulaCsv(self, operacao, filePath, lista):

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

    def calculaDiferenca(self, eixo, posCobra, posComida):

        valor = 0

        if eixo == "x":
            valor = 0

        elif eixo == "y":
            valor = 1

        return math.floor(abs(posCobra[valor]))-math.floor(abs(posComida[valor]))
