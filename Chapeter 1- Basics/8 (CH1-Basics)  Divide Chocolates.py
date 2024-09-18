# take two integer inputs for chocolates and children
chocolates= int(input())
children= int(input())

# find chocolates each children will get and and print it
get= int(chocolates/ children)
print(get)

# find remaining chocolates and print it
left= chocolates % children
print(left)