import streamlit as st
import pandas as pd

#Frontend using streamlit.
df = pd.read_csv("./projects.csv")
st.title(":blue[Dylan and Parin ML projects]")
st.dataframe(df)
selected_project = st.selectbox(
    "Select a project",
    options= df["name"]
)
project_details = df[df['name'] == selected_project].iloc[0]
st.write(f"**Number of project stars:** {project_details["stars"]}")
st.write(f"**Link to project:** [{project_details["name"]}]({project_details["link"]})")
