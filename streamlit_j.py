import streamlit as st

st.title("Simple Calculator app")
first_num = st.number_input("Enter your first number",value=0)
second_num = st.number_input("Enter your second number",value=0)

col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("Add (+)", use_container_width=True):
        addition = first_num + second_num
        st.success(f"Result:{addition}") 
with col2:
    if st.button("Subtract (-)", use_container_width=True):
        subtract = first_num - second_num
        st.success(f"Result:{subtract}") 
with col3:
    if st.button("Multiply (*)", use_container_width=True):
        multiply = first_num * second_num
        st.success(f"Result:{multiply}") 
with col4:
    if st.button("Division (+)", use_container_width=True):
        if second_num != 0:
            division = first_num / second_num
            st.success(f"Result:{division}")
        
        else:
            st.error("Error:Division by zero is not allowed")                             



