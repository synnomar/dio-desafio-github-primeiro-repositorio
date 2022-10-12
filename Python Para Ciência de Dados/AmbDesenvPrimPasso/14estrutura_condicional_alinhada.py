conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450


if conta_normal:
    if saldo >= saque:
        print('Saque Realizado com Sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com uso do cheque especial!')
    else:
        print('Não foi possivel realizar o saque, saldo insuficiente!')
elif conta_universitaria:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    else:
        print('Saldo insuficiente!')
elif conta_especial:
    print('Saldo insuficiente!')
else:
    print('Sistema não reconhece seu tipo de conta, entre em contato com seu gerente!')