def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print('Iniciando contagem das notas!')
        print('Retire o seu dinheiro')
    else:
        print('Saldo insuficiente')

    print('Obrigado por ser nosso cliente, tenha um bom dia')

def depositar(valor):
    saldo = 500
    saldo +=valor



sacar(1000)