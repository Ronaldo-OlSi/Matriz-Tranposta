
def matz_nula(nlins, ncols):
    Mt = []
    for i in range(nlins):
        lin = [0] * ncols
        Mt.append(lin)
    return Mt

def transposta(Mt):
    nlins = len(Mt)
    ncols = len(Mt[0])
    Tr = matz_nula(ncols, nlins)
    for i in range(nlins):
        for j in range(ncols):
            Tr[j][i] = Mt[i][j]
    return Tr

def eh_igual(A, B):
    nlinsA, ncolsA = len(A), len(A[0])
    nlinsB, ncolsB = len(B), len(B[0])
    if (nlinsA == nlinsB) and (ncolsA == ncolsB):
        for i in range(nlinsA):
            for j in range(ncolsA):
                if A[i][j] != B[i][j]:
                    return False
        return True
    return False

def somar(A, B):
    Cl = []
    # Compara se A e B tem a mesma medida
    nLinsA, nLinsB = len(A), len(B)
    nColA, nColB = len(A[0]), len(B[0])
    if (nLinsA == nLinsB) and (nColA == nColB):

        for i in range(nLinsA):
            linha = [0] * nColA
            Cl.append(linha)
            for j in range(nColA):
                Cl[i][j] = A[i][j] + B[i][j]
    else:
        print("Matrizes não tem a mesma ordem")

    return Cl

def oposta(Mt):
    oposta = []
    for i in range(len(Mt)):
        linha = [0] * len(Mt[0])
        oposta.append(linha)
        for j in range(len(Mt[0])):
            oposta[i][j] = -Mt[i][j]
    return oposta

def subtrair(A, B):
    return somar(A, oposta(B))