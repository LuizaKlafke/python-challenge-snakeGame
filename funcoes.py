import csv
from time import sleep


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


class Fim:
    def finalizarJogo(self, scores, highScores, filePath):

        for score in scores:
            highScores.append(score)

        highScores = Funcoes().removeRepetido(highScores)

        Funcoes().manipulaCsv('w', filePath, highScores)

        sleep(3)
