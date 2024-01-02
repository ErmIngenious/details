# asks user to input 2 details: 
# starts with asking for users first name and then surname
# stores them in the relevant variable name for access
name = input("First name:")
surname = input("Last name:")

#concatenated fstrings using variables
full_name = (f'{name} {surname}')

#request and store users age  and gender in variables relevently named age and gender.
age = input("Age?")
gender = input(" Are you M or F?")

#collect and store user address in variable.
house_number = input("House Number")
street_name = input("Street name?")

#using f-strings concatentates all details together to form a sentence.
print (f"This is {full_name}. {name} is a {age} year old {gender} who lives at number {house_number} on {street_name}")
