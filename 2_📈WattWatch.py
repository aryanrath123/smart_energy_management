import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns
import webbrowser

st.header("📈 Watt Watch")
st.subheader("Visualizing the Shifts in Energy Consumption Patterns Across Indian Regions")
st.divider()

conn = sqlite3.connect('energy_data.db')
c = conn.cursor()

p1="""
    ⚡️AI Integration \n
    ⚡️Predictive Energy Requirements\n
    ⚡️Real Time Info. Mapping\n
    ⚡️Automated Database Integration\n
    ⚡️Electric Tempering Report System\n
    ⚡️Energy Consumption Forecasting\n
    ⚡️Smart Meter API Integration\n

"""
st.sidebar.header("🔖Features")
st.sidebar.write(p1)


# Setting up the Tabs
tab1, tab2 = st.tabs(["Real Time", "Available"])

## Display from database
with tab1:
    df = pd.read_sql_query("SELECT * FROM energy_data", conn)
    d = pd.DataFrame(df)
    x, space, y = st.columns((1, 0.4, 1))
    a, b, c = st.columns(3)
    x.line_chart(d)
    y.bar_chart(d)
    x.area_chart(d)
    df = pd.read_csv('d1.csv')
    df1 = pd.read_csv('d2.csv')
    y.table(df1.iloc[0:10])
    d = pd.DataFrame(df)
    a, b, c = st.columns(3)
    st.divider()

    # Allow the user to select columns for the charts
    columns = st.multiselect("Select columns for the charts:", df.columns.tolist())

    # Check if the user has selected any columns
    if columns:
        # Plotting a Line Chart
        x.write("Trend Variations:")
        x.line_chart(df[columns])

        # Plotting an Area Chart
        st.write("Energy Variation Chart:")
        st.area_chart(df[columns])

        # Plotting a Bar Chart
        st.write("Bar Chart:")
        st.bar_chart(df[columns])
    else:
        st.write("Please select at least one column to display the charts.")
css_styles = """
<style>
    .main {
        border: 60px solid #000;
        border-radius: 50px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
        padding: 20px;
        border-color: black;
    }
</style>
"""
## Display from dataset/dataframe
## Display from dataset/dataframe
if st.button("Let's Talk!🤖"):
    
    webbrowser.open('https://aryanrath123.github.io/AI-chatbot/')


with tab2:
    # Load the CSV file
    p="""
    This component of the Watt Watch project enables users to visualize energy consumption patterns across Indian regions in real-time and from available datasets. Users can select specific columns to display in various charts, including line, area, and bar charts. Additionally, users can choose to view energy usage by region or state, providing a more detailed understanding of energy consumption trends
    
    """
    df = pd.read_csv('d2.csv')

    # Display the dataframe
    st.markdown("This component of the Watt Watch project enables users to visualize energy consumption patterns across Indian regions in real-time and from available datasets. Users can select specific columns to display in various charts, including line, area, and bar charts. Additionally, users can choose to view energy usage by region or state, providing a more detailed understanding of energy consumption trends")
    st.write("Data from Real Time:")
    # st.dataframe(df)

    # Allow the user to select columns for the x-axis
    x_axis = st.selectbox("Select the column for the x-axis:", ['Regions', 'States'])

    # Check if the user has selected the x-axis
    if x_axis:
        # Create a new dataframe with the selected column and 'Usage'
        df_selected = df[[x_axis, 'Usage']]

        # Group the dataframe by the selected column and calculate the sum of 'Usage'
        df_grouped = df_selected.groupby(x_axis)['Usage'].sum().reset_index()

        p, spac, q = st.columns(3)
        # Plotting a Line Chart
        p.write(f"{x_axis} vs Usage Line Chart:")
        p.line_chart(df_grouped.set_index(x_axis))

        # Plotting a Bar Chart
        q.write(f"{x_axis} vs Usage Bar Chart:")
        q.bar_chart(df_grouped.set_index(x_axis))
    else:
        st.write("Please select a column for the x-axis to display the charts.")
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
    opacity: 0.8;
    background-image: url("https://images.unsplash.com/photo-1629380072722-725fa5fdcfec?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
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

# Close the database connection
conn.close()