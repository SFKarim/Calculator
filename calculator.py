# Save this as app.py

import streamlit as st

# Title of the app
st.title('Simple Calculator')

# Inputs for numbers
num1 = st.number_input('Enter the first number:', format="%.2f")
num2 = st.number_input('Enter the second number:', format="%.2f")

# Dropdown for selecting the operation
operation = st.selectbox('Choose an operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Calculate the result
def calculate(num1, num2, operation):
    if operation == 'Add':
        return num1 + num2
    elif operation == 'Subtract':
        return num1 - num2
    elif operation == 'Multiply':
        return num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: Division by zero'

result = calculate(num1, num2, operation)

# Display the result
st.write(f'Result: {result}')

