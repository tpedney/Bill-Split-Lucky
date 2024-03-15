import math
import random

print("Enter the number of friends joining (including you):")
number_friends = int(input())
friends_dict = {}


def get_split_cost(bill_total, number_friends):
    indiv_bill = bill_total / number_friends
    indiv_bill_round = round(indiv_bill, 2)
    return indiv_bill_round


def bill_splitter():
    if number_friends < 1:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(number_friends):
        name = input()
        friends_dict[name] = get_split_cost(0, number_friends)
    print("Enter the total bill value:")
    bill_total = int(input())

    for friend in enumerate(friends_dict):
        _, name = friend
        friends_dict[name] = get_split_cost(bill_total, number_friends)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer_lucky = input()

    if answer_lucky.lower() == "yes":
        friends_keys = friends_dict.keys()

        friends_list = list(friends_keys)

        friends_random = random.choice(friends_list)
        for i, friend in enumerate(friends_dict):
            friends_dict[friend] = get_split_cost(bill_total, number_friends - 1)
        friends_dict[friends_random] = 0
        print(f"{friends_random} is the lucky one!")
    else:
        print("No one is going to be lucky")

    print(friends_dict)


bill_splitter()
