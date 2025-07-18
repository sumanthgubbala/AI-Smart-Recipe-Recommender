
import streamlit as st
from models.recipe_model import SmartRecipeRecommender

recommender = SmartRecipeRecommender('data/indian_food.csv')

st.set_page_config(page_title="Smart Recipe Recommender")
st.title(' Smart Recipe Recommender')

tab1, tab2 = st.tabs(["🔍 By Ingredients", "📖 By Recipe Name"])


with tab1:

    st.subheader("Enter ingredients you have (comma-separated):")

    user_input = st.text_input("Example: onion, tomato, garlic")

    if st.button("get recipes", key="ingredients_button"):

        ingredients = [i.strip() for i in user_input.split(',')]

        if ingredients :

            results = recommender.recommend_by_ingredients(ingredients)

            for recipe in results:

                st.markdown(f"### {recipe['RecipeName']}")
                st.markdown(f"**Cuisine:** {recipe['Cuisine']}")
                st.markdown(f"**Time:** {recipe['Time']} mins")
                st.markdown(f"**Ingredients:** {recipe['Ingredients']}")
                st.markdown(f"[View Recipe 🔗]({recipe['URL']})")
                st.markdown("---")

with tab2:
    st.subheader("Enter the name of a recipe you like:")
    recipe_name = st.text_input("Example: Aloo Gobi")