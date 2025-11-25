import re 
def is_email_valid(email):
    email_regex=r'^[A-Za-z0-9_.+-]+@+[A-Za-z0-9-]+\.[A-Za-z0-9._]+$'

    if re.match(email_regex,email):
        return True
    else:
        return False 

def main():
    email=input("Enter the email : ")
    if is_email_valid(email):
        print("The email is valid ")
    else:
        print("Invalid email...!")

if __name__=="__main__":
    main()

