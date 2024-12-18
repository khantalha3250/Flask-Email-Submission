# Documentation: Flask Email Submission Service

This documentation explains the functionality, structure, and usage of a Flask-based application for submitting assignments via email, including file attachments.

---

## 1. Problem Statement
The goal is to create a web service where users can submit assignments or messages through a web form. The submissions are sent as emails, optionally including file attachments.

---

## 2. Features
- User-friendly web interface for form submissions.
- Email functionality with support for CC and file attachments.
- Secure authentication using environment variables for email credentials.

---

## 3. Technology Stack
- **Backend**: Flask (Python web framework)
- **Email Handling**: SMTP (via smtplib) with MIME encoding for attachments
- **HTML Templates**: For rendering the web interface
- **File Management**: File uploads stored temporarily in the server

---

## 4. Approach

### 4.1. Email Sending Functionality
- **Email Setup**:
  - SMTP server: Gmail's SMTP (`smtp.gmail.com`).
  - Port: 587 (TLS).
  - Sender credentials are fetched securely using environment variables (`EMAIL_PASSWORD`).
- **Email Composition**:
  - The email includes the sender, recipient(s), CC, subject, and body.
  - Files are attached using `MIMEBase` with base64 encoding for safe transmission.
- **Email Transmission**:
  - A connection is established using `smtplib.SMTP`.
  - Authentication is performed, and the email is sent using `sendmail()`.

### 4.2. Flask Application Structure
- **Routes**:
  - `/`: Renders the home page (`index.html`), which contains the submission form.
  - `/submit`: Processes form submissions and calls the `send_email` function.
- **Form Handling**:
  - Data from the form (`to`, `cc`, `subject`, `body`) is extracted using `request.form`.
  - Uploaded files are saved in a temporary directory (`uploads`).
  - Files are passed to the `send_email` function for attachment.

---

## 5. Code Workflow
1. **Setup and Configuration**:
   - Import necessary libraries.
   - Configure SMTP settings and email credentials.
2. **Email Function**:
   - Compose and send emails, including attachments, using `send_email()`.
3. **Flask Application**:
   - Serve the form through the home route (`/`).
   - Handle form submissions via the `/submit` route.
4. **File Management**:
   - Save uploaded files in a temporary folder (`uploads`).
   - Attach files to the email before sending.

---

## 6. How to Run

### 6.1 Prerequisites
1. **Python**: Ensure Python (>=3.6) is installed.
2. **Dependencies**: Install Flask and other required packages:
   ```bash
   pip install flask
   ```
3. **Environment Variable**:
   - Set your app password as an environment variable named `app_password`:
     ```bash
     export app_password=your_password_here
     ```

### 6.2 Steps to Run
1. Save the script as `app.py`.
2. Create an `uploads` directory in the same location as the script.
3. Run the Flask application:
   ```bash
   python app.py
   ```
4. Access the application in your browser at `http://127.0.0.1:5000/`.

---

## 9. Conclusion
This Flask application provides a simple and efficient way to submit assignments or messages via email with file attachments. It leverages Flask for the web interface and SMTP for secure email communication, offering a customizable solution for similar use cases.
