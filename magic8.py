# We’ll be using the following 9 possible answers for our Magic 8-Ball:

# Yes - definitely
# It is decidedly so
# Without a doubt
# Reply hazy, try again
# Ask again later
# Better not tell you now
# My sources say no
# Outlook not so good
# Very doubtful

# The output of the program will have the following format:
# [Name] asks: [Question]
# Magic 8-Ball’s answer: [Answer]

# For example:
# Joe asks: Is this real life?
# Magic 8-Ball's answer: Better not tell you now

# importing random module
import random

# declaring the name variable
name = input()

# declaring the quesion variable with user input, must be "Yes" or "No" question
question = input()

# declaring the answer variable with an empty string
answer = ""

# declaring the random variable (1-9), and adding a print statement for the random number
random_number = random.randint(1,9)
# print(random_number)

# core logic
if random_number == 1:
    answer = 'Yes - definitely'
elif random_number == 2:
    answer = 'It is decidely so'
elif random_number == 3:
    answer = 'Without a doubt'
elif random_number == 4:
    answer = 'Reply hazy, try again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'Very doubtful'
else:
    print('Error')

if name == "":
    print("Magic 8-ball's answer: " + answer)
elif question == "":
    print(name + ", the universe hates this")
else:
    print(name + ' asks: ' + question)
    print("Magic 8-ball's answer: " + answer)
