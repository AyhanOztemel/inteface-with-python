from interfaceDecarator import interface
@interface
class IExample:
    
    def method1(self):pass
    
    def method2(self):        
        pass
    def method3(self):
        pass
    def method4(self):
        pass
    def method7(self):
        pass
@interface
class IIExample(IExample):
    def method5(self):
        pass
    def method6(self):
        pass
 
    
@interface
class IIIExample(IIExample):
    def method8(self):
        pass
    def method9(self):
        pass
#--------------------------------------------

@interface
class I_IV_Example:
    
    def method1(self):pass
    
    def method2(self):        
        pass
    def method3(self):
        pass
    def method4(self):
        pass
    def method7(self):
        pass
@interface
class I_V_Example():
    def method5(self):
        pass
    def method6(self):
        pass
 
    
@interface
class I_VI_Example():
    def method8(self):
        pass
    def method9(self):
        pass
