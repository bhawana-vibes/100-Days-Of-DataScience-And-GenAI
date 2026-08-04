#f = open("demo.txt", "r+")
#f.write("\n i am bhawana hirnwal")
#print(f.read())
#f.close()

#with open("demo.txt","r") as f:
 #  data = f.read()
 #  print(data)

#import os

#with open("practice.txt","w") as f:
#    f.write("Hi everyone\nwe are learning python\ntopic on file input and output")

with open("practice.txt","r") as f:
      data = f.read()

new_data = data.replace("python","java")
print(new_data)


