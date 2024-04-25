import streamlit as st

st.set_page_config(
    page_title="Fashion Trend Helper",
    page_icon=":bar_chart:"
)

st.title("Fashion Trend Tool")
st.sidebar.success("Select a page above.")

import pandas as pd
import pandas as pd

def load_data():
    try:
        # Here the data function was defined. 
        data = pd.read_csv('/Users/timae/Desktop/fp.csv', delimiter=';')
        #Because it didn't recognize the columns the following was added all of the following with ChatGPT
        print("Data loaded successfully:")
        print(data.head())  # Print the first few rows of the DataFrame
        print("\nDataFrame shape:", data.shape)  # Print the shape of the DataFrame
        print("Column names:", data.columns)  # Print the column names
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except pd.errors.ParserError:
        print("Error parsing the file. Check the delimiter and file format.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Load data function (assuming it's defined elsewhere and works correctly)
data = load_data()  # Make sure this function is correctly returning the DataFrame

# Ensuring that "whitespace and checked"
data.columns = data.columns.str.strip()

# Here we added the filter options to the sidebar
st.sidebar.header('Filter Options')
if 'Brand' in data.columns:
    selected_brand = st.sidebar.multiselect('Brand', options=data['Brand'].unique())
if 'Category' in data.columns:
    selected_category = st.sidebar.multiselect('Category', options=data['Category'].unique())
if 'Price' in data.columns:
    price_min, price_max = st.sidebar.slider('Price Range in USD', int(data['Price'].min()), int(data['Price'].max()), (int(data['Price'].min()), int(data['Price'].max())))
if 'Rating' in data.columns:
    rating_min, rating_max = st.sidebar.slider('Rating', float(data['Rating'].min()), float(data['Rating'].max()), (float(data['Rating'].min()), float(data['Rating'].max())))
if 'Color' in data.columns:
    selected_color = st.sidebar.multiselect('Color', options=data['Color'].unique())
if 'Size' in data.columns:
    selected_size = st.sidebar.multiselect('Size', options=data['Size'].unique())

# Initialize filtered_data as the original DataFrame, don't
filtered_data = data

# Here filters applied for each column of the data
if selected_brand:
    filtered_data = filtered_data[filtered_data['Brand'].isin(selected_brand)]
if selected_category:
    filtered_data = filtered_data[filtered_data['Category'].isin(selected_category)]
if price_min is not None and price_max is not None:  # To make sure both min and max are set
    filtered_data = filtered_data[(filtered_data['Price'] >= price_min) & (filtered_data['Price'] <= price_max)]
if rating_min is not None and rating_max is not None:  # Same as above 
    filtered_data = filtered_data[(filtered_data['Rating'] >= rating_min) & (filtered_data['Rating'] <= rating_max)]
if selected_color:
    filtered_data = filtered_data[filtered_data['Color'].isin(selected_color)]
if selected_size:
    filtered_data = filtered_data[filtered_data['Size'].isin(selected_size)]

# Display results on the web app
for _, row in filtered_data.iterrows():
    st.subheader(row['Product Name'])
    st.write(f"**Brand:** {row['Brand']}")
    st.write(f"**Category:** {row['Category']}")
    st.write(f"**Price:** ${row['Price']}")
    st.write(f"**Rating:** {row['Rating']:.2f} Stars") #this will give you the rating, I added .2f so it's rounded to 2 decimal places
    st.write(f"**Color:** {row['Color']}")
    st.write(f"**Size:** {row['Size']}")
    st.write("---") #this line is to seperate the different results





