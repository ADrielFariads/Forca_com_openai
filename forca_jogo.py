import forca as fc
import time
import openai_module

palavras_forca = fc.palavras_forca
NUM_MAX_ERRO = 5
palavra = fc.escolha_palavra()
caracteres_usados = []
num_erro = 0

while num_erro < NUM_MAX_ERRO:
    fc.mostre_estado_atual(palavra, caracteres_usados, num_erro, NUM_MAX_ERRO)
    tentativa = (input('Selecione uma letra ou tente uma palavra: ')).lower()

    if len(tentativa) == 1:
        if tentativa in caracteres_usados:
            print()
            print("Você já usou essa letra, tente outra!")
            time.sleep(2)

        else:
            if tentativa not in palavra:
                num_erro += 1
                caracteres_usados.append(tentativa)

            if tentativa in palavra:
                caracteres_usados.append(tentativa)

    elif len(tentativa) > 1:
        if tentativa == palavra:
            fc.mensagem_de_vitoria()

        if tentativa != palavra:
            print()
            print("Palavra errada!")
            time.sleep(1)
            num_erro += 1
fc.mensagem_de_derrota()
