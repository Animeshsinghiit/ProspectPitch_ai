import streamlit as st
import yaml
from yaml.loader import SafeLoader
from streamlit_local_storage import LocalStorage


with open('auth_config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


def check_credentials(username, password):
    if username in config['credentials']['usernames']:
        if config['credentials']['usernames'][username]["password"] == password:
            return True
    return False


def authentication_ui():
    placeholder = st.empty()
    with placeholder.form("login"):
        st.markdown("#### Enter your credentials")
        username = st.text_input("User")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")

        # Process login
        if submit and check_credentials(username, password):
            # Store logged-in user in local storage
            st.session_state['logged_in_user'] = username
            placeholder.empty()
            st.success(f"Login successful. Welcome, {username}!")
            st.rerun()  # Refresh the app after login
        elif submit:
            st.error("Either username or password is incorrect")

# Content for logged-in users
def logged_in_ui():
    logged_in_user = st.session_state.get('logged_in_user', None)
    if logged_in_user:
        return True 
    else:
        authentication_ui()

if __name__ == '__main__':
    logged_in_ui()  