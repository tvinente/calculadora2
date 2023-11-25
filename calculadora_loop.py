def calcular(numero1, numero2, operacao):

    if operacao == 1:
        return numero1 + numero2
    elif operacao == 2: 
        return numero1 - numero2
    elif operacao == 3:
        return numero1 * numero2
    elif operacao == 4:
        return numero1 / numero2
    
def escolher_opcoes():
    print("Escolha uma operação:")
    print("1: Somar")
    print("2: Subtrair")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")
    print("\n")

def validar(mensagem, tipo):
    while True:
        try:
            valor = tipo(input(mensagem))
            return valor
        except ValueError:
            print("Essa opção não existe" )

operacao = 1
while operacao !=0:
    escolher_opcoes()
    operacao = validar("Digite o número da operação:", int)
    if operacao == 0:
        exit()
    elif operacao in [1, 2, 3, 4]:
        valor1=(int(input(("Digite o primeiro valor:"))))
        valor2 = (int(input(("Digite o segundo valor:"))))  
        resultado = calcular(valor1, valor2, operacao)
        print("Resultado: %.2f \n" % resultado)
    else: 
        print("\n Essa opção não existe \n" )