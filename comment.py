import sys
import common


def ask_feedback():
    comment = common.input_highlight("Would you like to share your thought about our shop? [y/n]: ")
    if comment.lower() == "y":
        input("Your comment here: ")
        rating = input("What would you rate us? (0 -> 10)): ")
        if int(rating) <= 7:
            print("We will try to improve our service!")
            improvement = common.input_highlight("What do you think we should improve on?: ")
            print("Thank you for your time")
            print("We will try to improve on " + improvement + " as soon as possible")
            print("---THANK YOU AND SEE YOU SOON!---")
        else:
            print("We glad you love your experience here!")
            print("Thank you for trusting and choosing our shop! ")
            print("---THANK YOU AND SEE YOU SOON!---")
    else:
        print("Thank you for trusting and choosing our shop! \n")
        print("---THANK YOU AND SEE YOU SOON!---")
