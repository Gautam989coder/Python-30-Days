# User se 5 numbers lo aur list mein store karo.
numbers = []
for i in range(5):
    num = int(input(f'Enter Number {i+1}: '))
    numbers.append(num)

print(f'Here are your list {numbers}')
print(f'Total of the list is {sum(numbers)}')
print(f'largest no. of the list is {max(numbers)}')
print(f'Smallest no. of the list is {min(numbers)}')
print(f'Average of the list is {sum(numbers) / len(numbers)}')


