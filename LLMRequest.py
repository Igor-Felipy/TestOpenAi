import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("openai_key"),
)

def getBookContent(tema):
    chapters_name = getChaptersName(tema)
    chapters_content = []
    for n in chapters_name:
        chapters_content.append(getChaptersContent(tema,n))
    return [chapters_name,chapters_content]


def getChaptersName(tema):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"""
                Você é um assistente que ajuda na criação de livros digitais.
            """},
            {"role":"user", "content":f"""
             Imagine que vc está escrevendo um livro com o tema:{tema}, crie uma lista de capitulos para esse livro,
             A lista deve estar seguindo o seguinte formato: ['tema1','tema2','tema3','tema4'],
             Não retorne nenhuma quebra de linha,
             retorne no mínimo 8 capitulos"""}]
    )
    print(completion.choices[0].message.content)
    return clean_list(completion.choices[0].message.content)



def getChaptersContent(tema,titulo):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"""
                Você é um assistente que ajuda na criação de livros digitais.
            """},
            {"role":"user", "content":f"""
             Imagine que vc está escrevendo um livro com o tema:{tema},
             Escreva um capitulo onde o titulo é {titulo},
             O capitulo deve conter entre 1000 e 1500 palavras,
             Retorne apenas o texto dos paragrafos sem o titulo do capitulo,
             não retorne o titulo no inicio do texto"""}]
    )
    print(completion.choices[0].message.content)
    return completion.choices[0].message.content

def clean_list(ch_list):
    ch_list.replace("\n","")
    ch_list.replace("\t","")
    ch_list.replace("\n8","")
    ch_list.replace("\n12","")
    ch_list.replace(", ",",")
    return ch_list

