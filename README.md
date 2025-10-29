# Food and nutrition

Summary: This rush will help you to strengthen the skills acquired over the previous days.

💡 [Tap here](https://new.oprosso.net/p/4cb31ec3f47a4596bc758ea1861fb624) **to leave your feedback on the project**. It's anonymous and will help our team make your educational experience better. We recommend completing the survey immediately after the project.

## Contents

1. [Chapter I](#chapter-i) \
    1.1. [Foreword](#foreword)
2. [Chapter II](#chapter-ii) \
    2.1. [Instructions](#instructions)
3. [Chapter III](#chapter-iii) \
    3.1. [Specific instructions for the day](#specific-instructions-for-the-day)
4. [Chapter IV](#chapter-iv) \
    4.1. [Mandatory part](#mandatory-part)
5. [Chapter V](#chapter-v) \
    5.1. [Bonus part](#bonus part)
6. [Chapter VI](#chapter-vi) \
    6.1. [Submission and peer-evaluation](#submission-and-peer-evaluation)

## Chapter I

### Foreword

You are what you eat. Think of your body as a system that needs many different nutrients to live a happy, healthy life. Without the proper nutrients, important chemical reactions may stop occurring, which can lead to health problems.

To live healthily, your diet should be balanced. You need proteins, carbohydrates, and fats, as well as Fe, Mg, Na, K, Ca, Zn, Se, Cr, and I. You also need vitamins D, B12, E, C, A, and K, as well as Cu. This is a long list, but it's far from exhaustive. If you don't consume enough protein, your body will start breaking down your muscles, organs, and tissues to get it. Eventually, you will lack certain enzymes, hormones, transport proteins, and immune cells. Eating too much of these nutrients can intoxicate your body with decaying materials, which will decrease your health. This applies to any item on the list. "Everything is poisonous, and nothing is without poison. The dosage makes it either a poison or a remedy".

The first problem is that our diet is not as diverse as it should be.
If we are talking about the average person in the Western world, that is. How often do you eat vegetables, fruits, nuts, beans, berries, bread, pastries, fish, meat, seaweed, and butter? How often do you drink coffee, green tea, milk, alcohol, juice, and smoothies?

The second problem is that we like tasty food, and none of this healthy food tastes as good as fried potatoes, chips, etc. The third problem is that we don't know enough good recipes.

What if we had an app that could predict how tasty a dish could be with the ingredients currently in our refrigerator and recommend recipes that are both healthy and tasty?

## Chapter II

### Instructions

* Use this page as your only reference. Do not pay attention to rumors or speculation about how to prepare your solution.
* Here and throughout, we use Python 3 as the only correct version of Python.
* The python files for python exercises (module01, module02, module03) must have the following block at the end: `if __name__ == ‘__main__’`.
* Pay attention to the permissions of your files and directories.
* To be assessed your solution must be in your GIT repository.
* Your solutions will be evaluated by your peers in the bootcamp.
* You should not leave any other files in your directory other than those explicitly specified in the exercise instructions. It is recommended that you modify your .gitignore to avoid any accidents.
* Your solution must be in your GIT repository for evaluation. Always push only to the develop branch! The master branch will be ignored. Work in the src directory.
* When you need to get precise output in your programs, it is forbidden to display a precalculated output instead of performing the exercise correctly.
* Have a question? Ask your neighbor on the right. If that fails, try your neighbor on the left.
* Your reference materials are your peers, the internet, and Google.
* Read the examples carefully. They may require information that is not specified elsewhere in the subject.
* May the Force be with you!

## Chapter III

### Specific instructions for the day

* No code in the global scope of the main program. Use the classes and methods that you have written in the development stage!
* Any exception not caught will invalidate your work, even in the event of an error that you were asked to test.
* The interpreter to use is Python 3.
* All built-in functions are is allowed.

## Chapter IV

### Mandatory part

Today, you will work on your own application to help people eat healthier and tastier food. Creating a product prototype using the technologies you have studied is valuable experience. You will achieve great results in just two weeks of Python and data science training!

Your work will have three stages: research (working in a notebook), development (organizing everything in a module with classes and methods), and programming
(Python script). Each stage will produce corresponding files.

#### Main program

Let's start from the end. The program is a Python script (```nutritionist.py```).

* It takes in a list of ingredients.
* It forecasts and returns the rating class (bad, so-so, or great) of a potential dish containing the ingredients.
* It finds and returns all the nutrients (proteins, fats, sodium, etc.) in the ingredients, as well as their daily values as a percentage.
* It finds the three most similar recipes to the list of ingredients, their ratings, and the URLs where users can find full details.

Here is an example:

```
$ ./nutritionist.py milk, honey, jam
I. OUR FORECAST
You might find it tasty, but in our opinion, it is a bad idea to have a
dish with that list of ingredients.
II. NUTRITION FACTS
Milk
Protein - 6% of Daily Value
Total Carbohydrate - 1% of Daily Value
Total Fat - 1% of Daily Value
Calcium - 12% of Daily Value
...
Honey
...
Jam
...
III. TOP-3 SIMILAR RECIPES:
- Strawberry-Soy Milk Shake, rating: 3.0, URL:
https://www.epicurious.com/recipes/food/views/strawberry-soy-milk-
shake-239217
- ...
- ...
```

#### Development

You need to create a Python module (```recipes.py```) with the classes and
methods that are used in the main script.

#### Research

In this part of the Bootcamp, you need to prepare everything that is used
in the classes and methods above in a Jupyter Notebook (`recipes.ipynb`).

* Forecast
  * Data Preparation 
    * Use the [Epicurious dataset](https://drive.google.com/file/d/1hzmxNBrY7-9mv5EpqAvhVUiJahfrcYUN/view?usp=sharing) collected by HugoDarwood.
    * Filter the columns; the fewer non-ingredient columns in your dataset, the better. You will predict the rating or rating category using only the ingredients. 
  * Regression 
    * Try different algorithms and their hyperparameters for rating prediction. Select the best one based on cross-validation and determine the score (RMSE) using the test subsample. 
    * Try different ensembles and their hyperparameters. Select the best one using cross-validation and calculate the RMSE on the test subsample. 
    * Calculate the RMSE for a naive regressor that predicts the average rating. 
  * Classification 
    * Binarize the target column by rounding the ratings to the closest integer. These will be your classes. 
    * Try different algorithms and their hyperparameters for class prediction. Select the best algorithm based on cross-validation and determine the accuracy score on the test subsample. 
    * Compare the metrics using accuracy. Calculate the accuracy of a naïve classifier that predicts the most common class.
    * Binarize the target column by converting the integers to the following classes: “bad” (0, 1), “so-so” (2, 3), and “great” (4, 5). 
    * Try different algorithms and their hyperparameters for class prediction. Select the best algorithm using cross-validation and determine the score on the test subsample. 
    * Compare the metrics using accuracy. Calculate the accuracy of a naïve classifier that predicts the most common class. 
    * What is worse: predicting a bad rating that is actually good or predicting a good rating that is actually bad? Replace accuracy with the appropriate metric. 
    * Try different algorithms and their hyperparameters for class prediction with the new metric. Select the best algorithm and find its score on the test subsample. 
    * Try different ensembles and their hyperparameters. Select the best one and find its score on the test subsample.
  * Decision
    * Decide whether to use the regression model or the classification model. Save the best model. You will use it in the program.
* Nutrition Facts
  * Collect all the nutrition facts for the ingredients from your prepared and filtered dataset (only ingredient columns) into a data frame. Use [the following API](https://fdc.nal.usda.gov/api-guide.html) for that.
  * Transform all the values into a percentage of the daily value. Keep only nutrients that exist in [this](https://drive.google.com/file/d/1jn0t5tU_RgOpq4wcO-uS4D0_NAP6MwHz/view?usp=sharing) and [that](https://drive.google.com/file/d/1bmdZGB0QwND2BD3XlC1JswL7AdnTJHLT/view?usp=sharing) table. 
  * Save the transformed dataframe to a CSV file that you will use in your main program.
* Similar Recipes 
  * For each recipe in the dataset, collect the URL from epicurious.com with its details. If there is no URL for a recipe, skip it.
  * Save the new dataframe to a CSV file that you will use in your main program.

## Chapter V

### Bonus part

Add more methods to the classes to help the script perform a new function: generating a daily menu.

The daily menu should randomly provide a list of three recipes that cover most nutritional needs (percent of daily value) without exceeding them, and that have the highest total rating.

Only offer recipes appropriate for breakfast, lunch, and dinner, respectively.

The program's output should resemble this:

```
BREAKFAST
---------------------
Feta, Spinach, and Basil Omelette Muffins (rating: 4.375)
Ingredients:
- arugula
- egg
- feta
- muffin
- omelet
- spinach
- tomato
Nutrients:
- protein: 16%
- fat: 10%
- sodium: 7 %
- ...
URL: https://www.epicurious.com/recipes/food/views/feta-spinach-and-basil-omelette-muffins
LUNCH
---------------------
...
```

## Chapter VI

### Submission and peer-evaluation

Submit your work using your Git repository as usual.

Only work in your repository will be graded during the evaluation.

You will be evaluated on both your submission and your ability to present, explain, and justify your choices during the evaluation.

