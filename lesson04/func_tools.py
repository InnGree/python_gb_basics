from functools import reduce
# принимает функцию и список элементов, каждый элемент приводится к общему результату

users_balance = {"john": 340, "arthur": 100, "kate": 670}

def my_balance_function(total, amount):
    return total + amount

users_total = reduce(my_balance_function, users_balance.values())

# users_total = reduce(
#     lambda total, amount: total + amount,
#     users_balance.values()
# )

print(users_total)

