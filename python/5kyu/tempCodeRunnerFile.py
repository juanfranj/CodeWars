    for key, valor in recipe.items():
            if key in available.keys() and (available[key] - valor) > 0:
                available[key] -= valor
            else:
                ok = False
                break
        if ok:
            pasteles += 1
        print(available)