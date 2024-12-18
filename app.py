from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

app = Flask(__name__)

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"  # Use your SMTP server
SMTP_PORT = 587
EMAIL_ADDRESS = "khanmohdtalha3250@gmail.com"  # Replace with your email
EMAIL_PASSWORD = os.getenv("app_password")  # Replace with your app password

def send_email():
    # Set up the email
    subject = "Python (Selenium) Assignment - Khan Mohd Talha"
    to_address = "kt7863250@gmail.com"
    cc_address = "ktmt7863250@gmail.com"

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg['Cc'] = cc_address
    msg['Subject'] = subject

    # Email body
    body = """Dear Team,

Please find my submission for the Python (Selenium) assignment attached below. Here are the details:

1. Screenshot: Form filled via the code screenshot is attached below.
2. Source Code: GitHub repository link - [google.com]
3. Documentation: Included in the attached file.
4. Resume: Attached.
5. Work Samples: [Project Link 1], [Project Link 2]
6. Availability: I confirm my availability to work full time (10 am to 7 pm) for the next 3-6 months.

Thank you for considering my application. Let me know if you need any further details.

Best Regards,
[Your Name]
"""

    msg.attach(MIMEText(body, 'plain'))

    # Attachments
    files = [
        "confirmation_page.png",  # Screenshot
        "resume.pdf",             # Resume
        "documentation.txt"       # Documentation
    ]

    for file in files:
        attachment = MIMEBase('application', 'octet-stream')
        with open(file, 'rb') as f:
            attachment.set_payload(f.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file)}')
        msg.attach(attachment)

    # Sending email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, [to_address, cc_address], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Flask route to trigger email
@app.route('/submit', methods=['POST'])
def submit_assignment():
    send_email()
    return jsonify({"status": "success", "message": "Assignment submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
