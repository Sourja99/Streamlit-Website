# streamlit_app.py

import streamlit as st
from gsheetsdb import connect
import pandas as pd
#from collections.abc import Iterable

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=1)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["public_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)
