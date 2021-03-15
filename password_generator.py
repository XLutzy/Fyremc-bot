import random

password_list = []
numbers = ["0","1","2","3","4","5","6","7","8","9"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
capital_letters= ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
special_characters = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']


lenght = int(input("How long should the password be?: "))

user1 = input("Should there be letters in it? (y or n): ")
if user1 == "y":
    password_list.extend(letters)


user2 = input("Should it be capitalized? (y or n): ")
if user2 == "y":
    password_list.extend(capital_letters)

user3 = input("Should there be numbers in it? (y or n): ")
if user3 == "y":
    password_list.extend(numbers)

user4 = input("Should there be special characters in it? (y or n): ")
if user4 == "y":
    password_list.extend(special_characters)    

password_list_list = random.choices(password_list, k = lenght)
password = "".join(password_list_list)


print("The password: " + password)

input()

