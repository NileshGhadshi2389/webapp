import streamlit as st
import functions


todos  = functions.get_todos()


def add_todo():
    todo = st.session_state['txt_newtodo'] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My To-Do App")
st.header("To-Do Application")
st.subheader("This is my to-do application")
st.write("this app will give sample of theme")

st.write("Your To-Do list:")



""" for todo in todos:
    st.checkbox(todo)
 """
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# text Input
st.text_input(label="Enter your to-do item:",placeholder="Add new todo...",
              on_change=add_todo, key="txt_newtodo")

