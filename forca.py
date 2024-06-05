"""
Módulo com as funções básicas do aplicativo
"""

import os

import openai_module

# Entrada
palavras_forca = [openai_module.escolha_palavra()]

NUM_MAX_ERRO = 5


def escolha_palavra():
    return palavras_forca[0]


def mostre_palavra_terminal(palavra, caracteres_usados):
    palavra_ao_usuario = ''
    for letra in palavra:
        if letra in caracteres_usados:
            palavra_ao_usuario += letra
            palavra_ao_usuario += ' '
        else:
            palavra_ao_usuario += '- '
    print(f'Palavra: {palavra_ao_usuario}')


def mostre_erros_restantes(NUM_MAX_ERRO, num_erro):
    print(f'Número de erros disponíveis: {NUM_MAX_ERRO - num_erro}')


def mostre_estado_atual(palavra, caracteres_usados, num_erro, NUM_MAX_ERRO):
    os.system('cls')
    mostre_palavra_terminal(palavra, caracteres_usados)
    print(f'Letras já utilizadas: {caracteres_usados}')
    mostre_erros_restantes(NUM_MAX_ERRO, num_erro)


def mensagem_de_vitoria():
    print()
    print('Você ganhou!')
    print(f'A palavra era: {palavra}')
    print()
    exit()


def mensagem_de_derrota():
    print()
    print('Você perdeu!')
    print(f'A palavra era: {palavra}')
    print()
    exit()


palavra = escolha_palavra()
caracteres_usados = []
num_erro = 0