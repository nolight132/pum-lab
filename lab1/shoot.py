import math
import random

v0 = 50
h = 100
g = 9.81

target_distance = random.uniform(50, 340)
print(f"Target spotted at {target_distance:.2f} meters!")

tries = 0
hit = False

while not hit:
    angle_deg = float(input("Enter launch angle in degrees: "))
    tries += 1

    alpha = math.radians(angle_deg)

    vx = v0 * math.cos(alpha)
    vy = v0 * math.sin(alpha)

    term1 = vy
    term2 = math.sqrt(vy**2 + 2 * g * h)
    t_flight = (term1 + term2) / g

    d = vx * t_flight
    print(f"The projectile landed at {d:.2f} meters.")

    if abs(d - target_distance) <= 5:
        print(f"Target hit! Total tries: {tries}")
        hit = True
    else:
        if d < target_distance:
            print("Too short!")
        else:
            print("Too far!")
