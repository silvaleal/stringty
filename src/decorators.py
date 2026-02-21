import os

def existFile():
    def decorator(func):
        def wrapper(self, filePath, *args, **kwargs):
            if not os.path.exists(filePath):
                raise FileNotFoundError("File not exists")
            
            return func(self, filePath, *args, **kwargs)
        return wrapper
    return decorator