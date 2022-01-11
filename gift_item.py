from auth import get_address

service_lst = [
    {'name': "Standard service",
     'price': 50,
     'description': """
---SERVICE'S DESCRIPTION---
1. Scheduled shipping time with the customer
(Delivery takes at least 2 days)
2. Standard wrapping material
3. Include: 
    - a rose
    - a gifting card hand-written by our staff
---------------------------
     """
    },
    {'name': 'Premium service',
     'price': 200,
     'description': """
---SERVICE'S DESCRIPTION---
1. Scheduled shipping time with the customer
(Delivery takes at least 2 days)
2. Premium wrapping material
(Will schedule meeting with customer to take custom wrapping order)
3. Include: 
    - a flower bouquet 
    - balloons
    - a teddy bear
    - a gifting card hand-written by our staff and sealed with our shop wax seal  
---------------------------
     """
    }
]
def print_message():
    print('I\'m sorry, I did not understand your selection. Please enter the corresponding letter for your response.')


def choose_service():
    print("Okay. Here are two gifting services that we are currently providing:")
    for i in range(0,len(service_lst)):
        print(service_lst[i].get('description'))
    gift_service = input("Please choose your option: \n[a] Standard \n[b] Premium \n>")
    if gift_service == 'a':
    # return tiền để tí cộng vào bill checkout
        return 50
    elif gift_service == 'b':
        return 100
    else:
        print_message()
        return choose_service()

def notify_email():
    send_email = input("Do you want to send an email notifying the recipient? [y/n] \n>")
    if send_email == 'y':
        pass # để tạm :))
        # Gửi mail vs nội dung là "You have received a gift from ..."
    elif send_email == 'n':
        print("Sure")
        pass
    else:
        print_message()
        return notify_email()


def gift_item():
    # This function take email of the person that receive the gift of the user
    # It will also offer deals and services when gifting someone
    user_input = input("Please enter the email of the gift recipient: \n>")
    print("The gift will be delivered to {}".format(get_address(user_input)))
    bill_service = choose_service()
    notify_email()
    # return tiền service rồi lúc viết
    # chỉ cần khai thêm biến = gift_item() rồi cộng vào để check out
    return bill_service


gift_item()
