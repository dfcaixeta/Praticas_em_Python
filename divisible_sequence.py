
print('')
print('-' * 22)
print('Divisible number by ...')
print('-' * 22)
print('')


# Take a list of numbers

my_list = [12, 65, 54, 39, 109, 339, 221]

value = int(input("Input wint the divisible number: "))

print('')

# Use anonymous function to filter

result = list(filter(lambda x: (x % value == 0), my_list))

# Display to results

print(f"Number divisible by {value} are", result)

print('')

# EOF