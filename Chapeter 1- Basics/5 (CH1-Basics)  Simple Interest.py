# take float input for principal, rate, and time
principle= float(input())
rate= float(input())
time= float(input())

# calculate the simple interest
simple_interest= principle * time * rate * .01

# calculate the final amount
final_amount= principle + simple_interest

# print interest and total_sum in separate lines
print(simple_interest)
print(final_amount)