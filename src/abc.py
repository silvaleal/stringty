from redacty import Redacty

content = """a = "abc"


print(a)"""

Redacty().rescript("test.py", content)