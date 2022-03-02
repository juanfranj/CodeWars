def cakes(recipe, available):
    pasteles = 0
    ok = True
    while ok:
        for key, valor in recipe.items():
            if key in available.keys() and (available[key] - valor) >= 0:
                available[key] -= valor
            else:
                ok = False
                break
        if ok:
            pasteles += 1
    return pasteles

if __name__ == '__main__':
    recipe = {'cream': 1, 'flour': 3, 'sugar': 1, 'milk': 1, 'oil': 1, 'eggs': 1}
    available = {'sugar': 1, 'eggs': 1, 'flour': 3, 'cream': 1, 'oil': 1, 'milk': 1}
    print(cakes(recipe, available))
'''
   def cakes(recipe, available):
    return min(available.get(k, 0)/recipe[k] for k in recipe)

'''
 