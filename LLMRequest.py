import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("openai_key"),
)


def getChapters(tema):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system", "content":"""
                Você é um assistente que ajuda na criação de livros digitais.
            """},
            {"role":"user", "content":f"Imagine que vc está escrevendo um livro com o tema:{tema}, crie uma lista de capitulos para esse livro"}]
    )
    return completion.choices[0].message

