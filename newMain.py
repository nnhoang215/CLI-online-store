from termcolor import colored
import pandas as pd
from pandas.core.algorithms import isin
import yagmail

users = pd.read_csv('users.csv')

CURRENT_USER = users.iloc[0]
IS_LOGGED_IN = False

def print_function(message):
    print(colored(message, 'blue'))

def print_fail(message):
    print(colored(message, 'red'))

def print_highlight(message):
    print(colored(message, 'yellow'))

def print_success(message):
    print(colored(message, 'green'))    

def input_highlight(message):
    return input(colored(message, 'yellow'))
#full_name,email,key,address,phone number,items bought,total expense 
def get_address(email):
    user = users[(users['email'] == email)]
    user_index = user.index[0]
    address = users.at[user_index, 'address']
    return address
def sign_up():
    users = pd.read_csv('users.csv')
    print_function("Signing up for new user")

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
            print_fail("Passwords do not match. Try again! \n")
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
        send_confirmation(signup_email, signup_key, full_name)
        print_success("Let's sign in \n")
        sign_in()
    else:
        print(colored("This email is already associated with an account \n", 'yellow'))
        sign_in()

def send_confirmation(email, key, full_name):
    contents = [""" Dear {full_name},

        Congratulations, you have registered an account with us!
        This information is confidential, it is advised that you not share it with anyone
        The account login information are as followed:
        - email: {email} 
        - password: {key} 

        Best,
        CLI Online App group 4
    """.format(full_name = full_name, email=email, key = key)]
    try:
        yagmail.SMTP('hoangtesting93@gmail.com','@HoangTest' ).send(email,'Account Registration', contents)
    except:
        print_fail("Could not send confirmation to '{email}'".format(email=email))

        
def sign_in():
    users = pd.read_csv('users.csv')
    print_function("Logging into your account")

    login_email = input("Email: ")
    login_key = str(input("Password: "))
    user = users[(users['email'] == login_email)]
    user_index = user.index[0]

    global IS_LOGGED_IN
    IS_LOGGED_IN = login_key == str(users.at[user_index, 'key'])
    
    if IS_LOGGED_IN:
        global CURRENT_USER
        CURRENT_USER = user
        print_success("Login successfully \n")

def authenticate():
    choice = input_highlight("Enter '1' or '2'. [1] Sign Up | [2] Log In ")
    
    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        authenticate()

def main():
    authenticate()
main()

    
