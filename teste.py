def lista_random(tamanho = 50):
    lista = []

    for i in range(tamanho):
        sub_lista = []

        for i in range(12):
            sub_lista.append(random.randint(1, 50))
        lista.append(sub_lista)

    return lista