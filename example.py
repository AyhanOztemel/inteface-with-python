#explanation
#if you delete any method you will get Implemented error 
#If you delete a method from the interfaceClass, you will still get an error.

from interfaceDecarator import interface_implement
from interfaceClass import IExample,IIExample
    
   
@interface_implement
class ExampleImplementation(IExample,IIExample):
    def method1(self):
        print("method1 implemented")

    def method2(self):
        print("method2 implemented")
    def method3(self):
        print("method3 implemented")
    def method4(self):
        print("method4 implemented")
    def method5(self):
        print("method5 implemented")
    def method6(self):
        print("method6 implemented")
exampleImplementation=ExampleImplementation()
exampleImplementation.method2()
exampleImplementation.method1()

exampleImplementation=ExampleImplementation()
exampleImplementation.method5()
exampleImplementation.method6()
try:
    Example=IExample(10)  #Cannot create instance of class IExample becasue it's Interface
except Exception as e :
    print("Error!!!",e)


