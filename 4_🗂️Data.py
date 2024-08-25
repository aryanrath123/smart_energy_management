import streamlit as st
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize SQLite database
conn = sqlite3.connect('energy_data.db')
c = conn.cursor()

# Create tables if they don't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS energy_data (
        region TEXT,
        wind_energy REAL,
        hydro_energy REAL,
        extra_energy_needed REAL,
        net_energy REAL
    )
''')
conn.commit()

css_styles = """
<style>
    .main {
        border: 50px solid #000;
        border-radius: 50px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-color: black;
    }
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)


main_div = st.container()
with main_div:
    st.title("Energy Data Collection for Indian Regions")

# Energy Data Collection Form
with st.form("energy_form"):
    region = st.selectbox("Select the region", ["North", "South", "East", "West", "North East", "South West"])
    wind_energy = st.number_input("Enter Wind Energy (in MW)", min_value=0.0)
    hydro_energy = st.number_input("Enter Hydro Energy (in MW)", min_value=0.0)
    extra_energy_needed = st.number_input("Enter Extra Energy Needed (in MW)", min_value=0.0)
    net_energy = st.number_input("Enter Net Energy (in MW)", min_value=0.0)

    submit_button = st.form_submit_button("Submit")

if submit_button:
    # Insert data into the database
    c.execute("INSERT INTO energy_data (region, wind_energy, hydro_energy, extra_energy_needed, net_energy) VALUES (?, ?, ?, ?, ?)",
              (region, wind_energy, hydro_energy, extra_energy_needed, net_energy))
    conn.commit()
    st.success("Data submitted successfully!")

# Data Visualization Section


# Load data from the database
df = pd.read_sql_query("SELECT * FROM energy_data", conn)

# if not df.empty:
#     st.subheader("Bar Plot: Energy Distribution by Region")
#     fig, ax = plt.subplots()
#     sns.barplot(x='region', y='net_energy', data=df, ax=ax)
#     st.pyplot(fig)

#     st.subheader("Scatter Plot: Wind Energy vs Hydro Energy")
#     fig, ax = plt.subplots()
#     sns.scatterplot(x='wind_energy', y='hydro_energy', hue='region', data=df, ax=ax)
#     st.pyplot(fig)

#     st.subheader("Line Plot: Extra Energy Needed by Region")
#     fig, ax = plt.subplots()
#     sns.lineplot(x='region', y='extra_energy_needed', data=df, ax=ax)
#     st.pyplot(fig)
# else:
#     st.write("No data available yet.")
css_styles = """
<style>

    {
        font-size: 28px; 
    }
    body {
        border: 50px solid #000;
        border-radius: 50px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-color: white}

    
    [data-testid="stHeader"] {
        font-size: 30px; 
    }
    [data-testid="stForm"] label {
        font-size: 50px; 
        
    }
[data-testid="stAppViewContainer"]{
    background-color: white;
    opacity: 0.8;
    background-image: url("https://images.unsplash.com/photo-1631088902967-8bc33c083d66?q=80&w=2074&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;
    border: 5px solid #000;
}
[data-testid="stAppViewContainer"]{
    border: 3px solid #000;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
[data-testid="stForm"] {
    color: #eae5e5;
}
[data-testid="stForm"] label {
    color: #eae5e5;
}
[data-testid="stForm"] input[type="number"] {
    color: #eae5e5;
}
[data-testid="stForm"] select {
    color: #eae5e5;
}
</style>
"""

st.markdown(css_styles, unsafe_allow_html=True)


# # Close the database connection
conn.close()
