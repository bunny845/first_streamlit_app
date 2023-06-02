import streamlit
import snowflake.connector
streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hand-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
# new header Update streamlit_app.py
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# use pandas to fetch data from a csv file
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# set fruit col as index
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# multiselect with default selections and store them in variable 
fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# calling fruityvice api
streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# streamlit.text(fruityvice_response.json())
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
streamlit.dataframe(fruityvice_normalized)

# snowflake integration with streamlit
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_cur.execute("insert into my_fruit_list values('from streamlit') ")
streamlit.text("The fruit load list contains:")
my_data_row = my_cur.fetchall()
streamlit.dataframe(my_data_row)

fruit_to_add = streamlit.text_input('What fruit would you like to add?')
streamlit.write(fruit_to_add)

