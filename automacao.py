x = int(input("Digite um número: "))
print("O número digitado é:", x)

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)
numero = int(input("Digite um número para calcular o fatorial: "))
resultado = calcular_fatorial(numero)
print(f"O fatorial de {numero} é {resultado}") 
