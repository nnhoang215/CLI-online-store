def promo_check(code_dict) -> int:
    """
    This function checks if the input code is valid and return the discount value
    :param code_dict: a dictionary that contains the promo codes
    :return: discount value
    """
    code = input("Promo code: ")
    """
    Prompts the user to input a promo code
    """

    if not (code in code_dict):
        print("Sorry, that code has either expired or has been fully redeemed.")
        return 0
    """
    If the code is invalid
    """

    return code_dict[code]


def create_code_dict() -> dict:
    """
    This function creates a dictionary containing the promo codes and their values from a separate text file
    :return: a dictionary
    """
    code_dict = {}

    with open("discountcodes.txt", "r") as f:
        """
        Read the first line, if it's not the end of file then continue to read second line, then add to dict as 
        key:value pair. Repeat until end of file
        """
        line1 = f.readline().strip()
        while line1 != "":
            line2 = f.readline().strip()
            code_dict[line1] = line2
            line1 = f.readline().strip()
    return code_dict


promo_list = create_code_dict()
