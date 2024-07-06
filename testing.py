import streamlit as st

comparison = st.selectbox(
    'Select how many credit cards you are comparing:', 
    (2, 3))
st.write('Result is: ', comparison)

cc = []
for x in range(comparison):
    option = st.selectbox(
        'Select your credit card company', 
        ('Amex', 'BILT', 'Chase', 'Capital One'),
        key = x)
    st.write('You selected:', option)
    cc.append(option)
    del option

st.write(cc)