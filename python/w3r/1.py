numeros = str(input("Introduce los numeros: ")).split()
numeros.append(0)
print(numeros)


def diferenciador(data):
    if len(data) == len(set(data)):
        return True;
    else:
        return False;

print(diferenciador([1,2,3,3,2,3]))