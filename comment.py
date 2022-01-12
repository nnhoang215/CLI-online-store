import sys
import common


def ask_feedback():
    comment = common.input_highlight("Would you like to share your thought about our shop? [y/n]: ")
    while comment not in ["y", "n", "Y", "N"]:
        comment = common.input_highlight("Please answer with \"y\" or \"n\": ")

    if comment.lower() == "n":
        print("Thank you for trusting and choosing our shop! \n")
        print("---THANK YOU AND SEE YOU SOON!---")
        return None

    rating = input("What would you rate us? (0 -> 10): ")
    while rating.strip() not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
        rating = common.input_highlight("Please answer with an integer between 0 and 10.")

    if int(rating) <= 7:
        print("We will try to improve our service!")
        improvement = common.input_highlight("What do you think we should improve on?: ")
        print("Thank you for your time!")
        print(f"We will try to improve on {improvement} as soon as possible.")
        print("---THANK YOU AND SEE YOU SOON!---")
    else:
        print("We glad you love your experience here!")
        print("Thank you for trusting and choosing our shop!")
        print("---THANK YOU AND SEE YOU SOON!---")
        improvement = ''

    save_review(rating, improvement)


def save_review(rating, improvement):
    with open("ratings.txt", "a") as f:
        f.write(f"Rating: {rating} \nImprovement: {improvement} \n\n")


ask_feedback()
