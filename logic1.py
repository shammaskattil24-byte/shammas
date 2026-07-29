# num = int(input("Enter a number: "))

# if num <= 1:
#     print("Not Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
        
        
# s=5
# for i in range(1,s+1):
#     for j in range(s-i):
#         print (" ",end="")
#     for l in range(2 * i -1 ):
#         print("*", end = "")
#     print()
# s=5
# for i in range(s,0,-1):
#     for j in range(s-i):
#         print (" ",end="")
#     for l in range(2 * i -1 ):
#         print("*" , end = "")
#     print()
    
    
    
nums = [10, 20, 30, 40, 50]

left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print(nums)