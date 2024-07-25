def todos_preenchidos(objeto):
    for item in objeto.values():
        if item == '' or None :
            print('Preencha todos os campos')
            break