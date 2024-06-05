# funcoes que pedem a palavra ao ChatGPT

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openia_key = os.getenv("OPENAI_KEY")

client = OpenAI(api_key=openia_key)


def escolha_palavra():
    caracteres = input("Quantos caracteres vc deseja?")
    idioma = input("Qual idioma? ")
    dificuldade = input("Dificuldade: (0) Facil (1) Medio (2) Dificil ")
    if dificuldade == 0:
        dificuldade = "facil"
    elif dificuldade == 1:
        dificuldade = "medio"
    else:
        dificuldade = "dificil"

    prompt = [{"role": "user",
               "content": f"Gere uma palavra pra mim com {caracteres} caracteres, em {idioma} e em letras minusculas para um jogo da força em nivel {dificuldade}"}]

    response = client.chat.completions.create(
        messages=prompt,
        model="gpt-3.5-turbo-0125",
        max_tokens=1000,
        temperature=0
    )

    return response.choices[0].message.content