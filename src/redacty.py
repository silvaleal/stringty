from decorators import *

class Redacty:
    
    @existFile()
    def rescript(self, filePath, content):
        with open(filePath, 'w') as file:
            file.write(content)