





#  Count Uppercase and Lowercase Letter

s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)



#  Find Largest and Smallest Number


num = [12, 45, 7, 89, 23, 5]

largest = num[0]
smallest = num[0]

for num in num:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)



#  Count Vowels in "programming"


t = "programming"
vowels = "aeiou"

count = 0

for ch in t:
    if ch in vowels:
        count += 1

print("Number of vowels:", count)


# Print List in Reverse Order

num = [10, 20, 30, 40, 50]

for i in range(len(num) - 1, -1, -1):
    print(num[i])



#  Print Numbers from 10 to 1


for i in range(10, 0, -1):
    print(i)



#  Check Palindrome Number


num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")



#  Check Positive, Negative or Zero


num = float(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")


# Check Armstrong Number
# 

num = int(input("Enter a number: "))

original = num
power = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** power
    num = num // 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")



#  Sum of Even and Odd Numbers


numbers = [2, 5, 8, 11, 14, 17, 20]

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

even_list = [even_sum]
odd_list = [odd_sum]

print("Original List:", numbers)
print("Even Sum List:", even_list)
print("Odd Sum List:", odd_list)



# Find Common Elements Between Two Lists


list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Common Elements:", common)