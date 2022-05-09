import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Mom\'s New Healthy Diner") 
streamlit.header('Breakfast Favorites')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list= my_fruit_list.set_index('Fruit')
#Let's put a pick list here so they can pick the fruit they want to include

streamlit.write("The user entered",fruit_choice )

#import requests
fruityvice_response= requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#Take the json format of the data and normalize it 
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#output the data as table
streamlit.dataframe(fruityvice_normalized)

stremlit.stop()
#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit=streamlit.text_input("What fruit would you like to add?","jackfruit")
streamlit.write("Thanks for adding",add_my_fruit )

my_cur.execute("insert into pc_rivery_db.public.fruit_load_list values ('from streamlit')")
