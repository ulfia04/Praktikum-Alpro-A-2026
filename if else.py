a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

is_logged_in = True
if is_logged_in:
  print("Welcome back!")

  #Elif Statement
  a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  #Multiple Elif Statements
  score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#Short Hand If
a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#Practical Examples
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#Python Logical Operators
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#The or Operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Nested If
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#How Nested If Works
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

#Pass Statement
a = 33
b = 200

if b > a:
  pass

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

   a = 5
b = 2
if a > b: print("a is greater than b")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")