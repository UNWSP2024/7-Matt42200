import math


def distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2 + (coord2[2] - coord1[2])**2)


def main():
    try:
        x1, y1, z1 = map(float, input("Enter the first 3D point (x1, y1, z1) separated by spaces: ").split())
        coord1 = (x1, y1, z1)


        x2, y2, z2 = map(float, input("Enter the second 3D point (x2, y2, z2) separated by spaces: ").split())
        coord2 = (x2, y2, z2)


        dist = distance(coord1, coord2)


        print(f"The distance between {coord1} and {coord2} is: {dist:.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for the coordinates.")


main()