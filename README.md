# PYTHON-STAR-PATTERN-CODE
STAR PATTERN CODE REPOSITORY FOR PYTHON
# 1. Create Rectangle pattern:<br>

```python
for i in range(n):
  for j in range(i+1):
    print("*",end=" ")
  for j in range(i,n):
    print("*",end=" ")
  print(" ")
```
## OUTPUT:

```
* * * * * *  
* * * * * *  
* * * * * *  
* * * * * *  
* * * * * *
```

# 2. Create increasing triangle pattern:<br>

```python
for i in range(n):
    for j in range(i+1): # loop for increasing  triangle
        print("*",end=" ") 
    print(" ")

```
## OUTPUT:

```
*
* *
* * *
* * * *
* * * * *
```

# 3. Create decreasing triangle pattern:<br>

```python
for i in range(n):
    for j in range(i,n): # loop for decreasing triangle
        print("*",end=" ")
    print(" ")

```
## OUTPUT:

```
* * * * *  
  * * * *  
    * * *  
      * *  
        *  
```
# 4. Create left decreasing triangle pattern:<br>

```python
for i in range(n):
    for j in range(i+1): # loop for increasing triangle with space
        print(" ",end=" ")
    for j in range(i,n): # loop for left decreasing triangle
        print("*",end=" ")
    print(" ")

```
## OUTPUT:

```
  * * * * *  
    * * * *  
      * * *  
        * *  
          * 
```

# 5. Create left increasing triangle pattern:<br>

```python
for i in range(n):
    for j in range(i,n): # loop for increasing triangle with space
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print(" ")

```
## OUTPUT:

```
          *
        * *
      * * *
    * * * *
  * * * * *
```

# 6. Create right decreasing triangle pattern:<br>

```python
for i in range(n):
    for j in range(i+1): #left increasing triangle with space
        print(" ",end=" ")
    for j in range(i,n): # left decreasing triangle with space
        print(" ",end=" ")
    for j in range(i,n):  # right decreasing triangle
        print("*",end=" ")
    print(" ")

```
## OUTPUT:

```
            * * * * *  
            * * * *  
            * * *  
            * *
            *
```


# 7. Code for right increasing triangle pattern: <br>

```python
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print(" ")
```
## OUTPUT:

```
            * * * * *  
            * * * *  
            * * *  
            * *
            *
```
