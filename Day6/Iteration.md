# For Loop Basics: 
## Write a for loop to print numbers from 1 to 10.

for i in range(1,11):
    print(i)


# String Iteration: 
## Write a program that counts vowels in a string.

str = "czechoslovakia" 
count =0
for i in str:
    if i in "aeiou":
        count += 1
print(count)

# Accumulator Pattern: 
## Calculate the sum of squares from 1 to 100.

total = 0
for i in range(1,101):
    total += i*i
print(total)

# Nested Loops: 
## Create a multiplication table up to 10x10.

for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} ={i*j}")

# Image Processing: 
## Use PIL to invert the colors of an image.


