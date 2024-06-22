#explanation
#if you delete any method you will get Implemented error 
#If you delete a method from the interfaceClass, you will still get an error.

from interfaceDecarator import interface_decorator
from interfaceClass import IClass
    
   
@interface_decorator() 
class MyClass(IClass):#Implements the IClass interface
    def method1(self):
        print("Method-1")

    def method2(self):
        print("Method-2")

    def method3(self):
        print("Method-3")
        
    
    def languages(self):
        print("languages")
  
    def roadmapp(self):
        print("Road map")
        
    
myClass=MyClass()
myClass.roadmapp()
myClass.languages()

