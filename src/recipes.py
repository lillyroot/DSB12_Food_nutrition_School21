import joblib
import pandas as pd
import random
import time as tm
import numpy as np
class Ingredient:
    def __init__(self, name):
        ingredients = pd.read_csv('data/nutrition_facts.csv')['title'].to_list()
        if name in ingredients:
            self.name_ = name
        else:
            raise ValueError('Unknown ingredient typed')

class Recipe:
    def __init__(self, ingredient_list):
        self.ingredient_list_ = ingredient_list

    def get_forecast(self):
        print("I. OUR FORECAST")
        model = joblib.load('data/best_classification_model.pkl')
        feature_names = model.feature_names_in_.tolist()
        X_new = pd.DataFrame(0, index=[0], columns=feature_names)
        for ing in self.ingredient_list_:
            ing_clean = ing.name_.strip().lower()
            if ing_clean in feature_names:
                X_new.at[0, ing_clean] = 1
        pred = model.predict(X_new)[0]
        if ( pred == 0 ):
            print('You might find it tasty, but in our opinion, it is a bad idea to have a dish with that list of ingredients')
        elif ( pred == 1 ):
            print('Not bad, not great — just a forgettable so-so experience.')
        elif ( pred == 2 ):
            print('Wow! This combination is a masterpiece. We are sure this dish will be absolutely great!')

    def get_nutrition_facts(self):
        print("II. NUTRITION FACTS")
        daily_nutr = pd.read_csv('data/nutrition_facts.csv')
        for ingredient in self.ingredient_list_:
            mask = daily_nutr['title'].str.contains(ingredient.name_, na=False, case=False)
            if mask.any():
                print(ingredient.name_.capitalize())
                row = daily_nutr[mask].iloc[0]
                flag = True
                for col in daily_nutr.columns:
                    value = row[col]
                    if not isinstance(value, str) and float(value) > 0.0 and not col.lower().startswith('unnamed'):
                        print(f"{col.capitalize()} - {value.round(2)}% of Daily Value")
                        flag = False
            if flag: 
                print("\nNo nutrients found...")
            print("\n\n")

    def get_three_dishes(self):
        print("III. TOP-3 SIMILAR RECIPES:")
        df = pd.read_csv('data/similar_recipes_new.csv')
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

