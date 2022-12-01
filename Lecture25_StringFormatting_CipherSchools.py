# string formatting
  # python 2
  # python 3
  # python 3.6 (best)

name = "Satyam"
age = 18
# ugly syntax
print("hello " + name + " your age is " + str(age)) 
 
# python 3 
print("hello {} your age is {}".format(name,age))
print("hello {} your age is {}".format(name,age + 2))

# python 3.6
print(f"hello {name} your age is {age}") 