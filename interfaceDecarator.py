import inspect
import re

def interface(cls):
    if cls.__new__:                 
        cls.__init__ = None  # Base class initializer cancel
            
    if not cls.__name__.startswith('I'):
        raise ValueError("Interface class names must start with 'I'")
    
    # Tüm miras alınan interface'leri topla
    all_bases = set()
    def collect_bases(base):
        all_bases.add(base)
        for parent in base.__bases__:
            if parent.__name__.startswith('I'):
                collect_bases(parent)
    
    for base in cls.__bases__:
        if base.__name__.startswith('I'):
            collect_bases(base)
    
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
    
    # Tüm miras alınan interface'lerin metodlarını ekle
    for base in all_bases:
        for name, method in base.__dict__.items():
            if callable(method) and not name.startswith('__') and name not in cls.__dict__:
                setattr(cls, name, lambda *args, **kwargs: None)
    
    return cls

def interface_implement(cls):
    def new_init(self):
        pass  # Reverting base initializer instance
        
    cls.__init__ = new_init   
    
    # Tüm miras alınan interface'leri topla
    all_interfaces = set()
    def collect_interfaces(base):
        if base.__name__.startswith('I'):
            all_interfaces.add(base)
            for parent in base.__bases__:
                collect_interfaces(parent)
    
    for base in cls.__bases__:
        collect_interfaces(base)
    
    # Her bir interface için
    for interface in all_interfaces:
        # Interface'in tüm metodlarını kontrol et
        for name, method in interface.__dict__.items():
            if callable(method) and not name.startswith('__'):
                # Eğer metod implement edilmemişse hata ver
                if name not in cls.__dict__:
                    raise NotImplementedError(f"The class {cls.__name__} must implement the {name} method from the {interface.__name__} interface.")
    return cls
