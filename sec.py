import random
from colorama import Fore,Style,init,Back

print(Fore.CYAN+Style.BRIGHT+"Hello sir/mam please enter a value in  1 to 10 range")

while True:
    n = int(input(Fore.LIGHTMAGENTA_EX+"Enter a number: "))
    r = random.randint(1,10)
    if (n == r):
        print(Fore.GREEN+Style.BRIGHT+ f"You Win Because computer is {r} and you {n}")
        break
    elif (n > 5):
        print(Fore.YELLOW+f"Sorry! Please Enter minimun value {n}")
        break
    else:
        print(Fore.RED+f"You Loose Because computer is {r} and you {n}")