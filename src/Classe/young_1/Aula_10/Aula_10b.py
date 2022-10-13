
def somar(a, b):
    return a + b


def dividir(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError as zero:
        return f'Não há divisão por zero! {zero}'
    except TypeError:
        return 'Você digitou um caracter que não é um número!'
    else:
        return 'oi'
    finally:
        print('Fim da função!')


if __name__ == '__main__':
    print(__name__)
    teste = somar(2, 3)
    teste2 = somar(12, 3)
    print(f'Teste1: {teste}')
    print(f'Teste2: {teste2}')
