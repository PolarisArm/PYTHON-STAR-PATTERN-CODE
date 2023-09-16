n = 5

#print rectangle pattern
for i in range(n):
    for j in range(i+1): # loop for increasing  triangle
        print("*",end=" ") 
    for j in range(i,n): # loop for decreasing triangle
        print("*",end=" ")
    print(" ")


print("LEFT decreasing triangle")
print("-------------------------")
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print(" ")

print("Right decreasing triangle")
print("-------------------------")
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print(" ")

print("left increasing triangle")
print("-------------------------")
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("#",end=" ")
    print(" ")

print("Right increasing triangle")
print("-------------------------")
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

