import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = len(names)
persontopay = random.randint(0, x - 1)
personpay = names[persontopay]
print(f"{personpay} is going to pay for the meal today")

