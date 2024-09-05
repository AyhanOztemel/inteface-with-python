
#explanation
#if you delete any method you will get Implemented error 
#If you delete a method from the interfaceClass, you will still get an error.
from typeguard import typechecked
from interfaceDecarator import interface_implement
from interfaceClass import IExample,IIExample,IIIExample,I_IV_Example,I_V_Example,I_VI_Example

@typechecked
def type_safe_checked(class_name:IIExample):
    print("gelen class referance--->",class_name)

@typechecked
def type_safe_checked2(class_name:I_VI_Example):
    print("gelen class referance--->",class_name)
    
@interface_implement
class ExampleImplementation(IIIExample):
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
    def method7(self):
        print("method7 implemented")
    def method8(self):
        print("method8 implemented")
    def method9(self):
        print("method9 implemented")
    def method10(self):
        print("method9 implemented")

    
exampleImplementation=ExampleImplementation()
exampleImplementation.method2()
exampleImplementation.method1()
exampleImplementation.method8()
exampleImplementation2=ExampleImplementation()
exampleImplementation2.method5()
exampleImplementation2.method6()
exampleImplementation2.method9()

try:
    Example=IExample()   #Cannot create instance of class IExample becasue it's Interface
except Exception as e :  #e='NoneType' object is not callable
    print("Error!!!",e)

try:
    Example2=IIExample()   #Cannot create instance of class IExample becasue it's Interface
except Exception as e :    #e='NoneType' object is not callable
    print("Error!!!",e)
try:
    Example3=IIIExample()  #Cannot create instance of class IExample becasue it's Interface
except Exception as e :    #e='NoneType' object is not callable
    print("Error!!!",e)

@interface_implement
class ExampleImplementation2(I_IV_Example,I_V_Example,I_VI_Example):
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
    def method7(self):
        print("method7 implemented")
    def method8(self):
        print("method8 implemented")
    def method9(self):
        print("method9 implemented")
    def method10(self):
        print("method9 implemented")
print("------------------------------------------------------------")
exampleImplementation3=ExampleImplementation2()
exampleImplementation3.method3()
exampleImplementation3.method4()
exampleImplementation3.method9()
exampleImplementation4=ExampleImplementation2()
exampleImplementation4.method5()
exampleImplementation4.method7()
exampleImplementation4.method9()
print("------------------------------------------------------------")
try:
    Example=I_IV_Example()   #Cannot create instance of class IExample becasue it's Interface
except Exception as e :      #e='NoneType' object is not callable
    print("Error!!!",e)

try:
    Example2=I_V_Example()   #Cannot create instance of class IExample becasue it's Interface
except Exception as e :      #e='NoneType' object is not callable
    print("Error!!!",e)
try:
    Example3=I_VI_Example()  #Cannot create instance of class IExample becasue it's Interface
except Exception as e :      #e='NoneType' object is not callable
    print("Error!!!",e)

           #-------------REFERENCE CHECK---------------
    
print("------------------------------------------------------------")
try:
    type_safe_checked(ExampleImplementation()) #true class send
except Exception as e :  
    print("Error!!!",e)
try:
    type_safe_checked(ExampleImplementation2()) #false class send
except Exception as e :  
    print("Error!!!",e)
print("------------------------------------------------------------")

try:
    type_safe_checked2(ExampleImplementation2())  #true class send
except Exception as e :  
    print("Error!!!",e)
try:
    type_safe_checked2(ExampleImplementation())  #false class send
except Exception as e :  
    print("Error!!!",e)
#------------------------------------------------------------
