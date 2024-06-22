def interface_decorator():
    import inspect
    def decorator(cls):
        
        # Get the base class (super class)
        base_class = cls.__bases__[0]
        
        # Check if class is interface by name
        is_abstract = base_class.__name__.startswith('I')
        
        # Get methods defined in the base class
        interface_methods = {method_name for method_name, _ in inspect.getmembers(base_class, inspect.isfunction)}
        print("interface_methods----->",interface_methods)
               
        # Get methods defined in the implemantation class
        cls_methods = {method_name for method_name, _ in cls.__dict__.items() if inspect.isfunction(_)}
        print("cls_methods----->",cls_methods)
        
        # is the base class  interface and the methods defined in the implemantation class
        if is_abstract:
            for method_name in interface_methods:
               
                if method_name not in cls_methods:
                
                    raise NotImplementedError(f"Concrete class {cls.__name__} does not implement method {method_name} defined in {base_class.__name__}")
        else:
                    raise NotImplementedError(f"Interface must start with I, {base_class.__name__} does not comply with interface definition")
        return cls
    return decorator
