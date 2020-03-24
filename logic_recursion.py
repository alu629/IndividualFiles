############ Q1. Ask the user for an integer, multiply it by itself + 1, and print the result
# Topic: user input

value = int(input("Eneter interger:"))
print(value**2)



############ Q2. Ask the user for an integer
# If it is an even number, print "even"
# If it is an odd number, print "odd"

# Topic: conditionals, user input

if(value % 2 == 0):
    print("Even")
else:
    print("Odd")



############# Q3. Iterate through each element in the list USING A FOR LOOP, add 5 to it, and print them 
# Topic: loops + lists

numbers = [1, 2, 3, 4, 5]

# Code here
index = 0
for number in numbers:
    numbers[index] = number + 5
    index += 1
print(numbers)



# ############# Q4. Iterate through the list and only print values that are divisible by 3 ############
# Topic: lists, loops, conditions, comparison operators

numbers = list(range(0, 500))

# Code Here
EveryThirdNumber = []
for number in numbers:
    if(number % 3 == 0):
        EveryThirdNumber.append(number)
print(EveryThirdNumber)




# ############# Q5. Iterate through the list and count the number of even numbers within the list ############
# Topic: lists, loops, conditions, comparison operators

numbers = list(range(0, 500))

# Code Here
counter = 0
for number in numbers:
    if (number % 2 == 0):
        counter += 1
print(counter)





############# Q6. Iterate through each element in the list, add 5 to it, and print them
# MUST USE A WHILE LOOP
# Topic: loops + lists
# Hint: You can use len() function

numbers = [1, 2, 3, 4, 5]

# Code here

index = 0
while index < len(numbers):
    newValue = numbers[index] + 5
    numbers[index] = newValue
    #print(newValue)
    index += 1
print(numbers)




############# Q7. For the following list:
# Print ALL numbers divisible by 7 and label them like so: "Divisible by 7: 70"
# Print ALL numbers divisible by 3 and label them like so: "Divisible by 3: 6"
# Print ALL numbers divisible by 3 and 7 and label them like so: "Divisible by 3 and 7: 21"
############

# Topic: lists, loops, conditions, string concatenation

numbers = list(range(0, 500))

# Code here

DivisibleBy7and3Set = []
DivisibleBy7Set = []
DivisibleBy3Set = []
for number in numbers:
    if (number % 7 == 0 or number % 3 == 0):
        if (number % 7 == 0 and number % 3 == 0):
            DivisibleBy7and3Set.append(number)
            print("Divisible by 3 and 7: " + str(number))
            DivisibleBy7Set.append(number)
            print("Divisible by 7: " + str(number))
            DivisibleBy3Set.append(number)
            print("Divisible by 3: " + str(number))
        elif (number % 7 == 0):
            DivisibleBy7Set.append(number)
            print("Divisible by 7: " + str(number))
        else:
            DivisibleBy3Set.append(number)
            print("Divisible by 3: " + str(number))
print("These set of numbers are divisible by 3 and 7:")
print(DivisibleBy7and3Set)
print("These set of numbers are divisible by 3:")
print(DivisibleBy3Set)
print("These set of numbers are divisible by 7:")
print(DivisibleBy7Set)




