spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return[food["name"] for food in spicy_foods]
    pass

def get_spiciest_foods(spicy_foods):
    return[food for food in spicy_foods if food.get("heat_level") > 5 in spicy_foods]
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food['name']
        cuisine = food['cuisine']
        heat_level = food['heat_level']
        emoji = '🌶' * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {emoji}")
    

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get('cuisine') == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food.get("heat_level", 0) > 5:
            name = food['name']
            cuisine = food['cuisine']
            heat_level = food['heat_level']
            emoji = "🌶" * heat_level
            print(f'{name} ({cuisine}) | Heat Level: {emoji}')
    

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food.get('heat_level') for food in spicy_foods)
    spicy_lenght = len(spicy_foods)

    if spicy_lenght == 0:
        return 0

    return total_heat_level / spicy_lenght

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods