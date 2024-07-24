def jogar_forca():

    print('*********************************')
    print('Bem vindo, ao JOGO FORCA')
    print('*********************************')
    #Definir qual a palavra secreta
    palavraSecreta = "pepino"

    enforcou = False
    acertou = False 
    erros = 0

    #Enquanto o jogador não se "enforcar" E não acertar a palavra, faça algo
    while(not enforcou and not acertou):
        chute = input("Escolha a letra?")
        chute = chute.strip()

        index = 0

        for letra in palavraSecreta:
            if(chute.upper() == letra.upper ()):
                letras_acertadas[index] = letra
            index += 1     

else:
    erros: += 1 #erros = erros + 1 
    enforcou = erros == 6 
    acertou = "_" not in letras_acertadadas
    print(letras_acertadas)


    print("Fim de jogo!")
if(__name__ == "__main__"):
    jogar_forca()