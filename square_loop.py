print('this program displays a list of number')
print('(starting at 1)and their squares.')
end = int(input('how high should i go?'))
print('Number\tSquare')
print('------------')
for number in range(1, end + 1):
    square = number **2
    print(f'{number}\t{square}')




