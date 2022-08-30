
import streamlit as st

def greet_me(name , gender):
    if gender.lower() == 'female':
        greeting ='Hello ' + 'Ms. ' + name.capitalize()
    else:
        greeting ='Hello ' + 'Mr. ' + name.capitalize() 
    return greeting

    
def main():
    st.title('Greeting')
    name = st.text_input('Name')
    print(name)
    gender = st.selectbox('Gender' , ['Female' , 'Male'])
    button = st.button('Greet me!')
    if button:
        greeting = greet_me(name , gender)
        st.success(greeting)
        
    

if __name__ == '__main__':
    main()
    