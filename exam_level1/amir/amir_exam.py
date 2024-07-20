# Answer 1
def validpassword(pass_value):
    count_upper, count_lower, count_digits, count_signs = 0, 0, 0, 0
    if len(pass_value) > 8:
        for letter in pass_value:
            if letter.isupper():
                count_upper += 1
            if letter.islower():
                count_lower += 1
            if letter.isdigit():
                count_digits += 1
            elif not letter.isalnum():
                count_signs += 1
        if count_upper >= 1 and count_lower >= 1 and count_digits >= 1 and count_signs >= 1:
            return True
        else:
            return False
    else:
        return False


password = "sr@m@_f0rtu9e$._2023"
print(validpassword(password))

# ------------------------------------------
# Answer 2

statement = "i like this program very much"


def reverse():
    words = statement.split()
    reversed = words[::-1]
    reversedstate = ' '.join(reversed)
    print(reversedstate)


reverse()

# -----------------------------------------
# Answer 3

my_list = [1, 1, 2, 3, 2, 4, 2, 5, 2, 4, 2]
num = 2

def appers():
    indexes = []
    for i in range(len(my_list)):
        if my_list[i] == num:
            indexes.append(i)

    print(indexes)


appers()


# -----------------------------------------
# Answer 4

def removing(statement):
    after = []
    for i in statement:
        if i.isalnum():
            after.append(i)
    return ''.join(after)


ini_string = "123abcjw:, .@! eiw"
state = removing(ini_string)
print(state)

# -----------------------------------------
# Answer 5

ips_List = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.15', 'y'),
    ('192.168.0.11', 'y')
]
unique = []
for i in ips_List:
    if i not in unique:
        unique.append(i)

print(unique)

# -----------------------------------------
# Answer 6

company_employees = [
    (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
    (103, 'Adham Aly', 5000.0, 'Engineer', 'M'),
    (104, 'Islam Hassan', 7000.0, 'Sales', 'M'),
    (105, 'Marwa Esam', 7000.0, 'Marketer', 'F'),
    (106, 'Ola Hassan', 7000.0, 'Engineer', 'F')
]
countmale = 0
countfemale = 0
for employee in company_employees:
    if employee[4] == 'M':
        countmale = countmale + 1
    elif employee[4] == 'F':
        countfemale = countfemale + 1

print(countmale)
print(countfemale)

# -----------------------------------------
# Answer 7

shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
print(shopping_cart_dict)

total = 0
for item, value in shopping_cart_dict.items():
    shopping_cart_dict[item] = value + value * (10 / 100)
    total = total + shopping_cart_dict[item]

print(shopping_cart_dict)
print(total)

order_vat = total + total * (14 / 100)
print(order_vat)

# -----------------------------------------
# Answer 8

num1 = 4
num2 = 7
print(num1, num2)

num1, num2 = num2, num1

print(num1, num2)

# -----------------------------------------
# Answer 9

ips_list = [
    ('192.168.0.15', 'y'),
    ('192.168.0.22', 'y'),
    ('192.168.0.14', 'y'),
    ('192.168.0.24', 'n'),
    ('192.168.0.81', 'n'),
    ('192.168.0.11', 'y')
]

for i, state in ips_list:
    if state == 'y':
        print(i, '>', i.split('.')[-1])

# -----------------------------------------
# Answer 10

words = 'my name is amir , amir has 19 years old , amir loves python'
word = 'amir'

words2 = words.split()
count = 0
for item in words2:
    if item == word:
        count = count + 1

print(count)
