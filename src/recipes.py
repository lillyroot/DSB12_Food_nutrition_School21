import joblib
import pandas as pd
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
        class_ = None
        model = joblib.load('my_model.pkl')
        predictions = model.predict(new_data)
        if ( predictions == 0 or predictions == 1 ):
            class_ = 'bad'
        elif ( predictions == 2 or predictions == 3 ):
            class_ = 'so-so'
        else:
            class_ = 'great'

        



    def get_nutrition_facts(self):
        print("II. NUTRITION FACTS")
        for ingredient in self.ingredient_list_:
            print(ingredient.name_)
            for k, v in ingredient.nutritions:
                print(f"{k} - {v}% of Daily Value")

    
    def get_three_dishes(self):
        print("III. TOP-3 SIMILAR RECIPES:")
        for dish in self.similar_dishes:
            print(f"- {dish.dish_name}, rating: {dish.rating}, URL:")
            print(dish.url)


    def set_similar_dishes(ingredient_list):
        

class Dish:
    def __init__(self, url, ingredient_list, rating):
        self.url_ = url
        self.ingredient_list_ = ingredient_list
        self.rating_ = rating
        self.name_ = name

    def set_URL(self):
        df = pd.read_csv('data/similar_recipes.csv')
        return df[self.name]