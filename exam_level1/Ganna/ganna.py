
# Question 11
def check_password(str):
    str ='sr@m@_f0rtu9e$._2023'
    count_upper ,count_lower ,count_digits ,count_special =0 ,0 ,0 ,0
    if len(str)>= 8:
        for letter in str:
            if letter.isupper():
                count_upper +=1
            elif letter.islower():
                count_lower +=1
            elif letter.isdigit():
                count_digits +=1
            elif letter.isalnum():
                count_special +=1

    if count_upper >= 1 and count_lower >= 1 and count_digits >=1 and count_special >= 1:
        return True
    else:
        return False
str ='sr@m@_f0rtu9e$._2023'
res =check_password( str)
print(res)


# Question 12
def reverse_string(statement):
    words_list =statement.split(' ')
    my_list =[]
    for word in words_list:
        my_list.insert(0 ,word)

    words_str =' '.join(my_list)
    return words_str
statement ="i like this program very much"
print(reverse_string(statement))


# Question 13
def check_numbers_exist(my_list ,num):
    found =False
    indexes_list =[]
    for item in range(len(my_list)):
        if num== my_list[item]:
            indexes_list.append(item)
            found= True
    if found:
        return indexes_list
    else:
        return('Number not found ')
my_list =[2 ,5 ,3 ,8 ,6]
print(check_numbers_exist(my_list ,5))


# Question 14
def remove_characters(str):
    str1 =""
    for letter in str:
        if letter.isalnum():
            str1 += letter
    return str1
str ='123abcjw:,.@eiw'
print(remove_characters(str))

# Question 15
ips_List =[('192.168.0.15', 'y') ,('192.168.0.22', 'y') ,('192.168.0.14', 'y') ,('192.168.0.24', 'n')
            ,('192.168.0.15', 'y') ,('192.168.0.11', 'y')]
unique_list =[]
for ip in ips_List:
    if ip not in unique_list:
        unique_list.append(ip)
print(unique_list)

# Question 16
company_employees = [
    (101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
    (102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
    (103, 'Adham Aly', 5000.0, 'Engineer' ,'M'),
    (104, 'Islam Hassan', 7000.0, 'Sales' ,'M'),
    (105, 'Marwa Esam', 7000.0, 'Marketer' ,'F'),
    (106, 'Ola Hassan', 7000.0, 'Engineer' ,'F')
]

count_female ,count_male =0, 0
for employee in company_employees :
    if employee[4] =='F':
        count_female +=1
    elif employee[4 ]== 'M':
        count_male +=1
print('Count of Female: ' ,count_female)
print('Count of Male: ' ,count_male)

# Question 17
shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
for key in shopping_cart_dict:
    shopping_cart_dict[key] *= 1.10
print(shopping_cart_dict)

total_sum =0
for value in shopping_cart_dict.values():
    total_sum += value
print(total_sum)

total_net = total_sum +26.95
print(total_net)

# Question 18
num1 = 3
num2 = 5
num1, num2 =num2 ,num1
print(num1)
print(num2)

# Question 19

ips_List =[('192.168.0.15', 'y') ,('192.168.0.22', 'y') ,('192.168.0.14', 'y') ,('192.168.0.24', 'n'), ('192.168.0.15', 'y') ,('192.168.0.11', 'y')]
ips_str = ' '.join(ips_List)
for i in ips_str:
    del ips_str[i][1]
print(ips_str)


# Question 20
str = 'Computer science portal for portal'
word = 'portal'
count = 0
str1 = str.split(' ')
for item in str1:
    if item == word:
        count += 1
print('Count Occurrences of a word:', count)

