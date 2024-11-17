def get_password(number):
    password = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password += str(i) + str(j)
    return password
for i in range(3, 21):
    result = get_password(i)
    print(f"{i} - {result}")
n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)

number = int(input("Enter a number: "))
password = get_password(number)
print(number, " : ", password)

while True:
    number = input("Enter a number (or 'exit' to quit): ")
    if number.lower() == 'exit':
        break
    if number.isdigit():
        number = int(number)
        if 3 <= number < 20:
            password = get_password(number)
            print(number, " : ", password)
    else:
        print("Please enter a valid number.")





