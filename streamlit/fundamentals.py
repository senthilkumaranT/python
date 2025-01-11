import streamlit as st
import pandas as pd
import numpy as np 


st.title("sample app ")

st.text_input("enter your nam e")

### write 
st.write("hello world")

### line chart 
data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(data)


### slider 
x= st.slider("x")

st.write(x, "squared is ",x*x)




###input 
 
st.text_input("enter your name " , key ="name")


if st.checkbox('Show dataframe'):
    st.session_state.name




df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option





import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")