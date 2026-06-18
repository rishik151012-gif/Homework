name = input("What is your name? ")
print(f"\nHello, {name}! Welcome to the app! 😊")

first_time = input("Is this your first time with us? (yes/no): ").lower()

if first_time == "no":
    print(f"Welcome, {name}!  i think you don't know what to do. 😄")
elif first_time == "yes":
    print(f"Welcome, {name}! Let's get you started right away. 🚀")
else:
    print("Please enter only 'yes' or 'no'.")