import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
np.random.seed(42)

# Set wide layout
st.set_page_config(layout="wide")

# Reduce top padding and sidebar width using CSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.1rem;
        }
        [data-testid="stSidebar"] {
            width: 100px !important;
            max-width: 100px !important;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar content
st.sidebar.title("Note")
st.sidebar.write("Management Considered- 1,3,4,13,15,16,97")

# Header
st.header('UDISE+ Data Analysis and Visualization: Kolkata')

# ---------- TOP HALF: Two Columns ----------
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Chart of a selected Circle")
        st.write("One of the RTE Parameter: Subject group wise UP teacher")
        #Load data
        #df = pd.read_csv("C:/DataAnalysis/upsch.csv")

        df = pd.read_csv("https://kolkatassm.in/dataVisu/upsch.csv")
        #st.dataframe(df)


        #Sidebar selection
        circle_list = list(df.Circle.unique())
        circle_list1 = circle_list[:-1]
        circle_name = st.selectbox('Select a circle', circle_list1, index=len(circle_list1)-1)



        # Get the data for the selected circle
        selected_circle_data = df[df['Circle'] == circle_name].iloc[0]

        schools_with_teachers = selected_circle_data['No. of schools having tch in all major group']
        schools_without_teachers = selected_circle_data['No. of schools not having tch in all major group']

        labels = ['Schools with all major group teachers', 'Schools without all major group teachers']
        values = [schools_with_teachers, schools_without_teachers]

        # Define colors for the segments
        colors = ['#1f77b4', 'red'] # Using a default blue for the first category and red for the second

        # Create a donut chart using Plotly for the selected circle with specified colors
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4, marker=dict(colors=colors))])

        # Display the chart in Streamlit
        st.plotly_chart(fig)

    with col2:
        st.subheader("District Value: and Chart")
        st.write("One of the RTE Parameter: Subject group wise UP teacher")
        # Filter out the 'District Value' row
        circle_list2=['District Value']
        circle_name1 = st.selectbox('District Graph', circle_list2, index=len(circle_list2)-1)

        selected_District_data = df[df['Circle'] == 'District Value'].iloc[0]

#district_name = df_filtered[df_filtered['Circle']]


#Get the data for the selected circle
#selected_District_data = df[df['Circle'] == district_name].iloc[0]

        schools_with_teachers = selected_District_data['No. of schools having tch in all major group']
        schools_without_teachers = selected_District_data['No. of schools not having tch in all major group']

        labels1 = ['Schools with all major group teachers', 'Schools without all major group teachers']
        values1 = [schools_with_teachers, schools_without_teachers]

        # Define colors for the segments
        colors = ['green', 'yellow'] # Using a default blue for the first category and red for the second

# Create a donut chart using Plotly for the selected circle with specified colors
        fig1 = go.Figure(data=[go.Pie(labels=labels1, values=values1, hole=.4, marker=dict(colors=colors))])

        # Display the chart in Streamlit
        st.plotly_chart(fig1)

# Add vertical spacing to simulate split
#st.markdown("<div style='height: 40vh;'></div>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='height: 8vh; background-color: lightblue; border: 2px solid gray;'>
        <p style='text-align: center; padding-top: 5px;'>Next Section:Next Parameter</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- BOTTOM HALF: Full Width ----------
with st.container():
    st.subheader("Relation of PTR and SCR: and Chart")
    #st.write("This is the full-width bottom section")
    # Load data
    df = pd.read_csv("https://kolkatassm.in/dataVisu/ptr_scr.csv")
#st.dataframe(df)
# Let user pick columns for the X and two Y values
    x_column = st.selectbox("Select X-axis column", df.columns)
    y_column1 = st.selectbox("Select first Y-axis column", df.columns, index=1)
    y_column2 = st.selectbox("Select second Y-axis column", df.columns, index=2)


# Melt the DataFrame for Plotly Express to handle multiple lines
    df_melted = df[[x_column, y_column1, y_column2]].melt(id_vars=x_column, 
                                                          value_vars=[y_column1, y_column2],
                                                          var_name="PTR_Vs_SCR", 
                                                          value_name="Value")

# Create Plotly line chart
    fig2 = px.line(df_melted, x=x_column, y="Value", color="PTR_Vs_SCR",
                  title=f"Line Chart: {y_column1} vs {y_column2}")



# Define custom colors for the two lines
    color_map = {
        y_column1: "red",      # change light green to red
        y_column2: "blue"      # adjust or keep as desired
    }

# Create Plotly line chart with custom colors
    fig2 = px.line(
        df_melted,
        x=x_column,
        y="Value",
        color="PTR_Vs_SCR",
        title=f"Line Chart: {y_column1} vs {y_column2}",
        color_discrete_map=color_map
    )



# Show plot
    st.plotly_chart(fig2)
