"""x = int(input("Tell me a number: \n"))
if x % 2 == 0:
    if x % 3 == 0:
        print(f"{x} is divisible by 2 and 3")
    else:
        print(f"{x} is divisible by 2 but not 3")
elif x % 3 == 0:
    print(f"{x} is dvisible by 3 but not 2")"""
    
x = int(input("Tell me a number:\n"))
y = int(input("Tell me a number:\n"))
omega = x if x > y else y
print(omega)