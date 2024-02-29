import math
# This program finds the angle MBC of a right angle triangle with 90 degrees at
# angle B. Given the lengths of sides AB and BC the angle needs to be calculated.
# Input: The first line contains input length of side AB
#        The second line contains input length of side BC.
# Output: Output angle MBC in degrees round to nearest integer.  
side_AB = int(input())
side_BC = int(input())
# Round the calculated degrees to nearest whole number
angle_MBC = round(math.degrees(math.atan(side_AB / side_BC)))
# Print the angle_MBC and also the degree symbol
print(str(angle_MBC), chr(176),sep='')


