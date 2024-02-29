# This program given dimensions of a cuboid x,y,z in integer and an integer n prints
# all possible co-ordinates of the cuboid where i+j+k would not be equal to n.
# Input: In separate lines, integer values of x,y,z and n
# Output: Permutations of all possible values of x,y,z not equal to n
x = int(input())
y = int(input())
z = int(input())
n = int(input())
permutations = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
valid_permutations = [perm for perm in permutations if sum(perm) != n]
print(valid_permutations)