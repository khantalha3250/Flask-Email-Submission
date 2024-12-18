from flask import Flask, request, jsonify, render_template
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

def send_email(to_address, cc_address, subject, body, files):
    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg['Cc'] = cc_address
    msg['Subject'] = subject

    # Email body
    msg.attach(MIMEText(body, 'plain'))

    # Attach files
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

# Home route for form submission
@app.route('/')
def home():
    return render_template('index.html')

# Submit route to send email
@app.route('/submit', methods=['POST'])
def submit_assignment():
    to_address = request.form['to']
    cc_address = request.form['cc']
    subject = request.form['subject']
    body = request.form['body']

    # Handle file uploads
    files = []
    for file in request.files.getlist('files'):
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)
        files.append(file_path)

    send_email(to_address, cc_address, subject, body, files)
    
    return jsonify({"status": "success", "message": "Assignment submitted successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
