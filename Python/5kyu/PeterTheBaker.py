def cakes(recipe, available):

    cake_count = 0

    ingredients = []

    for x in recipe:
        if x not in available.values():
            return 0
        
        ingredients.append(int(available[x] / recipe[x]))

    return min(ingredients)