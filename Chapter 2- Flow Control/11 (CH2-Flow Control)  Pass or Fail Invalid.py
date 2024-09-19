marks = int(input())

# check if user has entered valid marks or not
# also check if the student passed or failed
if marks not in range(0,101):
    print("Invalid Marks")
elif marks >=40:
    print("Pass")
else:
    print("Fail")