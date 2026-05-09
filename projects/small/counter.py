# Take user input
# Add the input to counter

counter = 0
number = int(input("Enter a number: "))

while True:
    counter += number
    print("Current counter is:", counter)
    number = int(input("Enter a number: "))
