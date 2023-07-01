#An Email Simulation

class Email:
    
    def __init__(self, email_contents, from_address):        
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address
  
    # Return 'has_been_read' to True when function called
    def mark_as_read(self):    
        self.has_been_read = True
    
    # Return 'is_spam' to True when function called
    def mark_as_spam(self):
        self.is_spam = True
    
inbox = []

def add_email(email_contents, from_address):
    new_email = Email(email_contents, from_address)
    inbox.append(new_email)

def get_count():
    return len(inbox)

def get_email(i):
    if user_read == 'all':
        if 0 <= i < len(inbox):
            email = inbox[i]
            email.mark_as_read()
            return email
        else:
            print("Invalid index. Email does not exist.\n")
    
    if user_read == 'unread':
        if 0 <= i < len(unread_box):
            email = unread_box[i]
            email.mark_as_read()
            return email
        else:
            print("Invalid index. Email does not exist.\n")

def get_unread_emails():
    unread_box = []
    for email in inbox:
        if email.has_been_read is False:
            unread_box.append(email)
    return unread_box

def get_spam_emails():
    spam_box = []
    for email in inbox:
        if email.is_spam is True:
            spam_box.append(email)
    return spam_box

def delete(i):
    if 0 <= i < len(inbox):
        del inbox[i]
        print("Email deleted")
    else:
        print("Invalid index. Email does not exist.")
    
# Add dummy emails to inbox
add_email("I am an email 1", "first@gmail.com")
add_email("I am an email 2", "second@gmail.com")
add_email("I am an email 3", "third@gmail.com")
add_email("I am an email 4", "fourth@gmail.com")



user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/quit?: ").lower()
    
    if user_choice == "read":
        user_read = input("What would you like to read - all/unread/spam?: ")
        
        # List of all emails from 'inbox'
        # if none found - prompt user 
        # Prompt user to open email by index
        if user_read == "all":
            print("List of all emails\n")
            
            if len(inbox) == 0:
                print("No emails in inbox.")
            
            else:
                for idx, email in enumerate(inbox):
                    print(f'{idx+1}. {email.email_contents}. Read: {email.has_been_read}. Spam: {email.is_spam}.')
                
                user_mail_idx = int(input("\nWhich email would you like to open from inbox - enter index: ")) - 1
                
                print(f"From: {get_email(user_mail_idx).from_address}")
                print(f"Content: {get_email(user_mail_idx).email_contents}\n")
            
        # List of all emails from 'unread'
        # if none found - prompt user 
        # else prompt user to open email by index
        elif user_read == "unread":
            print("List of unread emails\n")
            unread_box = get_unread_emails()
            
            if len(unread_box) == 0:
                print("No emails unread.")
            
            else:     
                for idx, email in enumerate(unread_box):
                    print(f'{idx+1}. {email.email_contents}. Read: {email.has_been_read}. Spam: {email.is_spam}.')
               
                user_mail_idx = int(input("\nWhich email would you like to open from unread - enter index: ")) - 1
               
                print(f"From: {get_email(user_mail_idx).from_address}")
                print(f"Content: {get_email(user_mail_idx).email_contents}\n")

        # List of all emails from 'spam'
        # if none found - prompt user
        # else prompt user to open email by index
        elif user_read == "spam":
            print("List of spam emails\n")
            spam_box = get_spam_emails()
            
            if len(spam_box) == 0:
                print("No emails marked as spam.")
            
            else:     
                for idx, email in enumerate(spam_box):
                    print(f'{idx+1}. {email.email_contents}. Read: {email.has_been_read}. Spam: {email.is_spam}.')
            
                user_mail_idx = int(input("\nWhich email would you like to open from spam - enter index: ")) - 1
            
                print(f"From: {get_email(user_mail_idx).from_address}")
                print(f"Content: {get_email(user_mail_idx).email_contents}\n")

    # List inbox and prompt user to mark which email is spam
    elif user_choice == "mark spam":
        for idx, email in enumerate(inbox):
            print(f'{idx+1}. {email.email_contents}')
        
        user_mail_idx = int(input("\nWhich email would you like to mark as spam from inbox - enter index: ")) - 1
        inbox[user_mail_idx].mark_as_spam()
        
        print("Email now marked as spam.")

    # 'Send email' - add sent email into inbox
    elif user_choice == "send":
        from_address = input("Enter your email address: ")
        email_contents = input("Enter email content: ")
        add_email(email_contents, from_address)
        print("Email sent successfully!")

    # exit program
    elif user_choice == "quit":
        print("Goodbye")

    # invalid option
    else:
        print("Oops - incorrect input")
