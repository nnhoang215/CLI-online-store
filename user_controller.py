import pandas as pd
import common


def get_info(is_admin, current_user):
    users = pd.read_csv('users.csv')

    target_email = common.input_highlight("Email of who you want to search: ")
    target_user =  users[(users['email'] == target_email)]
    if is_admin:
        return target_user
    else:
        common.print_fail("You are not authorized to see other's information!")
        return current_user

def get_shopping_info(is_admin, current_user):
    users = pd.read_csv('users.csv')
    
