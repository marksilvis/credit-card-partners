import streamlit as st
# from st_paywall import add_auth
# import st_paywall.buymeacoffee_auth as stp

# st.title("🎈 Tyler's Subscription app POC 🎈")
# st.balloons()

# add_auth(required=True)

# st.write("Congrats, you are subscribed!")
# st.write('the email of the user is ' + str(st.session_state.email))

# x = "markbbarnes@yahoo.com"
# y = x and x in stp.get_bmac_payers(one_time = True)
# st.write(y)

if 'page' not in st.session_state:
    st.session_state['page'] = 0

st.write("this works")

def nextpage(): st.session_state['page'] += 1
def restart(): st.session_state['page'] = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 3))

if st.session_state['page'] == 0:
    # Replace the placeholder with some text:
    placeholder.text(f"Hello, this is page {st.session_state.page}")

elif st.session_state['page'] == 1:
    # Replace the text with a chart:
    placeholder.line_chart({"data": [1, 5, 2, 6]})

elif st.session_state['page'] == 2:
# Replace the chart with several elements:
    with placeholder.container():
        st.write("This is one element")
        st.write("This is another")
        st.metric("Page:", value=st.session_state.page)

elif st.session_state['page'] == 3:
    placeholder.markdown(r"$f(x) = \exp{\left(x^🐈\right)}$")

else:
    with placeholder:
        st.write("This is the end")
        st.button("Restart",on_click=restart)


# if 'x' not in st.session_state:
#     st.session_state['x'] = None

# st.write(st.session_state)



