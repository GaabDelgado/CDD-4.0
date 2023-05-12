def texto_quant(texto):
    texto_2=''.join(texto.split())
    return len(texto_2),texto[::-1]
print(texto_quant("Agora você me ve e agora não vê mais."))

#len - lê a quantia de caracteres do texto
#::-1 - inverte meu texto
#.join - substitui tudo que esteja dentro do ''.
#.split - tudo que tiver separação ele coloca em lista(quebra os espaços)