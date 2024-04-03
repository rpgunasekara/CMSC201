"""
File: cannon_ball.py
Author: Ravindu Gunasekara
Date: 09/11/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
  Asks for a velocity and an angle (in degrees).
  Calculates the distance based on the inputs.
"""
import math

velocity = float(input("Enter the initial velocity (V0): "))
angle = float(input("Enter the angle in degrees that you will fire the cannon: "))
print(f"The distance the cannon ball will travel is {((velocity ** 2) * (math.sin((angle * 2) * (math.pi) / (180)))) / (9.8)} meters.")
