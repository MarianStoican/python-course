'''
import copy

my_lambda = lambda x, y: x + y

my_sum = my_lambda(2, 3)
print(my_sum)

print('--------------------------------------------------------------------------------------------------------------')

players = [
    {
        'first_name': 'Jhon',
        'last_name': 'Jhon',
        'rank': 3,
    },
    {
        'first_name': 'Kevin',
        'last_name': 'McDonald',
        'rank': 1,
    },
    {
        'first_name': 'Brad',
        'last_name': 'Kelvin',
        'rank': 4,
    },

]

print(players)
sorted_players = sorted(players, key=lambda player: player['rank'])
print(sorted_players)

print('--------------------------------------------------------------------------------------------------------------')


def check_top_three_players(player):
    updated_player = copy.deepcopy(player)
    updated_player['is_top_three'] = True if player['rank'] <= 3 else False
    return updated_player


top_players = list(map(check_top_three_players, players))

print(top_players)


print('--------------------------------------------------------------------------------------------------------------')

all_mc_donalds = list(filter(lambda player: player['last_name'] == 'McDonald', players))

print(all_mc_donalds)


print('--------------------------------------------------------------------------------------------------------------')

letters = ['a', 'b', 'c', 'z']
numbers = [1, 2, 3]

print(zip(letters, numbers))
for let, nr in zip(letters, numbers):
    print(nr, let)


print('--------------------------------------------------------------------------------------------------------------')

my_numbers = [1, 2, 3, 4, 5]
squared_numbers = [item ** 2 for item in my_numbers if item % 2 == 0]

print(squared_numbers)

m = 0



m = 0


def foo(n):
    global m
    assert m != 0
    try:
        return 1/n
    except ArithmeticError:
        raise ValueError


try:
    foo(0)
except ArithmeticError:
    m += 2
except Exception as e:
    _ = e
    m += 1

print(m)
'''


a = 'abcde'[::-1]
print(a)



