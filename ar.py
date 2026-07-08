def remove_duplicates(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)

    return result

numbers = [1, 2, 2, 3, 4, 4, 5]

print("Original List:", numbers)
print("List after removing duplicates:", remove_duplicates(numbers))








def count_words(sentence):
    words = sentence.split()
    return len(words)

text = input("Enter a sentence: ")

print("Number of words =", count_words(text))




def palindrome(text):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not a Palindrome"

string = input("Enter a string: ")

print(palindrome(string))




def find_sum(numbers):
    total = 0
    for i in numbers:
        total = total + i
    return total

n = int(input("Enter the number of elements: "))

lst = []
for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

print("Sum =", find_sum(lst))





def average(a, b, c):
    avg = (a + b + c) / 3
    return avg

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Average =", average(num1, num2, num3))



def even_numbers(lst):
    even_list = []

    for i in lst:
        if i % 2 == 0:
            even_list.append(i)

    return even_list

n = int(input("Enter the number of elements: "))

numbers = []
for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

print("Even numbers:", even_numbers(numbers))








def count_digits(num):
    count = 0

    while num != 0:
        count = count + 1
        num = num // 10

    return count

number = int(input("Enter a number: "))

print("Number of digits =", count_digits(number))





def sum_even_digits(num):
    total = 0

    while num != 0:
        digit = num % 10
        if digit % 2 == 0:
            total = total + digit
        num = num // 10

    return total

number = int(input("Enter a number: "))

print("Sum of even digits =", sum_even_digits(number))