from main import *

testWord = "python" # palavra de teste
print("\nBem vindo ao arquivo de testes da nossa APS!!\n")
print("\nAqui você poderá testar os funcionamentos de cada função implementada\n")

print("Nosso projeto é baseado na conversão de mensagens para matrizes e vice-versa,")
print("através das funções para_one_hot e para_string.\n")
print("As quais são utilizadas para converter uma mensagem para uma matriz e depois para uma string.\n")
M = para_one_hot(testWord) # matriz
print(f"M = para_one_hot('{testWord}')")
print(f"Resultado: {para_one_hot(testWord)}")
print(f"S = para_string(M)")
print(para_string(M)+"\n") 

print("Além disso, também podemos utilizar uma matriz auxiliar, com um alfabeto embaralhado.\n Com o intuito de criptografar uma mensagem através de uma cifra usando uma multiplicação matricial.\n")
cifrador_auxiliar  = para_one_hot("ijkl mnopqrstuvwxyzabcdefgh") # cifrador auxiliar
C = cifra(testWord, cifrador_auxiliar )
print(f"C = cifra('{testWord}', auxiliar)")
print(f"Resultado: {cifra(testWord, cifrador_auxiliar)}")
print(f"DC = de_cifra('{testWord}', auxiliar)")
print(de_cifra(C, cifrador_auxiliar )+"\n")

print("Para finalizar, temos a função enigma, que é uma combinação de cifra + cifra auxiliar, sendo assim nossa função principal!\n ")
print(" Essa utiliza a multiplicação matricial para criptografar uma mensagem, utilizando uma cifra e uma cifra auxiliar.\n")
cifrador_auxiliar2 = para_one_hot("zxcvbnm asdfghjklpoiuytrewq")
E = enigma(testWord,cifrador_auxiliar ,cifrador_auxiliar2)
print(f"E = enigma('{testWord}',auxiliar,auxiliar2)")
print(E)
print("DE = de_enigma(E,auxiliar,auxiliar2)")
print(de_enigma(E,cifrador_auxiliar ,cifrador_auxiliar2)+"\n")