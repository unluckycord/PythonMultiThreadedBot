import string
import secrets

def PasswordGenerator(PasswordLength):

    #creates entire alphabet and number sequence    
    alphabet = string.ascii_letters + string.digits

    while True:
        #randomly picks chars and nums to use in password
        password = ''.join(secrets.choice(alphabet)for i in range(PasswordLength))

        #checks strength of password
        if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
            break

    #returns password to be used
    return password

if __name__ == "__main__":
    print(PasswordGenerator(30))