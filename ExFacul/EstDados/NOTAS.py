# EXERCICIOS SOBRE BIG O
# EX 1
def Exercicio1 (dados):
    for i in range(0, len(dados)/2, 1):
        dados[i] = i * 2
# loop executado em n/2 vezes, logo T(n) = n/2 = O(n)

# EX 2
def Exercicio2 (dados):
    for i in range(0, len(dados), 1):
        dados[i] = i + 1
    for i in range(0, len(dados), 1):
        dados[i] = i - 1
# T(n) = n + n = O(n)

# EX 3
def Exercicio3 (dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            dados[i] = dados[j] + 1
# T(n) = n * n = O(n²)

# EX 4
def Exercicio4 (dados):
    for i in range(0, len(dados), 1):
        for j in range(i, len(dados), 1):
            dados[i] = dados[j] + 1
# T(n) = n * n = O(n²)

# EX 5
def Exercicio5 (dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            for k in range(0, 9000000, 1):
                dados[i] = dados[j] + 1
# T(n) = 9000000 * n * n = O(n²)

# EX 6 
def Exercicio6 (dados):
    for i in range(1, i*i, 1):
        print(i)
# x² ≤ n = x ≥ √n, logo T(n) = √n = O(√n)

# EX 7
def Exercicio7 (dados):
    if (n == 0):
        return 
    Exercicio7(n/2)
    print(n)
# T(n) = log2 n = O(log n)

# EX 8
def Exercicio8 (dadosA = [], dadosB = []):
    sort(dadosB)
    for i in range(0, len(dadosA), 1):
        if(busca(dadosB, i) >= 0):
            return i
# Tsort(B) = O(B * logB) / Tbusca(B) = O(logB)
# T(A,B) = O(B * logB) + A * O(logB) = O((A+B)*logB)

# -------------------------------------------------------------------------------------------

