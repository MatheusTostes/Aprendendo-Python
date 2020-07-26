# O objetivo era criar uma calculadora com operações básicas e interface.

# Resultado: https://i.imgur.com/277HGa4.png

from tkinter import *

class Calculadora:
	def __init__(self, janela):                                                                        # Inicializa a classe.
		self.dados = Entry(janela, justify='right', bd=2, bg='orange')				   # Cria umaa caixa para a entrada dos números.
		self.dados.grid(row = 1, column = 0, sticky=N+S+E+W)					   # Posiciona e dimensiona a caixa.
		self.frame = Frame(janela)  								   # Cria a janela.
		self.frame.grid()									   # Cria a grade na janela.

		bts = ["1", "2", "3", "+", "4", "5", "6", "-", "7", "8", "9", "*", ".", "0", "/", "C", "="]# Determina o valor visual e numérico dos botões.
		r = 1											   # Contador inicial de linhas para posicionar os botões.
		c = 0											   # Contador inicial de colunas para posicionar os botões.
		for bt in bts:										   # Loop for seguido de lambda para preencher os botões com
			comando = lambda x = bt: self.calcular(x)					   ## os valores e dimensiona-los.
			self.botao = Button(self.frame, text = bt, width = 6, command = comando)				
			self.botao.grid(row = r, column = c)
			c += 1										   # Posiciona um botão por coluna.
			if c > 3:								           # Pula à próxima linha no limite de 3 botões.
				c = 0
				r += 1

	def calcular(self, valor):																		
		if valor == "=":									   # Identifica quando a tecla = é pressionada.
			tudo = "123456789/*-+."                                                                 
			if self.dados.get()[0] not in tudo: 						   # Restringe os valores de entrada.
				self.dados.insert(END, "operação inválida!")				   # Retorna aviso em caso de valor inválido.
			try:
				resultado = eval(self.dados.get())					   # Analisa os valores de entrada e realiza os operadores.
				self.dados.insert(END, "="+str(resultado))				   # Retorna o sinal de = seguido do resultado.
			except:
				self.dados.insert(END, "="+"Error!")					   # Retorna erro em caso de impossibilidade matemática.
		elif valor == "C":																			
			self.dados.delete(0, END)							   # Define um botão C para limpar o display.
		else:
			if "=" in self.dados.get():
				self.dados.delete(0, END)						   # Deleta o resultado antigo sempre que um novo número
			self.dados.insert(END, valor)							   ## for digitado após o botão = ser pressionado.


janela = Tk()
janela.title("Calculadora")

Calculadora(janela)
janela.mainloop()
