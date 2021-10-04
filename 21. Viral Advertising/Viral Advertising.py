import math
input_str = input()
try:
    n = int(input_str)
except:
    print("An error occurred while parsing the required input as integer.")
if n <= 0 or n >= 51:
    print("Bad input specified! Please try again")
result = 0
people = 5
for day in range(1, n + 1):
    half = math.floor(people / 2)
    result += half
    people = 3 * half
print(result)
