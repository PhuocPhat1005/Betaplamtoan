import streamlit as st

st.title('Bé tập làm toán')

col1, col2, col3 = st.columns(3)
with col1:
    number1 = st.number_input('a')
with col2:
    radio = st.radio(label='Phép toán', options = ('$+$', '$-$', 'x', ':'), horizontal = True)
with col3:
    number2 = st.number_input('b')

number3 = st.number_input('Nhập kết quả')

if st.button('Kiểm tra'):
    result = number1 + number2
    if radio == '$-$':
        result = number1 - number2
    elif radio == 'x':
        result = number1 * number2
    elif radio == '$:$':
        result = number1 / number2
    if result == float(number3):
        st.success('Correct answer')
        st.balloons()
    if radio == '$:$' and number2 == float(0):
        st.error(f'Wrong data, b must not be the same as 0.')
    else:
        st.error(f'Wrong answer, the correct answer is {result}.')

