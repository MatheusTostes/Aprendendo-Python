# A ideia é permitir conversões entre as escalas celsius, farenheight e kelvin.

print("Escolha a conversão desejada")				# Informações para explicar o uso do programa.

print("1 = celsius para kelvin")
print("2 = kelvin para celsius")
print("3 = celsius para fahrenheit")			
print("4 = fahrenheit para celsius")
print("5 = fahrenheit para kelvin")
print("6 = kelvin para fahrenheit")


ope = input("Conversão :")					# Entrada para o tipo de conversão.

temp = input("Digite a temperatura :" )				# Entrada para o valor da temperatura a ser convertida.


def convert():

    entradas = '1234567890.'					# Elementos de entrada possíveis para temperatura.
    operadores = '123456'					# Elementos de entrada possíveis para os operadores.
    
    if ope not in operadores:					# Checa se o operador está contido no dicionário operadores
        print("Número de operador inválido")		    ## senão, retorna erro.
    else:
        for i in temp:						# Se o operador o operador for válido, verifica se os valores inseridos
            if i not in entradas:				## estão no dicionário entradas, senão, retorna erro.
                print("Valores inválidos")
            else:
                op = int(ope)					# Se ambos operadores e valores são válidos, retira os dois do formato string.
                t = float(temp)					# Usa-se float para os valores pois podem receber entradas não inteiras.

                if op == 1:					# Condicional para chamar a equação com base no valor do operador.
                    rst = str(t + 273)				
                    print(rst+ " K")				# Printa na tela o resultado da função seguido da letra que identifica a temperatura final.
                elif op == 2:					# Os passos acima se repetem.
                    rst = str(t - 273)
                    print(rst+ " ºC")
                elif op == 3:
                    rst = str((t * 1.8)+32)
                    print(rst+ " ºF")
                elif op == 4:
                    rst = str((t - 32)/1.8)
                    print(rst+ " ºC")
                elif op == 5:
                    rst = (t - 32)/1.8 				# Em vez de manipular uma equação que converta fahrenheit para kelvin, converte
                    rst = str(rst + 273)			## fahrenheit para celsius e depois celsius para kelvin.
                    print(rst+ " K")
                elif op == 6:
                    rst = t - 273				# A mesma lógica do comentário acima.
                    rst = str((t * 1.8)+32)
                    print(rst+ " ºF")
            break 						# Caso não fosse inserido este break, o for faria um print para cada casa decimal do valor inserido.

convert()							# Executa a função convert depois dos dois inputs serem inseridos.
