#class Student:
 #  name = "bhawana"
#s1 = Student()
#print(s1)
#print(s1.name)

#s2 = Student()
#print(s2.name)


#class Student:
 #   def __init__( self, name, marks):
 #     self.name = name
 #     self.marks = marks

 #   def get_avg(self):
  #      sum = 0
  #      for val in self.marks:
  #          sum += val
  #      print("hi", self.name , "your avg score:",sum/len(self.marks))
#s1 = Student("bhawana",[85,39,98])
#s1.get_avg()

#class Student:
#   def __init__( self, name, marks):
#    self.name = name
#     self.marks = marks
#   @staticmethod
#   def hello():
#      print("hello")

#  def get_avg(self):
#      sum = 0
#       for val in self.marks:
#          sum += val
#       print("hi", self.name , "your avg score:",sum/3)
#s1 = Student("bhawana",[85,39,98])
#s1.get_avg()
#s1.hello()


#class Student:
  #  def __init__(self, name):
 #       self.name = name

#s1 = Student("bhawana")
#print(s1.name)
#del s1.name
#print(s1.name)

class Car:
   color = "black"
   @staticmethod
   def start():
       print("car started..")
   def stop():
       print("car stoped..")
class ToyotaCar(Car):
   def __init__(self, name):
         self.name = name
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("puris")
print(car1.name)
print(car1.start())
print(car1.color)


