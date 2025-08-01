# Types String
"""
TRANSFORMATIONS.
    replace - old to new --- 
"""

price = "1234,56"
print(price.replace(",", "."))
print("_____________________")

phone = "176-1234-56"
print(phone.replace("-", "/"))
print("_____________________")

phone = "176-1234-56"
print(phone.replace("-", " "))
print("_____________________")
price = "$1,299.99"
print(price.replace("$", "R$") .replace(",", "") .replace(".", ",") )


