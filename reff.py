# sum = 0
# for i in range(1,101):
#     sum=(sum+i)
#     print (sum)



# l=int(input("enter the length"))
# w=int(input("enter the length"))
# area=(l*w)
# print("area of the squar",area)

# r=float(input("enter the perimeter"))

# s=3.14
# area=(s*r*r)
# print("area of the circle :",area)




#                             # Amstrong number
# l=(input("Enter the number :"))
# len=len(l)
# print(len)
#  =0
# while l >0 :
#     digit = l %10
#     rev = rev * 10 +digit
    
#  print("reversed number",rev)


# num1=str(input("Enter the produt:"))
# num3=int(input("enter the product price:"))
# print("product is:",num1)  
# if num3>5000:
#     discount=num3*0.20
# elif num3>=2000:
#     discount=num3*0.10
# else:
#      discount=0
# total_amount=(num3 - discount)
# print("discount:", discount)
# print("totel price:",total_amount )

# num=int(input("enter the number"))
# digit = num %10
# if digit==0:
#     print("not valid")
# elif digit % 3 == 0:
#         print("valid")
# else:
#     print("not valid")

# stri1=str(input("Enter the first string : "))
# stri2=str(input("Enter the secont string : " ))
# if sorted (stri1) == sorted (stri2):
#     print("its a angram")
# else:
#     print("not a angram")
  
# username=("shamas")
# password=('2468')
# f=str(input("Enter your user name : "))
# p=int(input("Enter your password: "))
# if f==username and p==password:
#     print("Login successfull") 
# else:
#      print("errror")



# s=int(input("Enter the number"))
# if s % 5 == 0 and s % 3 == 0:
#     print("fizz buzz")

# elif s % 3 == 0:
#     print("fizz")
# elif s % 5 == 0:
#     print("buzz")

# s=int(input("Enter the number"))
# if s % 2 == 0 == s % 4 == 0:
#     print ("it divisible of 2 and 4")
# else:
#     print("not same")
    

# a=(input("Enter the name"))
# age=int(input("enter your age"))
# c=float(input("enter your exam percentage"))
# d=int(input("enter your annual income"))
# e=(input("whether the student is already receving another scholarship?  (yes/no):"))
# if age >= 17 and age <= 25 and d < 800000 and e == "no" :
#     if c >= 85:
#         print("get full scholarship")
#     if c >= 70 and c <= 84.99:
#         print("get partial scholarship")
# else:
#         print("Not Eligible")


# a=(input("whether the student passed 10 th standard (yes/no"))
# b=(input("whether the student passed 12 th standard (yes/no"))
# c=float(input("Enter your 12 th percetage"))
# if b == "no":
#     print("Not eligible for admission ")
# elif b =='yes' and b == 'no':
#     print ("complete 12 th to proceed")
# elif c >= 75:
#     print("Eligible for Engineering admission ")
# else:
#     print("Eligible genaral degree")

# Loan Approval System

# age = int(input("Enter your age: "))
# income = float(input("Enter your monthly income : "))
# credit_score = int(input("Enter your credit score: "))
# loan_amount = float(input("Enter your desired loan amount : "))

# if age < 21:
#     print("Loan Denied: Age must be at least 21.")

# elif income < 25000:
#     print("Loan Denied: Income too low.")

# elif loan_amount > (20 * income):
#     print("Loan Denied: Loan amount too high compared to income.")

# else:
#     if credit_score < 650:
#         interest = 15
#         print(f"Loan Conditionally Approved with {interest}% interest.")
#     elif 650 <= credit_score <= 750:
#         interest = 10
#         print(f"Loan Approved with {interest}% interest.")
#     else:
#         interest = 7
#         print(f"Loan Approved with {interest}% interest.")



        # ATM Cash Withdrawal System

amount = int(input("Enter the amount to withdraw: "))

if amount <= 0:
    print("Invalid amount")
elif amount % 100 != 0:
    print("Amount must be in multiples of 100")
elif amount > 20000:
    print("Maximum withdrawal limit is Rs.20,000")
else:
    print("Transaction successful")