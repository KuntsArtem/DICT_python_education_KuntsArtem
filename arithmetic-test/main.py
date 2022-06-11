import math
import random
def lvl_1_exerise():
    global answer
    x = random.randint(2, 9)
    y = random.randint(2, 9)
    action = random.randint(1, 3)
    if action == 1:
        print(str(x) + "+" + str(y))
        answer = x + y
    if action == 2:
        print(str(x) + "-" + str(y))
        answer = x - y
    if action == 3:
        print(str(x) + "*" + str(y))
        answer = x * y
def lvl_2_exerise():
    global answer
    x = random.randint(11, 29)
    print("Square " + str(x))
    answer = x * x
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
print("Which level do you want? Enter \n 1 - simple operations with numbers 2-9 \n 2 - integral squares of 11-29 ")
test = False
user_level = input(">")
if int(user_level) == 1:
    test = True
if int(user_level) == 2:
    test = True
while test == False:
    user_level = input("Please, enter a number 1 or 2 >")
    if is_number(user_level) == True:
        if int(user_level) == 1:
            test = True
        if int(user_level) == 2:
            test = True
right_answer_counter = 0
answer_counter = 0
if int(user_level) == 1:
    while answer_counter != 5:
        lvl_1_exerise()
        test = False
        user_answer = input("Enter your answer >")
        if is_number(user_answer) == True:
            test = True
        while test == False:
            user_answer = input("Please, enter a number >")
            test = False
            if is_number(user_answer) == True:
                break
        if int(user_answer) == answer:
            right_answer_counter = right_answer_counter + 1
            print("Right")
        else:
            print("Wrong")
        answer_counter = answer_counter + 1
if int(user_level) == 2:
    while answer_counter != 5:
        lvl_2_exerise()
        test = False
        user_answer = input("Enter your answer >")
        if is_number(user_answer) == True:
            test = True
        while test == False:
            user_answer = input("Please enter a number >")
            test = False
            if is_number(user_answer) == True:
                break
        if int(user_answer) == answer:
            right_answer_counter = right_answer_counter + 1
            print("Right")
        else:
            print("Wrong")
        answer_counter = answer_counter + 1
print("Your mark is " + str(right_answer_counter) + "/5. Well done!")
username = input("What is your name >")
f = open('text.txt', 'a')
f.write(username + " result is " + str(right_answer_counter) + "/5" + "\n")
f.close()
print("All results saved to text.txt")


