import common
import pandas as pd

from confirmation import send_signup_confirmation



users = pd.read_csv('users.csv')

CURRENT_USER = users.iloc[0]
IS_LOGGED_IN = False
IS_ADMIN = False


#full_name,email,key,address,phone number,items bought,total expense 
def get_address(email):
    user = users[(users['email'] == email)]
    user_index = user.index[0]
    address = users.at[user_index, 'address']
    return address
def sign_up():
    users = pd.read_csv('users.csv')
    common.print_function("Signing up for new user")

    signup_email = input("Your email address(used to sign in):")
    is_email_available = users[(users['email'] == signup_email)].empty
    
    if is_email_available:
        signup_key = str(input("Enter a password: "))
        confirm_key = input("Re-enter your password: ")

        if (signup_key == confirm_key):
            full_name = input("\t" + "What is your full name? ")
            address = str(input("\t" + "What is your address? "))
            phone = str(input("\t" + "What is your phone number? "))
        else:
            common.print_fail("Passwords do not match. Try again! \n")
            sign_up()

        new_user = pd.DataFrame({
            'full_name': [full_name],
            'email': [signup_email],
            'key': [signup_key],
            'address': [address],
            'phone_number': [phone],
            'items_bought': [0],
            'total_expense': [0],
        })
        new_user.to_csv('users.csv', mode = 'a', header = False, index=False)
        send_signup_confirmation(signup_email, signup_key, full_name)
        common.print_success("Let's sign in \n")
        sign_in()
    else:
        common.print_highlight("This email is already associated with an account \n")
        sign_in()
        
def sign_in():
    users = pd.read_csv('users.csv')
    common.print_function("Logging into your account")

    login_email = input("Email: ")

    user = users[(users['email'] == login_email)]
    if user.empty:
        common.print_fail("Wrong email. Please try again")
        choice = common.input_highlight("Enter '1' or '2'. [1] Try again | [2] Sign Up ")
        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_up()
    else:
        user_index = user.index[0]

    login_key = str(input("Password: "))
    
    global IS_LOGGED_IN
    IS_LOGGED_IN = login_key == str(users.at[user_index, 'key'])

    if login_email == "admin":
        global IS_ADMIN
        IS_ADMIN = True

    if IS_LOGGED_IN:
        global CURRENT_USER
        CURRENT_USER = user
        common.print_success("Login successfully \n")
    else:
        common.print_fail("Wrong password. Please try again")
        choice = common.input_highlight("Enter '1' or '2'. [1] Try again | [2] Sign Up ")
        if choice == '1':
            sign_in()
        elif choice == '2':
            sign_up()