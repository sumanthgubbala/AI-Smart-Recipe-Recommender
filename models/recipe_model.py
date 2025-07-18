
import pandas as pd
from sklearn.feature_extraction.text  import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SmartRecipeRecommender:

    def __init__(self,csv_path):
        
        self.df = pd.read_csv(csv_path)

        self.vectorizer = TfidfVectorizer()
        self.tifdf_matrix = self.vectorizer.fit_transform(self.df['Cleaned-Ingredients'])

        self.similarity_matrix = cosine_similarity(self.tifdf_matrix)
    
    def recommend_by_ingredients(self,ingredients_list,top_n=5):

        user_input = ' '.join(ingredients_list).lower()
        user_vector = self.vectorizer.transform([user_input])

        sim_scores = cosine_similarity(user_vector,self.tifdf_matrix).flatten()
        top_indices = sim_scores.argsort()[-top_n:][::-1]

        recommendations = []
        for idx in top_indices :

            row = self.df.loc[idx]
            recommendations.append({
                'RecipeName': row['TranslatedRecipeName'],
                'Cuisine': row['Cuisine'],
                'Time': row['TotalTimeInMins'],
                'Ingredients': row['Cleaned-Ingredients'],
                'URL': row['URL'],
                'TranslatedInstructions': row['TranslatedInstructions']
            })
        
        return recommendations
    
    def recommend_by_recipe_name(self,recipe_name,top_n=5):

        if recipe_name not in self.df['TranslatedRecipeName'].values:
            return f"'{recipe_name}' not found in dataset."
        
        idx = self.df[self.df['TranslatedRecipeName'] == recipe_name].index[0]

        sim_scores = list(enumerate(self.similarity_matrix[idx]))
        sim_scores = sorted(sim_scores,key= lambda x: x[1], reverse=True)[1:top_n+1]

        recommendations = []
        for i, score in sim_scores:
            row = self.df.iloc[i]
            recommendations.append({
                'RecipeName': row['TranslatedRecipeName'],
                'Cuisine': row['Cuisine'],
                'Time': row['TotalTimeInMins'],
                'Ingredients': row['Cleaned-Ingredients'],
                'URL': row['URL'],
                'TranslatedInstructions': row['TranslatedInstructions']
            })
        return recommendations