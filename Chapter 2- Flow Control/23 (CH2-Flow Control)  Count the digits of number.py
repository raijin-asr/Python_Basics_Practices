number = int(input())

count = 0

# run loop as long as number != 0
while (number!=0):
    # divide number by 10
    number= number//10 #floor division
      
    # increase count by 1
    count+=1

# print count
print(count)