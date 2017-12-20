#This app iterates numbers  with a step provided by te user

print("Hello user \nIn what range would you like to iterate?")
beginning = int(input("First number: "))
end = int(input("Last number: "))
step = int(input("step: "))

print("Your numbers are:")
for i in range(beginning, end, step):
    print(i)

print("Thanks!")
