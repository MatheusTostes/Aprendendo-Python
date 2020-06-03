# Entrada dos lados do triângulo a ser analisado
# Resultado: https://i.imgur.com/5I6uX21.png

a = int(input("Digite um valor para o lado A:"))
b = int(input("Digite um valor para o lado B:"))
c = int(input("Digite um valor para o lado C:"))


# Condições para existência e cada tipo de triângulo

if (a <= 0 or b <= 0 or c <= 0):
    print("Valores invalidos.")  
    
else: 
    if (a + b <= c or a + c <= b or b + c <= a):
         print("Valores nao podem formar um triangulo.")

    else:        
        if (a == b and a == c):
             print("Triangulo equilatero.")

        if (a == b and b !=c or a == c and a != b or c==b and c != a):
             print("Triangulo isosceles.")

        if (a != b and b != c and a != c):
             print("Triangulo escaleno.")

        if ((b ** 2  == (a ** 2 + c ** 2)) or (a ** 2  == (b ** 2 + c ** 2)) or (c ** 2  == (a ** 2 + b ** 2))):
            print("Triangulo retangulo.")

        if (((b ** 2 < (a ** 2 + c ** 2))and a<=b and c<=a) or ((a ** 2 < (c ** 2 + b ** 2))and c <= a and b <= c) or ((c ** 2 < (b ** 2 + a ** 2))and b <= c and a <= b)):
            print("Triangulo acutangulo.")

        if (b ** 2 > (a ** 2 + c ** 2)) or (a ** 2 > (b ** 2 + c ** 2)) or (c ** 2 > (b ** 2 + a ** 2)):
            print("Triangulo obtusangulo.")
