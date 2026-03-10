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
                        print(f"{col.capitalize()} - {value.round()}% of Daily Value")
            print("\n\n")

    
    def get_three_dishes(self):
        print("III. TOP-3 SIMILAR RECIPES:")
        df = pd.read_csv('data/similar_recipes.csv')
        df_full = pd.read_csv('data/epi_r.csv')
        similar_df = pd.DataFrame()
        for ingredient in self.ingredient_list_:
            found_df = df[df['title'].str.contains(ingredient.name_, na=False, case=False)]
            similar_df = pd.concat([similar_df, found_df], ignore_index=True)
        similar_df = pd.merge(similar_df, df_full[['rating']], left_index=True, right_index=True, how='inner')
        print(similar_df)
        for i in range(0,3):
            rand_index = random.randint(0, similar_df.shape[0] - 1)
            row = similar_df.iloc[rand_index]
            print(f"- {row['title']}, rating: {row['rating']}, URL: {row['url']}")


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