
def exibir_matriz(matz):
    # Exibe a matriz
    for lin in matz:
        print(lin)

def ler_matriz(arq):
    matz = []
    arq = open(arq, "r")
    lin = arq.readline()
    while lin != "":
        els = lin.split()
        for n in range(len(els)):
            els[n] = int(els[n])
        matz.append(els)
        lin = arq.readline()
    arq.close()
    return matz

if __name__ == "__main__":

    # Requisita os elementos ao usuário
    lin = int(input("Qual o número de linhas: "))
    coluna = int(input("Qual o número de colunas: "))

    matz = []
    for i in range(lin):
        lin = []
        for j in range(coluna):
            elemt = input("Elemento da linha {} e coluna {}".format(i, j))
            lin.append(int(elemt))
        matz.append(lin)

    exibir_matriz(matz)

    # Cria matriz vinda de um arquivo .txt
    matriz = ler_matriz("matriz1.txt")
    exibir_matriz(matriz)