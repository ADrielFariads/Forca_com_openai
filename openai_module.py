# funcoes que pedem a palavra ao ChatGPT

from openai import OpenAI
from dotenv import load_dotenv
import key

load_dotenv()
openia_key = key.OPENAI_API_KEY

client = OpenAI(api_key=openia_key)

def escolha_palavra():
    caracteres = input("Quantos caracteres você deseja? ")
    idioma = input("Qual idioma? ")
    dificuldade = input("Dificuldade: (0) Facil (1) Medio (2) Dificil ")
    
    if dificuldade == 0:
        dificuldade = "facil"
    elif dificuldade == 1:
        dificuldade = "medio"
    else:
        dificuldade = "dificil"

    palavras_usadas = []

    with open('palavras_usadas.txt', 'r') as arquivo:
        for palavra in arquivo:
            palavras_usadas.append(palavra)
    
    palavras_usadas_string = ", ".join(palavras_usadas)

    prompt = [{"role": "user",
               "content": f"Gere uma palavra para mim com {caracteres} caracteres, no idioma {idioma}, com letras minusculas, sem acentuação, para um jogo da força em nivel {dificuldade}. Essa palavra não pode ser uma dessas: {palavras_usadas_string}. Só responda com a palavra."}]

    response = client.chat.completions.create(
        messages=prompt,
        model="gpt-3.5-turbo-0125",
        max_tokens=1000,
        temperature=0
    )

    with open('palavras_usadas.txt', 'a') as arquivo:
        arquivo.write(response.choices[0].message.content + '\n')
        
    return response.choices[0].message.content
