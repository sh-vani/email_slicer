email_id=input("Enter your email id=").strip() # strip() remove spaces before the email id and after email id 
user_name=email_id[:email_id.index('@')]
domain=email_id[email_id.index('@')+1:]
print(f"Your username is {user_name} and domain name is {domain}")