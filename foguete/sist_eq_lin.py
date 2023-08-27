'''
Sistema de eqs Lineares

    Considere o sistema:
        |a11 x1 + a12 x2 + ... a1n xn = y1|
        |a21 x1 + a22 x2 + ... a2n xn = y2|
        :         :            :      :
        |am1 x1 + am2 x2 + ... amn xn = ym|

    O qual podemos escrever como Ax = y

Resolução de sistemas triangulares
    São sistemas em que a matriz A são matrizes triangulares

        A = L = | a11 0        0   0   |      A = U =  | a11 0        0   0   |
                | a21 a22      0   0   |               | 0   a22      0   0   |
                | a31 a32 a33  0   0   |  ou           | 0   0   a33  0   0   |    
                | a41 a42 a43  a44 0   |               | 0   0   0    a44 0   |     
                | a51 a52 a53  a54 a55 |               | 0   0   0    0   a55 |       


                                                 n-1
    x1 = y1       x2 = y2 - a21*x1     xn = yn - E(anj * xj)
         --            -----------               j=1   
         a11                a22             -----------------
                                                 ann

    Triângulo superior

    Xn = yn           xn-1 = yn-1 - a(n-1)n xn
         --                  -----------------
         ann                     a(n-1)(n-1)
'''


class resolve_matriz():
    def __init__(self) -> None:
        self.matriz = [[1, 1, 1], [2, 1, -1], [2, 2, 1]]
        self.resposta = [1, 0, 1]
        self.printa_matriz()
        self.arrumar_ordem()
        self.printa_matriz()
        self.escalona_matriz()
        self.printa_matriz()
        print('fim do escalonamento')
        self.diagonalizacao()
        respostas = self.encontrar_valores()
        self.printa_matriz()
        print(respostas)

    def encontrar_valores(self):
        respostas = []
        for i in range(len(self.matriz)):
            try:
                x = self.matriz[i][i] / self.resposta[i]
            except ZeroDivisionError:
                x = 0
            respostas.append(x)
        return respostas
    
    def diagonalizacao(self):
        for i in range(1, len(self.matriz)):
            index1 = len(self.matriz) - i 
            num_base = self.matriz[index1][index1]
            resp_base = self.resposta[index1]
            for j in range(i, len(self.matriz)):
                index2 = len(self.matriz) - j
                num = self.matriz[index2-1][index1]
                try:
                    multiplicador = num / num_base
                except ZeroDivisionError:
                    multiplicador = 0
                self.matriz[index2-1][index1] = num - num_base * multiplicador
                self.resposta[index2-1] = self.resposta[index2-1] - resp_base * multiplicador

    def escalona_matriz(self):
        for j in range(len(self.matriz)):
            for i in range(j+1, len(self.matriz)):
                try:
                    multiplicador =  self.matriz[j][j]/self.matriz[i][j]
                except ZeroDivisionError:
                    multiplicador = 0
                self.matriz[i] = self.subtrai_linhas(self.multiplica_linha (self.matriz[i], multiplicador), self.matriz[j])
                self.resposta[i] = self.resposta[i] * multiplicador - self.resposta[j]

    def subtrai_linhas(self, linha1: list, linha2:list) -> list:
        r = []
        for i in range(len(linha1)):
            subtraido = linha1[i] - linha2[i]
            r.append(subtraido)
        return r
    
    def multiplica_linha(self, linha: list, multiplicador: float) -> list:
        r = []
        for num in linha:
            prod = num * multiplicador
            r.append(prod)
        return r
    
    def arrumar_ordem(self):
        watch_line = float('-inf')
        for num, linha in enumerate(self.matriz):
            if linha[0] > watch_line:
                self.troca_de_linha(linha, num, )
            watch_line =  linha[0]
    
    def troca_de_linha(self, linha, num):
        guarda_primeira_linha= self.matriz[0]
        self.matriz[0] = linha
        self.matriz[num] = guarda_primeira_linha

        guarda_primeira_resposta = self.resposta[0]
        self.resposta[0] = self.resposta[num]
        self.resposta[num] = guarda_primeira_resposta
        
    def printa_matriz(self):
        print('-------------------------')
        for num, linha in enumerate(self.matriz):
            print(linha, ' ', self.resposta[num])
        print('-------------------------')

if __name__ == '__main__':
    resolvedor = resolve_matriz()