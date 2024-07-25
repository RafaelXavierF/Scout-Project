def todos_preenchidos(evt):
    for item in evt.values():
        if item == '' or None :
            return False
    return True