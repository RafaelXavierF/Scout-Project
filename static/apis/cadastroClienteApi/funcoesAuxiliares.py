def todos_preenchidos(evt: dict):
    for item in evt.values():
        if item == '' or None :
            return False
    return True

def formata_retorno():
    print()