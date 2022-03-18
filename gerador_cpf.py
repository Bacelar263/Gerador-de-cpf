# Import da biblioteca random que vai gerar um cpf novo
from random import randint
# Import da biblioteca os que vai permitir executar um comando cmd
import os

print("[-] Aguarde enquanto procuramos um cpf válido para você")

# while true que vai fazer rodar o programa gerando novos números e verificando se tem o cpf
while True:

    # Gera 11 números aleatórios que vai ser o novo cpf
    cpf = str(randint(10000000000, 99999999999))

    # Quantidade de caracteres que serão utilizados na primeira conta
    tamanho_cpf1 = 9
    # Contador da primeira equação
    contador = 0

    # Estrutura de repetição que vai executar todos os cálculos para descobrir o primeiro número para verificar se vai ser válido
    while contador <= tamanho_cpf1:
        # Lista de um a um o caractere do cpf gerado
        n = cpf[contador]
        # Estrutura de condição para fazer a multiplicação de acordo o caractere
        if contador == 0:
            n1 = int(n) * 10
        elif contador == 1:
            n2 = int(n) * 9
        elif contador == 2:
            n3 = int(n) * 8
        elif contador == 3:
            n4 = int(n) * 7
        elif contador == 4:
            n5 = int(n) * 6
        elif contador == 5:
            n6 = int(n) * 5
        elif contador == 6:
            n7 = int(n) * 4
        elif contador == 7:
            n8 = int(n) * 3
        elif contador == 8:
            n9 = int(n) * 2

        # Aumenta o contador
        contador = contador + 1

    # Soma o total das multiplicações
    nt = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9

    # Cálculo final para a primeira conta que gerará o décimo número do cpf
    r = 11 - (nt % 11) 

    # Caso seja maior que 9, o resultado será 0
    if r > 9:
        r = 0

# ===============================================================================================
# SEGUNDO CÁLCULO
# ===============================================================================================

    # Quantidade de caracteres que serão utilizados na segunda conta
    tamanho_cpf2 = 10
    # Contador da segunda equação
    contador2 = 0

    # Estrutura de repetição que vai executar todos os cálculos para descobrir o segunda número para verificar se vai ser válido
    while contador2 <= tamanho_cpf1:
        # Lista de um a um o caractere do cpf gerado
        c = cpf[contador2]
        # Estrutura de condição para fazer a multiplicação de acordo o caractere
        if contador2 == 0:
            c1 = int(c) * 11
        elif contador2 == 1:
            c2 = int(c) * 10
        elif contador2 == 2:
            c3 = int(c) * 9
        elif contador2 == 3:
            c4 = int(c) * 8
        elif contador2 == 4:
            c5 = int(c) * 7
        elif contador2 == 5:
            c6 = int(c) * 6
        elif contador2 == 6:
            c7 = int(c) * 5
        elif contador2 == 7:
            c8 = int(c) * 4
        elif contador2 == 8:
            c9 = int(c) * 3
        elif contador2 == 9:
            c10 = int(c) * 2

        # Aumenta o contador
        contador2 = contador2 + 1

    # Soma o total das multiplicações
    ct = c1 + c2 + c3 + c4 + c5 + c6 + c7 + c8 + c9 + c10

    # Cálculo final para a primeira conta que gerará o décimo primeiro número do cpf
    u = 11 - (ct % 11)

    # Pega o décimo número do cpf gerado
    dg1 = cpf[9]
    # Pega o décimo primeiro número do cpf gerado
    dg2 = cpf[10]

    # Se o décimo número e o décimo primeiro forem iguais aos gerados no cálculo então o cpf é válido
    if (int(dg1) == r) and (int(dg2) == u):
        # Limpa a tela
        os.system("cls")
        print("===============================")
        print("CPF VÁLIDO ENCONTRADO")
        print("===============================")
        # Informa o número do cpf válido encontrado
        print("Seu cpf é: ", cpf)
        # Encerra o ciclo de repetição
        break

