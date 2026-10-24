def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y 


print ("+")
print ("-")
print ("*")
print ("/")

while True:
    choice = input("tyui")

    if choice in ('+', '-', '*', '/'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '+':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '-':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '*':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '/':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        next_calculation = input("again? y/n ")
        if next_calculation.lower() != 'y':
            break
    else:
        print("Invaslid")
        

@tasks.loop(seconds=0.1)
async def timed_message():
    channel = client.get_channel(CHANNEL_ID)

    if channel is not None:
        await channel.send("<@995055171891642498>")
    