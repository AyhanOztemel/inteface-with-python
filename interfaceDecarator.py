import inspect
import re

def interface(cls):
    
    if cls.__new__:                 
            cls.__init__ = None  #Base class initializer cancel
            
    if not cls.__name__.startswith('I'):
        raise ValueError("Interface class names must start with 'I'")
    
    for name, method in cls.__dict__.items():
        
        if callable(method) and not name.startswith('__'):
            # Check the source code of the method
            source = inspect.getsource(method).strip()
            # Remove spaces and newlines
            source = ' '.join(source.split())
            # Check if the method just has the format 'def method_name(self): pass
            if not re.match(r'^def \w+\(self\): ?pass$', source):
                raise ValueError(f"Method '{name}' in interface {cls.__name__} must only contain 'pass'")
            
            # Metodu işlevsiz hale getir
            setattr(cls, name, lambda *args, **kwargs: None)
    
   
    return cls
           
def interface_implement(cls):
    def check_interface(cls):
        def new_init(self):pass #Reverting base initializer instance
            
        cls.__init__ = new_init   
        # Miras alınan sınıfları kontrol et
        bases = [base for base in cls.__bases__ if base.__name__.startswith('I')]
        if not bases:
            raise TypeError(f"With @interface_implement the decore {cls.__name__} class must inherit an interface starting with 'I'.")

        # Her bir miras alınan interface için
        for base in bases:
            # Interface'in tüm metodlarını kontrol et
            for name, method in base.__dict__.items():
                if callable(method) and not name.startswith('__'):
                    # Eğer metod implement edilmemişse hata ver
                    if name not in cls.__dict__:
                        raise NotImplementedError(f"With @interface_implement, the decore {cls.__name__} class must implement the {name} method from the {base.__name__} interface.")
        return True

    if check_interface(cls):
        return cls

