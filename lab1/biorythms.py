import math
from datetime import date

name = input("Enter your name: ")
year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))

birth_date = date(year, month, day)
today = date.today()
t = (today - birth_date).days

print(f"Hello {name}! Today is day {t} of your life.")

phys = math.sin((2 * math.pi / 23) * t)
emot = math.sin((2 * math.pi / 28) * t)
intel = math.sin((2 * math.pi / 33) * t)

print(f"Physical: {phys:.2f}")
print(f"Emotional: {emot:.2f}")
print(f"Intellectual: {intel:.2f}")

results = [("Physical", phys, 23), ("Emotional", emot, 28), ("Intellectual", intel, 33)]

for label, value, period in results:
    if value > 0.5:
        print(f"Your {label} score is high.")
    elif value < -0.5:
        print(f"Your {label} score is low.")
        tomorrow_val = math.sin((2 * math.pi / period) * (t + 1))
        if tomorrow_val > value:
            print(f"Don't worry, your {label} state will be better tomorrow!")
        else:
            print(
                f"The {label} cycle is still trending down, tomorrow will be worse :("
            )
