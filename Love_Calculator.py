# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combine_name = name1 + name2
lowercase_str = combine_name.lower()

t = lowercase_str.count("t")
r = lowercase_str.count("r")
u = lowercase_str.count("u")
e = lowercase_str.count("e")

true = t + r + u + e

l = lowercase_str.count("l")
o = lowercase_str.count("o")
v = lowercase_str.count("v")
e = lowercase_str.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))
# print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")

