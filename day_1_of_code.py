#1. Creating the greeting for my program
print("Hello there! Welcome to the Band Name generator")

#2. Asking user for the city they grew up in
city = input("What city did you grow up in? \n" )

#3. Asking user for the name of their pet
pet = input("What is your pet's name? \n")

#4. combining the names of city an dpet to create their band name
band_name = city + " " + pet
Band_name = pet + " " + city
print("Your band name could be " + band_name.title() + "\nAltenatively it could be " + Band_name.title())