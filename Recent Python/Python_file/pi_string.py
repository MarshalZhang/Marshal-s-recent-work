filename="pi_digits.txt"
with open(filename) as file_object:
    lines= file_object.readlines()

pi_string=""
for line in lines:
    pi_string+=line.strip()

print(pi_string[:52] +"...")
print(len(pi_string))

birthday= input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first hundred digits of pi")
else:
     print("Your birthdya doea not appear in the first million digits of pi")
