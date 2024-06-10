def interface_decorator(interface):
    def decorator(cls):   
        for method_name in dir(cls):
            if callable(getattr(cls, method_name)) and not hasattr(interface, method_name):
                raise NotImplementedError(f"Class {cls.__name__} implements method {method_name} not defined in MyInterface")
        for method_name in dir(interface):
            if callable(getattr(interface, method_name)) and not hasattr(cls, method_name):
                raise NotImplementedError(f"Class {cls.__name__} does not implement method {method_name}")
        return cls
    return decorator
