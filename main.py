print ("Escolha uma palavra chave!")
chave = input ()
print ("\n" * 50)

chutes = []
tentativas = 6
resultado = ""
ja_chutados = []
alfabeto = []
caracteres = len(chave)

for i in range (97,123):
  alfabeto.append (chr(i))

print("Para ver as letras já chutadas escreva 'help'")
print("Palavras sem acento e em letra minúscula")
print ("A palavra tem %s letras" % caracteres)
print("\n")

while True:

  print ("Chute uma letra")
  chute = input()
  resultado = ""
  chutes.append(chute)
  
  if chute == "help":
    print (ja_chutados)
  else:
    if len(chute) > 1:
      print ("Chute inválido :/")
    elif chute in ja_chutados:
      print ("Você já chutou isso :/")
    elif chute not in alfabeto:
      print ("Chute inválido :/")

    elif chute in chave:
      print ("Acertou! :) ")
    elif chute in ja_chutados:
      continue  

    elif chute not in chave:
      print ("Errou :( ")
      tentativas -= 1

    ja_chutados.append(chute)
  
    for letra in chave:
      if letra in chutes:
        resultado += letra
      else:
        resultado += "_ "  

    if tentativas == 1:
      print ("Você ainda tem %d tentativa" %(tentativas))
    else:
     print ("Você ainda tem %d tentativas" %(tentativas))
  
  print (resultado)
  print ("\n")

  if resultado == chave:
    print ("Parabéns você ganhou! :D")
    break 

  if tentativas == 0:
   print ("Você perdeu. T_T")
   print ("A palavra era " + chave)
   break
