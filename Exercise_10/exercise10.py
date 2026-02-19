#Functions with outputs
#Changing case of Name using function
''' 
def format_name(first, last):
    f_name = first.title()
    l_name = last.title()
    return f_name +" "+ l_name

firstName = input("Enter your First Name: ")
lastName = input("Enter your Last Name: ")
formatted_Name = format_name(first=firstName, last=lastName)
print(formatted_Name)
'''
from  asciiart import logo, image
print(logo)
print(image)

