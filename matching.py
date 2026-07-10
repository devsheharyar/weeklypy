##### Parking Problem Solver
print("Welcom to our Parking System.\nWe are Glade to have you here.")
print("How can we help you? Select one from the following.")
print("1. For new Parking ticket\n2. for checkout from parking\n3. for avalible space status.\n4. for exit.")

with open("geek.txt","a") as file:
    file.write("Hello Pakistan")
    print("good")

try:
    with open("geeke","r") as file:
     file.write("so good")
     print("Working")
except FileNotFoundError as e:
    print("Error",e)
finally:
    file.close()



"""
file=open("geek.txt","r")
file
content=file.read()
print(content)
print("Filename",file.name)
print("Filemode",file.mode)
print("Is closed",file.closed)

file.close()
"""