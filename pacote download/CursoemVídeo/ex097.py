def escreva(mensagem):
    tamanho = len(mensagem) + 4
    print('~'*tamanho)
    print(f"  {mensagem}")
    print('~'*tamanho)


escreva("Curso de Python")
escreva("Curso em Vídeo")