import numpy as np
import pandas as pd
import altair as alt
import streamlit as st
import altair as alt

st.header("Sharon's st.write samples")

st.write("Hello, **World!** It's summer :sunglasses:")

st.write(1234)

df = pd.DataFrame({
    'col1': [1,2,3,4,5],
    'col2': [10, 20, 30, 40, 50]
})
st.write(df)

st.write("Below is a DataFrame:", df, "Above is a DataFrame in a table")

df2 = pd.DataFrame(
    np.random.rand(200,3),
    columns=["a", "b", "c"]
)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y = 'b', size='c', color = 'c', tooltip=['a', 'b', 'c']
)
st.write(c)