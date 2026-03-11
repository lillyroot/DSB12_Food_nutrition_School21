import joblib
import pandas as pd
import random
class Ingredient:
    def __init__(self, name):
        self.name_ = name
        self.nutritions = {}

class Recipe:
    def __init__(self, ingredient_list):
        self.ingredient_list_ = ingredient_list

    def get_Forecast(self):
        class_ = None
        model = joblib.load('my_model.pkl')
        new_data = None
        predictions = model.predict(new_data)
        if ( predictions == 0 or predictions == 1 ):
            class_ = 'bad'
        elif ( predictions == 2 or predictions == 3 ):
            class_ = 'so-so'
        else:
            class_ = 'great'

        

    def get_nutrition_facts(self):
        print("II. NUTRITION FACTS")
        daily_nutr = pd.read_csv('data/nutrition_facts.csv')
        for ingredient in self.ingredient_list_:
            mask = daily_nutr['title'].str.contains(ingredient.name_, na=False, case=False)
            if mask.any():
                print(ingredient.name_.capitalize())
                row = daily_nutr[mask].iloc[0]
                for col in daily_nutr.columns:
                    value = row[col]
                    if not isinstance(value, str) and float(value) > 0.0 and not col.lower().startswith('unnamed'):
                        print(f"{col.capitalize()} - {value.round(2)}% of Daily Value")
            print("\n\n")

    
    def get_three_dishes(self):
        print("III. TOP-3 SIMILAR RECIPES:")
        df = pd.read_csv('data/similar_recipes.csv')
        df_full = pd.read_csv('data/epi_r.csv')
        df = pd.merge(df, df_full[['rating']], left_index=True, right_index=True, how='inner')
        similar_df = pd.DataFrame()
        for ingredient in self.ingredient_list_:
            found_df = df[df['title'].str.contains(ingredient.name_, na=False, case=False)]
            similar_df = pd.concat([similar_df, found_df], ignore_index=True)
        for i in range(0,3):
            rand_index = random.randint(0, similar_df.shape[0] - 1)
            row = similar_df.iloc[rand_index]
            print(f"- {row['title']}, rating: {row['rating']}, URL:\n {row['url']}")


#     def set_similar_dishes(ingredient_list):
        

# class Dish:
#     def __init__(self, url, ingredient_list, rating):
#         self.url_ = url
#         self.ingredient_list_ = ingredient_list
#         self.rating_ = rating
#         self.name_ = name

#     def set_URL(self):
#         df = pd.read_csv('data/similar_recipes.csv')
#         return df[self.name]

class Menu:
    def __init__(self):
        self.max_boundary = 1.2
        self.min_boundary = 0.9
        self.menu_list = []

    def generate_menu(self):
        df = pd.read_csv('data/similar_recipes.csv')
        df_full = pd.read_csv('data/epi_r.csv')
        nutritions = pd.read_csv('data/nutrition_facts.csv')

        ingredient_titles = nutritions['title'].tolist()
        df_dish_ingredients = df_full[['title'] + [col for col in df_full.columns if col in ingredient_titles]]
        df_dish_ingredients['title'] = df['title']

        eat_time = ['breakfast', 'lunch', 'dinner']

        for time in eat_time:

            df_time = df_full[df_full[time] == 1.0][['title', 'rating']]
            df_time[nutritions.columns[2:]] = 0.0
            df_time['title'] = df['title']

            for index, row in df_time.iterrows(): #проходимся по строкам блюдо/элементы
                #проходимся по колонкам нужной строки блюдо/ингридиенты
                dish_ingredients_row = df_dish_ingredients[df_dish_ingredients['title'] == row['title']]
                for column in dish_ingredients_row.columns[2:]:
                    if ( dish_ingredients_row[column].iloc[0] == 1.0 ): #если есть ингридиент прибавляем к блюдо/элементы ингридиент/элементы
                        ing_nutrition = nutritions[nutritions['title'] == column]
                        for nut_col in nutritions.columns[2:]:
                            df_time.at[index, nut_col] += ing_nutrition[nut_col].iloc[0]
        
            print(f'-----------------------df_{time}------------------------')
            print(df_time)


        # df_lunch = df_full[df_full['lunch'] == 1.0]
        # print(df_lunch.shape[0])

        
        # df_dinner = df_full[df_full['dinner'] == 1.0]
        # print(df_dinner.shape[0])