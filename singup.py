import streamlit as st

select = st.selectbox('Select', ['login', 'singup'])
# =pd.read_csv('accounts.csv')
account = open('accounts.csv', 'r+')


def login():
    login_flage = False
    if select == 'login':
        user_name_or_email = st.text_input('User name')
        password = st.text_input('Enter your password', type='password')
        if user_name_or_email and password and st.button('login'):
            for i in account.readlines()[1:]:
                checker = i.split(',')
                st.write(checker)
                # st.write(checker[2].replace('\n', ''))
                if user_name_or_email == checker[0] or user_name_or_email == checker[1]:
                    if password == checker[2].replace('\n', ''):
                        st.write('login succescful')
                        login_flage = True
                        break
            else:
                st.write('Account not found', help='try to singup')
            if login_flage:
                if st.button('log out'):
                    account.close()
                    login()

    if select == 'singup':
        user_name = st.text_input(
            'Enter a Unique name', help="Don't use--> ',' anywhere")
        email = st.text_input('Email address')
        password = st.text_input('Create password', type='password')
        new_account = ['\n', user_name, email, password]
        count = 0
        if user_name and email and password and st.button('singup'):
            if ',' not in user_name and ',' not in email and ',' not in password:
                for i in account.readlines()[1:]:
                    checker = i.split(',')
                    st.write(checker)
                    # st.write(checker[0],user_name)
                    # st.write(checker[1],email)
                    if user_name == checker[0] or email == checker[1]:
                        count = 1
                        break
                st.write(count)
                if count == 0:
                    account.write(new_account[0]+','.join(new_account[1:]))
                    account.close()
                    st.write('Account created sucessfuly')
                    st.write('You can login with your account')
                    st.balloons()
                else:
                    st.subheader('Acount already exists')
            else:
                st.warning('Not allowed this sign ","')


login()
