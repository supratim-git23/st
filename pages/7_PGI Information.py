
# this is final  as on 2.5.25

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
np.random.seed(42)


# page width
st.set_page_config(layout="wide")

# Reduce top padding using custom CSS
st.markdown("""
    <style>
        .block-container {
            padding-top: 1.1rem;
        }
            
        [data-testid="stSidebar"] {
        width: 100px !important;   /* Adjust the width as needed */
        max-width: 100px !important;
    }
    </style>
""", unsafe_allow_html=True)

#Example sidebar content
st.sidebar.title("Note")
st.sidebar.write("Management Considered- 1,3,4,13,15,16,97")


#st.title('UDISE+ Data Analysis and Visualization')
st.header('Circle Wise UDISE+ Data Analysis and Visualization: Kolkata District')

# Load data
df = pd.read_csv("https://kolkatassm.in/dataVisu/pgi2.csv")

# Sidebar selection
circle_list = list(df.Circle.unique())
circle_list1 = circle_list[:-1]
circle_name = st.selectbox('Select a circle', circle_list1, index=len(circle_list1)-1)

# Define years and metrics
years = [2023, 2024]
base_metrics = ['training-of-safety-tch-and-std', 'teachers-digital-attendance', 'displayed-safety-guideline', 'handwash-mdm' , 'rainwater-hervesting' , 'health-checkup']

# Get data for selected circle and district
try:
    circle_data = df[df['Circle'] == circle_name].iloc[0]
    district_data = df[df['Circle'] == 'District_average'].iloc[0]
except IndexError:
    st.error("Circle or District data not found.")
    st.stop()

# Custom x-axis labels: (metric, year) pairs
x_labels = []
for metric in base_metrics:
    for year in years:
        x_labels.append(f"{metric.capitalize()} {year}")

# Bar values
circle_values = [circle_data[f"{metric}_{year}"] for metric in base_metrics for year in years]
district_values = [district_data[f"{metric}_{year}"] for metric in base_metrics for year in years]

# Plot
fig = go.Figure()

# Bar chart for circle (hide legend for this trace)
fig.add_trace(
    go.Bar(
        x=x_labels,
        y=circle_values,
        name=circle_name,
        marker_color=['skyblue', 'magenta'] * len(base_metrics),
        showlegend=False  # Hides the legend for the bar chart
    )
)

# Line chart for district (legend will show for this trace)
fig.add_trace(
    go.Scatter(
        x=x_labels,
        y=district_values,
        mode='lines+markers',
        name='District Average',
        line=dict(color='red', width=3),
        marker=dict(color='black', size=9)
    )
)



# Dummy traces for legend
fig.add_trace(
    go.Bar(
        x=[None], y=[None],
        marker_color='skyblue',
        name='2023[2023-24]'
    )
)
fig.add_trace(
    go.Bar(
        x=[None], y=[None],
        marker_color='magenta',
        name='2024[2024-25]'
    )
)

# Layout
fig.update_layout(
    title=f"PGI and Safety Indicators for {circle_name} and District Average (2023-24[2023] vs (2024-25[2024])",
    xaxis_title='Parameter and Year',
    yaxis_title='No. of School',
    barmode='group',  # bars side-by-side
    template='plotly_white',
    width=950,
    height=600,
    xaxis_tickangle=-45
)

# Show in Streamlit
st.plotly_chart(fig)









