# Math
password = "123s"
print(len(password))

if len(password) < 8:
    print(" Your Password is too short! ")

print(".................................")
#count Substring - str method output: int - Returns how often 
# a word apperas in the string.

text = """
Python is easy to learn.
Python is powerful.
Many people love Python.
"""
print(text.count("Python"))
print(text.count("&")) # Achar caracter que nao precisa