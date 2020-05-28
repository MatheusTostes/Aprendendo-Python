# Conversor de binário para decimal
  ## Rápida explicação de como decimais são convertidos em binários: 
  ## Para tal, usa-se uma fórmula simples. Devemos dividir o número decimal por 2 e em seguida o resultado de sua divisão por 2 (os restos 
  ## das divisões são importantes), até que o resultado da última divisão seja 1. Após isso, nosso número decimal sera o último valor 1, 
  ## acrescido de todos os outros restos das divisões anteriores. Logo, para converter binários em decimais, faremos o passo inverso com o 
  ## uso de exponenciais.
  
bnr = input('Digite um valor binário de até 8 dígitos:')      # Define a variável bnr com o valor da entrada

def check(string) :                                           # Define a função check     
    t = '01'                                                  ## Cria uma fonte de busca com os dígitos possíveis
    for char in string :                                      ## Faz um loop for para verificar se cada elemento da string está contido em t
        if char not in t or len(bnr) > 8:                     ### Se o elemento for diferente de algum elemento em t ou a entrada possuir mais de 8 dígitos, avisa restrição e para
            print("O valor deve conter apenas 0 ou 1 e até oito dígitos")
            break 
        else :                                                ## Senão, passar
            bnr2 = list(bnr)                                  # Cria uma lista (para que futuramente possamos utilizar o método pop)
            value = 0                                         # Define o value partindo de 0
            
            for i in range(len(bnr)):                         # Varre os elementos do valor inserido, a partir de um range que tem como final o seu último elemento
                digit = bnr2.pop()                            # Busca o último elemento da lista que criamos com o valor binário
                if digit == '1':                              # Se o dígito for igual a 1 
                    value = value + pow(2, i)                 ## Adiciona à variável value 2^i (sendo i a posição do enésimo elemento da lista bnr sendo varrido) 
            print("O binário convertido em decimal é", value) # Exibe o resultado
            break
    
check(bnr)                                                    # Checa o valor com a função definida acima
