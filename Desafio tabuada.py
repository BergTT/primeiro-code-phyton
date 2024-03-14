while True:
    print("Olá amigo(a)")

    numero = input("\nDigite um número de 1 à 10 para tabular: ")

    if numero.isdigit():
        numero = int(numero)
        if 1 <= numero <= 10:
            print("\nAqui está a tabuada do " + str(numero) + ":")
            for i in range(1, 11):
                resultado = numero * i
                print(f"{numero} x {i} = {resultado}")
        else:
            print("Número fora do intervalo válido (1 a 10).")
    else:
        print("Entrada inválida. Por favor, insira um número inteiro de 1 a 10.")
    
    continuar = input("\nDeseja fazer outra operação? (s/n): ")
    if continuar.lower() != 's':
        break

