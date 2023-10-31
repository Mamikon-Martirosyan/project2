try:
    import smtplib
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'smtplib' module:Install it")
    exit()
try:
    from email.mime.text import MIMEText
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'MIMEText' module:Install it")
    exit()
try:
    from email.mime.multipart import MIMEMultipart
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'MIMEMultipart' module:Install it")
    exit()
try:
    import argparse
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'argparse' module:Install it")
    exit()

def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message body
    msg.attach(MIMEText(message, 'plain'))

    # Set up the SMTP server
    smtp_server = "smtp.mail.ru"  # Replace with your SMTP server	
    smtp_port = 587  # Replace with your SMTP port

    try:
        # Create a secure SSL context
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
	
        # Log in to the email server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the SMTP server connection
        server.quit()

        print("Email sent successfully")
    except Exception as e:
        print(f"Email could not be sent. Error: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send an email")
    parser.add_argument("--sender-email", required=True, help="Sender's email address")
    parser.add_argument("--sender-password", required=True, help="Sender's email password")
    parser.add_argument("--recipient-email", required=True, help="Recipient's email address")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--massage", required=True, help="Email message")

    args = parser.parse_args()

    send_email(
        args.sender_email,
        args.sender_password,
        args.recipient_email,
        args.subject,
        args.massage
    )