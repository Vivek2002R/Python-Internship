# Simple Login Application
# Hardcoded username and password(for demonstration purposes)
correct_username = "user123"
correct_password = "pass456"

#input from the user
input_username = input("Enter Your Username:")
input_password = input("Enter Your Password:")

#Decision-making statements to check login credentials
if input_username == correct_username and input_password == correct_password:
    print("Login Successful ! Welcome,"+ correct_username + ".")
else:
    print("Login Failed. Please Check Your Username And Password")