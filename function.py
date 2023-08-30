# def calculateGmean(a,b):
#     mean = (a*b)/(a+b)
#     print(mean)
    
# a = 9 
# b = 8
# c = 4
# d = 2



# def isGreater(a, b):
#     if(a > b):
#         print("first is greater")
#     else:
#         print("second number is greater or equal")
# def isLesser(a,b):
#     pass

# if(a > b):
#     print("first is greater")
# else:
#     print("second number is greater or equal")


# calculateGmean(a,b)
# isGreater(a,b)
# calculateGmean(c,d)
# isGreater(c,d)

# if(c > d):
#     print("first is greater")
# else:
#     print("second number is greater or equal")


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is : " , sum / len(numbers))
    return sum / len(numbers)

c = average (5, 6, 1,7)
print(c)


