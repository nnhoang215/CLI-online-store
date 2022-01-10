def prompt_review():
    """
    This function prompts the user to leave a review
    """
    response = input(
        "Would you like to rate your purchase experience? It will help us improve our services (yes, no): ")
    while not (response.lower() == "yes" or response.lower() == "no"):
        response = input("please enter valid response")
    """
    If the user says no to the prompt
    """

    if response == "no":
        print("Thank you for your purchase, we hope you will continue to use our services!")
        return
    """
    If the user says yes
    """

    name = input("Name: ")
    """
    Prompts the user to input their name
    """
    rating = input("How would you rate our services on a scale of 1 to 5: ")
    while rating not in ["1", "2", "3", "4", "5"]:
        rating = input("Please enter a number from 1 to 5: ")
    """
    Prompts the user to leave a rating (must be an integer from 1 to 5)
    """
    comments = input("Additional comments: ")
    """
    Prompts the user to leave a comment
    """

    save_review(name, rating, comments)

    print("Thank you for your time! We hope to see you again")


def save_review(name, rating, comments):
    """
    This function saves the users' reviews in a text file
    :param name: users' name
    :param rating: rating from 1 to 5
    :param comments: additional comments
    """
    with open("ratings.txt", "a") as f:
        f.write("Name: " + name + "\nRating: " + rating + "\nComment: " + comments + "\n\n")


