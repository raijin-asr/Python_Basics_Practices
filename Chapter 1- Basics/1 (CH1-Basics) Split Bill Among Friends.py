# get input value for total number of friends 
total_friends= int(input("Enter total number of friends: "))

# get input value for bill 
bill= float(input("Enter bill: "))

# calculate the tax amount
tax= (0.2 * bill)

# divide the total bill among friends
total_bill= (tax + bill) / total_friends

# print the split amount
print(total_bill)

# OUTPUT: 
# Enter total number of friends: 5
# Enter bill: 100
# 24.0
