from .decorators import *

class Stringty:
    
    @existFile()
    def rescript(self, filePath, content):
        with open(filePath, 'w', encoding='utf-8') as file:
            file.write(content)
            
    def imprement(self, filePath, content):
        with open(filePath, 'a+', encoding='utf-8') as file:
            file.write("\n"+content)