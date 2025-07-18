
import streamlit as st
from models.recipe_model import SmartRecipeRecommender
from utils.image_fetcher import get_image_by_class


recommender = SmartRecipeRecommender('data/indian_food.csv')

st.set_page_config(page_title="AI Smart Recipe Recommender")
st.title('AI Smart Recipe Recommender')

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
                img_url = get_image_by_class(recipe['URL'])
                if img_url:
                    st.image(img_url, width=300)
                st.markdown(f"**Cuisine:** {recipe['Cuisine']}")
                st.markdown(f"**Time:** {recipe['Time']} mins")
                st.markdown(f"**Ingredients:** {recipe['Ingredients']}")
                st.markdown(f"[View Recipe 🔗]({recipe['URL']})")
                with st.expander("👨‍🍳 Show Instructions"):
                    steps = recipe['TranslatedInstructions'].split('\n')
                    for i, step in enumerate(steps):
                        st.markdown(f"**Step {i+1}:** {step.strip()}")
                st.markdown("---")

with tab2:
    st.subheader("Enter the name of a recipe you like:")
    recipe_names = sorted(recommender.df['TranslatedRecipeName'].unique())
    selected_recipe = st.selectbox("Choose a recipe", recipe_names)

    if st.button("Find Similar Recipes", key='name_button'):
        results = recommender.recommend_by_recipe_name(selected_recipe)

        if isinstance(results, str):
            st.error(results)
        else:
            for recipe in results:
                st.markdown(f"### {recipe['RecipeName']}")
                img_url = get_image_by_class(recipe['URL'])
                if img_url:
                    st.image(img_url, width=300)
                st.markdown(f"**Cuisine:** {recipe['Cuisine']}")
                st.markdown(f"**Time:** {recipe['Time']} mins")
                st.markdown(f"**Ingredients:** {recipe['Ingredients']}")
                st.markdown(f"[View Recipe 🔗]({recipe['URL']})")
                with st.expander("👨‍🍳 Show Instructions"):
                    steps = recipe['TranslatedInstructions'].split('\n')
                    for i, step in enumerate(steps):
                        st.markdown(f"**Step {i+1}:** {step.strip()}")
                st.markdown("---")
