import turtle
import math

print("Enter the length of leg #1:")
leg_a = float(input("Leg A:"))
print("Enter the length of leg#2:")
leg_b = float(input("Leg B:"))
leg_c = math.sqrt((leg_a ** 2) + (leg_b ** 2) )
alpha_in_radians = math.atan(leg_a / leg_b)
alpha = math.degrees(alpha_in_radians)
beta = 90 - alpha


turtle.forward(leg_a)
turtle.left(90)
turtle.forward(leg_b)
turtle.left(180 - alpha)
turtle.forward(leg_c)
turtle.left(180 - beta)


turtle.hideturtle()
turtle.done()
