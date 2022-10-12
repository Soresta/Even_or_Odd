# Even or Odd:
# Program that calculates whether the entered number is odd or even.
# Girilen sayının tek mi çift mi olduğunu hesaplayan program.

num = int(input("Enter a number: "))

episode = num // 2
remainder = num - episode * 2

if remainder == 1:
    print("The number you entered is an Odd number")
else:
    print("The number you entered is an Even number")
