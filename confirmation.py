import yagmail
import common
from menu_2 import purchase


############################## EXTRA FEATURE ######################################
def send_signup_confirmation(email, key, full_name): 
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
        common.print_fail("Could not send confirmation to '{email}'".format(email=email))

# def order_confirmation(email, purchased_items, full_name):
#     address = get_address(email)
#     contents = [""" Dear {full_name},

#         Your order has been successfully placed. 
#         {purchased_items} are being shipped to {address}
#         Expect your package in 3 days

#         Best,
#         CLI Online App group 4
#     """.format(full_name = full_name, email=email, purchased_items = purchased_items, address = address)]
#     try:
#         yagmail.SMTP('hoangtesting93@gmail.com','@HoangTest' ).send(email,'Order Confirmation', contents)
#     except:
#         common.print_fail("Could not send confirmation to '{email}'".format(email=email))
