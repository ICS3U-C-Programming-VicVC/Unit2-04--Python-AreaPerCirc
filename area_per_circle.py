#!/usr/bin/env python3
# Created By: Victor V-C
# Date: 09 29, 2026
# This code will calculate the circumference and area of a circle from the radius input of the user


import math


def main():
    # Get Radius from the user
    radius = int(input("Enter Radius of circle (cm): "))

    # Calculate the Circumference and Area from the Radius
    circumference = (math.pi * 2) * radius
    area = math.pi * math.pow(radius, 2)

    # Display the results of Circumference and Area
    print("Circumference of the circle is {:.2f}cm".format(circumference))
    print("Area of Circle is {:.2f}cm²".format(area))


if __name__ == "__main__":
    main()
