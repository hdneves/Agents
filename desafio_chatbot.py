import openai

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

def chat_(mensagem):

    resposta = client.chat.completions.create(
        messages=mensagem,
        model='gpt-3.5-turbo-0125',
        temperature=0,
        max_tokens=10,
        stream=True,
    )

    texto_completo = ''

    for res_stream in resposta:
        texto = res_stream.choices[0].delta.content
        if texto:
            print(texto, end='')
            texto_completo += texto

    mensagem.append({'role': 'assistant', 'content': texto_completo})
    return mensagem


if __name__ == '__main__':

    mensagens = []
    print('Bem-vindo ao chatBot com Python =)')

    while True:
        msg_user = input('User:  ')
        mensagens.append({'role': 'user', 'content': msg_user})
        mensagens = chat_(mensagem=mensagens)
        print('\n\n')#, mensagens)