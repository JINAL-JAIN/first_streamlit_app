# importing essential libraries
import streamlit
import pandas

# adding title, header and text to the application
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled free-range egg')
streamlit.text(' 🥑🍞 Avocado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
 # loading the csv file
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# filtering the dataframe, using multiselect 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
 # new section to display fruitvise api response 
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
import requests               
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
# take the json version of response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# display the output as a table
streamlit.dataframe(fruityvice_normalized)
