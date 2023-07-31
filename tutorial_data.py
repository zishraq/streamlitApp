import streamlit as st
import pandas as pd
from streamlit_modal import Modal

# Load the dataframe
df = pd.DataFrame({
    "Name": ["John Doe", "Jane Doe", "Mary Smith", "Peter Jones"],
    "Age": [30, 25, 40, 50],
    "City": ["New York", "Los Angeles", "Chicago", "Miami"]
})

# Create a modal
modal = Modal(key="my_modal", title="Text Message")

# Add a text message to the modal
if modal:
    st.write("This is a text message.")

# Create a button to open the modal
st.button("Open Modal", on_click=modal.open)

# Click on a row in the dataframe
st.dataframe(df)
