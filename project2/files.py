username = input("please input your name: ")
with open(' name.txt ', 'w') as file:
    file = open('name.txt', 'w')
    file.write(username)
    file.close()

with open(' name.txt ', 'r') as file:
    print("Your name is", username)
    file.close()


with open('numbers.txt', 'r') as file:
    sum = 0
    for i in range(2):
        number = int(file.readline())
        sum = sum+number
    print("the total of 2 lines is:", sum )
    file.close()


with open('numbers.txt', 'r') as file:
    sum = 0
    for i in range(3):
        number = int(file.readline())
        sum = sum + number
    print("the total of 3 lines is:", sum )
    file.close()