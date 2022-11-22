from random import randrange


def nivelFacil():
	n = randrange(100)
	contador = 0
	print("Descubra o valor que está entre 0 e 100")

	while  True:
		k = int(input("-> "))
		if n == k:
			print("\nVocê acertou")
			print("Numero de tentativas: ", contador)
			break
		print("Valor menor" if (n < k) else "Valor maior")
		contador += 1


def nivelMedio():
	n = randrange(1000)
	contador = 0
	print("Descubra o valor que está entre 0 e 1.000")

	while  True:
		k = int(input("-> "))
		if n == k:
			print("\nVocê acertou")
			print("Numero de tentativas: ", contador)
			break
		print("Valor menor" if (n < k) else "Valor maior")
		contador += 1


def nivelDificil():
	n = randrange(10000)
	contador = 0
	print("Descubra o valor que está entre 0 e 10.000")

	while  True:
		k = int(input("-> "))
		if n == k:
			print("\nVocê acertou")
			print("Numero de tentativas: ", contador)
			break
		print("Valor menor" if (n < k) else "Valor maior")
		contador += 1

print("\t***Jogo para descobrir valor****")

print("\n1.Facil\n2.Medio\n3.Dificil")
level = int(input("\nEscolha um nivel: "))

if(level == 1):
	nivelFacil()
elif(level == 2):
	nivelMedio()
elif(level == 3):
	nivelDificil()
else:
	print("\n\t***Valor incorreto***")

print("\nFim de jogo")
