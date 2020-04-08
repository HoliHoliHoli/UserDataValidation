import random
import string

""" A program that saves the details of new employees for the HNG organization.
"""

print ("Welcome to the HNG onbording process!")



def password_validation(password):
    print(f'\nYour auto-generated password is {password}')
    change = input('If you want to change the password enter "y", or else enter "n": ')

    if change.lower() == "y":
        print("Password must be \"at least 8 characters\". It is case sensitive.")
        newPassword = input('Enter new password:')
        newPasswordCheck = input('Re-enter new password:')
        if newPassword==newPasswordCheck and len(newPassword) > 7:
            print("New password set")
            password = newPassword
            return password
        else: 
            print("\nNo match or too short. You will need to re-enter password")
            return password_validation(password)
    elif change.lower() == "n":
        print ("Password accepted!")
        return password
    else:
        print("Invalid response.")
        return password_validation(password)


def new_User():
    first = input("\nPlease input your first name: ")
    last = input("Thank You!\nAnd your last name: ")
    email = input("What is your email address? ")

    details = [first, last, email]
    details = [detail.capitalize() for detail in details]


    #No2. password creation
    letters = string.ascii_letters
    extra = ''.join(random.sample(letters, 5))
    password = first[:2] + last[-2:] + extra
    password = password_validation(password)

    details.append(password)
    print(details)
    return details


container = {}  #container for details of onborded employess
new = True
userCount = 1

while new:
    container["User"+str(userCount)] = new_User()
    new = input('\nDo you want to save a new user? Enter "y" for yes and anything else for no: ')
    if new.lower() == "y":
        new = True
    else: break
    userCount += 1

print("\n HNG Onbording complete! Below are the details.")
for item in container.items(): print(item)


