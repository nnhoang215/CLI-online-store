import yagmail
import common


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