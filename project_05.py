#challenge_1 : avg using only for loop 

# student_height = input("input a list of students heights\n").split()
# for n in range(0,len(student_height)):
#     student_height[n]=int(student_height[n])
# print(student_height)

# sum=0
# for i in student_height:
#     sum=sum + i
# avg_height = round(sum/len(student_height),2)
# print(f"the avg height of students is :{avg_height}")



#challenge_2 : getting max value from list using for loop

# student_scores = input("input a list of students scores\n").split()
# for n in range(0,len(student_scores)):
#     student_scores[n]=int(student_scores[n])
# print(student_scores)

# highest_score = 0
# for i in student_scores:
#     if i>highest_score:
#         highest_score=i
# print(f"the highest score is :{highest_score}")



#challenge_3 : taking sum 

# sum = 0 
# for i in range(2,101,2):
#     sum += i
# print(sum)



#challenge_4 : fizz-buzz

# range_ = int(input("limit of the game :\n"))

# for i in range(1,(range_+1)):
#     if i%15==0:
#         print("fizzbuzz")
#     elif i%3==0:
#         print("fizz")
#     elif i%5==0:
#         print("buzz")
#     else:
#         print(i)



#project : 

import random 
leters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm','Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbolls =['!', '@', '#', '$', '%', '^', '&', '*']

total_digits = int(input("total no of digit\n"))
no_of_letters = int(input("no of letters in password\n"))
no_of_digits = int(input("no of digits \n"))
no_of_symbolls = int(input("no of symbolls\n"))

#easy level
# password = ""
# for i in range (1,no_of_letters+1):
#     letter = random.choice(leters)
#     password += letter
# for i in range (1,no_of_digits+1):
#     letter = random.choice(numbers)
#     password += letter
# for i in range (1,no_of_symbolls+1):
#     letter = random.choice(symbolls)
#     password += letter
# print(password)

#haard level 
password = ""
password_list = []
for i in range (1,no_of_letters+1):
    password_list.append(random.choice(leters))
for i in range (1,no_of_digits+1):
    password_list.append(random.choice(numbers))
for i in range (1,no_of_symbolls+1):
    password_list.append(random.choice(symbolls))
# print(password_list)
random.shuffle(password_list)
# print(password_list)

for char in password_list:
    password+=char
print(f"your password is : {password} \n")
