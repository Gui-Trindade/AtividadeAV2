##Atividade 01

try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))
    resultado = numero1 / numero2
except ValueError:
    print('Entrada inválida! Digite apenas números.')
except ZeroDivisionError:
    print('Não é possível dividir por zero!')
else:
    print('Resultado da divisão:', resultado)

##Atividade 02

def calcular_media(notas):
    return sum(notas) / len(notas)


notas = [8, 7, 9, 6]
print('Média:', calcular_media(notas))


##Atividade 03

def verificar_carga(horas):
    if horas >= 40:
        return 'Carga completa'
    else:
        return 'Carga incompleta'


horas = float(input('Digite as horas trabalhadas na semana: '))
print(verificar_carga(horas))

##Atividade 04

def calcular_saldo(saldo_atual, valor, operacao):
    if operacao == 'deposito':
        return saldo_atual + valor
    elif operacao == 'saque':
        return saldo_atual - valor
    else:
        return saldo_atual


saldo = float(input('Digite o saldo atual: '))
valor = float(input('Digite o valor da operação: '))
operacao = input('Digite a operação (deposito ou saque): ').lower()
print('Novo saldo:', calcular_saldo(saldo, valor, operacao))


##Atividade 05

def notas_aprovadas(notas):
    aprovadas = []
    for nota in notas:
        if nota >= 7:
            aprovadas.append(nota)
    return aprovadas


notas = [5, 7, 8, 6, 9, 10]
print('Notas aprovadas:', notas_aprovadas(notas))


