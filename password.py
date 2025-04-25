import re
#which allows pattern matching and searching within strings.
def check_password_strength(password):
    #check the length
    if len(password) < 6:
        print('weak password, must be atleast six characters')
        return
    # Condition 2: Check if it contains only letters or only numbers
    if password.isalpha() or password.isdigit():
        print("Moderate password! Try adding symbols or numbers.")
        return
        
    # Condition 3: Check if it contains letters, numbers, and special characters
    if re.search(r"[a-zA-Z]", password) and re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password):
        print('strong password: good job')
        return
    
#loops continously
while True:
    password = input('Enter your password (or type exit to quit)')
    if password.lower() == 'exit':
        print('goodbye')
        break
    else:
        check_password_strength(password)