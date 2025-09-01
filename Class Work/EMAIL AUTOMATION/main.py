import emaillogic 

subject = input("Enter the email subject: ")
body = input("Enter the email body: ")

choice = input("Do you want to send (1) Single Email or (2) Bulk Email? Enter 1 or 2: ")

if choice == '1':
    recipient = input("Enter the recipient email: ")
    emaillogic.send_email(recipient, subject, body)

elif choice == '2':
    csv_file = input("Enter the path to the CSV file with email addresses: ")
    emaillogic.send_bulk_emails(csv_file, subject, body)
else:
    print("Invalid choice! Please enter 1 or 2.")
