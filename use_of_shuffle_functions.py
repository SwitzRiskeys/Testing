
import time
import random

keep_going = 'Yes' or 'yes'
while keep_going == 'Yes' or 'yes':
    list_of_number = []
for i in range(10):
    list_of_number.append(random.randint(1,100))
print(f'the starting players are{list_of_number} \n')
predict1 = int(input('Which contestant do you think will win?'))
predict2 = int(input('Which contestant do you think will win?'))
predict3 = int(input('Which contestant do you think will win?'))
predict4 = int(input('Which contestant do you think will win?'))
predict5 = int(input('Which contestant do you think will win?'))

for i in range(9):
    print(f'The last contestant, number {list_of_number[-1]} has been eliminated')
    list_of_number.pop()
    random.shuffle(list_of_number)
    print(f'D...a...n...c...i...n...g\n')
    time.sleep(5)
    print(f'The contestants are{list_of_number}\n')

print(f"Hurray!!Hurraay!!! \ncontestant {list_of_number[0]} is the winner")
if predict1 == list_of_number[0]:
    print(f'{predict1} Your prediction was right')
elif predict2 == list_of_number[0]:
    print(f'{predict1} Your prediction was right')
elif predict3 == list_of_number[0]:
    print(f'{predict1} Your prediction was right')
elif predict4 == list_of_number[0]:
    print(f'{predict1} Your prediction was right')
elif predict1 == list_of_number[0]:
    print('Your prediction was right')

elif:
    print('oops!!! wrong prediction \nTry Again! .')

keep_going = print(input('Would You Like To Play Again!!'))

else:
print('Game has come to an end ')




