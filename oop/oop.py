class Student(object):
   test = 10;
   def __init__(self,name,roll_no):
      self.name =  name
      self.roll_no = roll_no

   def inst(self):
      print self.name+'   '+self.roll_no

   def retobj(self):
   	  print self

   def okman(self,data1,data2=0):
       print data1+'  '+data2

   def hobnob(self):
       print Student.test

   @classmethod
   def methclass(cls):
      print cls.test



t1 = Student('sharad','66088')
print t1
print t1.inst()
t1.okman(50,20)
print t1.hobnob()


# print t1
# t1.inst()
#t1.methclass()
# print t1.name
