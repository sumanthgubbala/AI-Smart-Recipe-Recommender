
from models.recipe_model import SmartRecipeRecommender


recommender = SmartRecipeRecommender('data/indian_food.csv')


print(recommender.recommend_by_ingredients(['potato', 'onion', 'garlic'], top_n=3))