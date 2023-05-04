# define a function to validate if a username is valid
def set_username(user):
    # check if the length of the username is 0 (empty)
    if len(user) == 0:
        # return False if the username is empty
        return False
    #  otherwise, return True 
    return True

# define a function to test the set_username function
def test_valid_username():
    # check if an empty is not a valid username
    assert set_username("") == False
    # check if a non-empty string is a valid username
    assert set_username("testuser") == True

#  print a welcome message
print("Welcome to Mia secret Box!")
# ask the user to set a username and password 
# that are at least 12 characters long 
print("Please set a username and password that is at least 12 characters long.")

#  Loop until the user enters a  valid username and password
while True:
    # ask the user to enter a username
    username = input("Username :) : ")
    # ask the user to enter a password
    password = input("Password :) : ")
    # check if the usernaame is not valid
    if not set_username(username):
        #  if the username is not valid, print an error message
        print("Please enter a valid username.")
    
    # check if the username is less than 12 characters long
    elif len(password) < 12:
        # if so, print an error message 
        print("Your password must be at least 12 characters long. Please try again.")
    else:
        #  if both the username and password are valid, exit the loop
        break

#  print a message to thank th user for setting their password and now check if it matches
print("Thank you for setting your password! Let's check if you remember it.")

# loop until the user enters the correct password
while True:
    # ask the user to re-enter their password
    password_check = input("Please re-enter your password to check if you remember it: ")
    # check if the re-entered password is correct
    if password_check == password:
        # if it's the correct password, print a successful message and exit 
        print("Great! You correctly entered your password.")
        break
    else:
        # if it's not the correct password, print an error message and continue the loop
        print("Sorry, that password is incorrect. Please try again.")
#  call the test_valid_username function to test the set_username function
test_valid_username()
