def save_to_txt(itens):
    with open('saida.txt','w') as f:
        f.write('{}\n'.format(itens))