class Menu:
    def __init__(self):
        self.max_boundary = 100
        self.min_boundary = 50
        self.menu_list = []

    def generate_menu(self):
        df = pd.read_csv('data/similar_recipes_new.csv')
        df_full = pd.read_csv('data/epi_r.csv')
        nutritions = pd.read_csv('data/nutrition_facts.csv')
        all_combinations = []
        ingredient_titles = nutritions['title'].tolist()
        df_dish_ingredients = df_full[['title'] + [col for col in df_full.columns if col in ingredient_titles]]
        df_dish_ingredients['title'] = df['title']
        # df_dish_ingredients.to_csv('data/dish_ingridient_new.csv')
        eat_time = ['breakfast', 'lunch', 'dinner']
        df_list = []

        # Создаётся датафреймы по завтраку, обеду и ужину
        # for time in eat_time:
        #     df_time = df_full[df_full[time] == 1.0][['title', 'rating']]
        #     df_time[nutritions.columns[1:]] = 0.0
        #     df_time['title'] = df['title']
        #     df_time = df_time[df_time['rating'] > 4.0]
        #     for index, row in df_time.iterrows(): #проходимся по строкам блюдо/элементы
        #         #проходимся по колонкам нужной строки блюдо/ингридиенты
        #         dish_ingredients_row = df_dish_ingredients[df_dish_ingredients['title'] == row['title']]
        #         for column in dish_ingredients_row.columns[2:]:
        #             if ( dish_ingredients_row[column].iloc[0] == 1.0 ): #если есть ингридиент прибавляем к блюдо/элементы ингридиент/элементы
        #                 ing_nutrition = nutritions[nutritions['title'] == column]
        #                 for nut_col in nutritions.columns[1:]:
        #                     df_time.at[index, nut_col] += ing_nutrition[nut_col].iloc[0]
        #     print(f'-----------------------df_{time}------------------------')
        #     print(df_time)
        #     df_time.to_csv(f'data/{time}.csv')
        #     df_list.append(df_time.sample(frac=1))
        
        # df_list = [df.reset_index(drop=True) for df in df_list]
        df_list = [df.reset_index(drop=True) for df in [pd.read_csv('data/breakfast.csv').sample(frac=1), pd.read_csv('data/lunch.csv').sample(frac=1), pd.read_csv('data/dinner.csv').sample(frac=1)]]
        pd.concat([df_list[0], df_list[1], df_list[2]], ignore_index=True).to_csv('data/dish_nutr.csv')
        # print(df_list)

        arrays = []
        titles = []
        for df in df_list:
            list_ = (df.iloc[:, 4:] > 0.0).sum().sort_values(ascending=False).index.to_list()[0:10]#10 самых популярных нутриента
            df = df[['title'] + list_]   
            numeric_data = df.iloc[:, 2:].values
            arrays.append(numeric_data)
            titles.append(df['title'].values)
        n1, n2, n3 = len(arrays[0]), len(arrays[1]), len(arrays[2])
        n_features = arrays[0].shape[1]
        min_target = np.full(n_features, self.min_boundary)
        max_target = np.full(n_features, self.max_boundary)
        
        found = False
        for i1 in range(n1):
            if found: break
            row1 = arrays[0][i1]
            for i2 in range(n2):
                if found: break
                row2 = arrays[1][i2]
                partial_sum = row1 + row2
                for i3 in range(n3):
                    if found: break
                    row3 = arrays[2][i3]
                    print(f"{i1} {i2} {i3}")
                    total_sum = partial_sum + row3
                    
                    if np.all((total_sum >= min_target) & (total_sum <= max_target)):
                        self.menu_list.append(titles[0][i1])
                        self.menu_list.append(titles[1][i2])
                        self.menu_list.append(titles[2][i3])
                        found = True

    def print_menu(self):
        dish_ing_df = pd.read_csv('data/dish_ingridient.csv')
        dish_nutr_df = pd.read_csv('data/dish_nutr.csv')
        print('BREAKFAST\n---------------------\n')
        breakfast = self.menu_list[0]
        print(f"{breakfast} (rating: {dish_nutr_df[dish_nutr_df['title'] == breakfast].iloc[0]['rating']})\n")
        print_ingredients(breakfast)
        print_dish_nutr(breakfast)
        print('LUNCH\n---------------------\n')
        lunch = self.menu_list[1]
        print(f"{lunch} (rating: {dish_nutr_df[dish_nutr_df['title'] == lunch].iloc[0]['rating']})\n")
        print_ingredients(lunch)
        print_dish_nutr(lunch)
        print('DINNER\n---------------------\n')
        dinner = self.menu_list[2]
        print(f"{dinner} (rating: {dish_nutr_df[dish_nutr_df['title'] == dinner].iloc[0]['rating']})\n")
        print_ingredients(dinner)
        print_dish_nutr(dinner)

def print_ingredients(dish):
    print('Ingredients:\n')
    dish_ing_df = pd.read_csv('data/dish_ingridient.csv')
    dish_ing_row = dish_ing_df[dish_ing_df['title'] == dish]
    for column in dish_ing_row.columns[2:]:
        if dish_ing_row[column].iloc[0] == 1.0:
            print(f"- {column}\n")

def print_dish_nutr(dish):
    print('Nutrients:\n')
    dish_nutr_df = pd.read_csv('data/dish_nutr.csv')
    row = dish_nutr_df[dish_nutr_df['title'] == dish].iloc[0]
    for col in row.index:
        value = row[col]
        if not isinstance(value, str) and float(value) > 0.0 and not col.lower().startswith('unnamed') and not col.lower().startswith('rating'):
            print(f"{col.capitalize()} - {value.round(2)}%")
