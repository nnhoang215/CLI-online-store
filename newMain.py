import pandas as pd
from pandas.core.algorithms import isin
from auth import CURRENT_USER, IS_ADMIN, sign_in, sign_up
from menu_2 import get_shopping_list, menu_2
from user_controller import get_info, get_shopping_info
import common
import menu


def authenticate():
    choice = common.input_highlight("Enter '1' or '2'. [1] Sign Up | [2] Log In ")
    
    if choice == '1':
        sign_up()
    elif choice == '2':
        sign_in()
    else:
        authenticate()

def main():
    exit_program = False
    # authenticate()
    # while exit_program == False:
    menu_2()
    # print(get_shopping_list())
        # print(get_info(IS_ADMIN, CURRENT_USER))

main()

    
