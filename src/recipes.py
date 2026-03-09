import joblib

class Ingredient:
    def __init__(self, name):
        self.name_ = name
        self.nutritions = {}

    # def get_nutrition(self) - Все вещества из API
    # def to_daily_percentage(self) - преобразовать в % от суточной нормы

class Recipe:
    def __init__(self, ingredient_list):
        self.ingredient_list_ = ingredient_list
        self.similar_dishes = []

    def get_Forecast(self):
        model = joblib.load('my_model.pkl')
        predictions = model.predict(new_data)

    def get_nutrition_facts(self):
        print("II. NUTRITION FACTS")
        for ingredient in self.ingredient_list_:
            print(ingredient.name_)
            for k, v in ingredient.nutritions:
                print(f"{k} - {v}% of Daily Value")

    
    def get_three_dishes(self):
        print("III. TOP-3 SIMILAR RECIPES:")
        for i in range(0,3):
            
        for dish in self.similar_dishes:
            print("- Strawberry-Soy Milk Shake, rating: 3.0, URL:
            print("https://www.epicurious.com/recipes/food/views/strawberry-soy-milk-shake-239217")

    #def get_nutrients_by_dish(recipe) - Вернуть все элементы и их процент по отношению к суточной норме

    def set_similar_dishes(ingredient_list):


class Dish:
    def __init__(self, url, ingredient_list, rating):
        self.url_ = url
        self.ingredient_list_ = ingredient_list
        self.rating_ = rating