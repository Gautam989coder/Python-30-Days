# Count Even and Odd Numbers
# Difficulty: Easy–Medium
# Use this list:


# Loop through the list and count how many numbers are even and how many are odd.
# Concepts: lists, loops, if/else, % (remainder)



numbers = [3, 2, 4, 8, 6, 2, 1]   
even_count = 0
odd_count = 0
for i in numbers:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count +=1    
print(f'Even numbers count {even_count}')
print(f'Odd numbers count {odd_count}')