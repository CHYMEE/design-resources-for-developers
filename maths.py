import random

# def display():
#     topic = "MATHS QUIZ!!!"
#     print ('*' * len(topic))
# #print(title)
# #print('*' * len(title))

print(" HELLO!! WELCOME TO THIS QUIZ SESSION")
print (" *" * 19)

topic=0
score = 0
question = 0
operators =("*", ("+"),("-"))

for i in range(3):
    num1=random.randint(5,10)
    num2=random.randint(1,5)
    operator=random.choice(operators)

if operator=="+":
    answer = num1 + num2
elif operator=="-":
    answer=num1-num2
elif operator=="*":
    answer=num1*num2

print ('what is '  + str(num1) +operator+ str(num2))
user_answer= int(input("ENTER ANSWER: "))

if user_answer==answer:
    print("Correct!")
else:
    print("NOT CORRECT! THE ANSWER IS:" + str(answer))
score=score


