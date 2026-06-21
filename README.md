# CodeAlpha_SecureCodingReview

## Project Overview

This project was completed as part of the CodeAlpha Cyber Security Internship Program.

The objective of this task is to perform a secure coding review of a Python-based login application, identify security vulnerabilities, and implement secure coding practices to mitigate security risks.

---

## Technologies Used

- Python 3
- SQLite3
- VS Code

---

## Project Files

### vulnerable_login.py
A vulnerable login application that directly inserts user input into SQL queries, making it susceptible to SQL Injection attacks.

### secure_login.py
An improved version of the login application that uses parameterized queries and exception handling to prevent security vulnerabilities.

### create_db.py
Creates the SQLite database and inserts sample user credentials for testing purposes.

---

## Vulnerabilities Identified

### 1. SQL Injection (High)
User input is directly concatenated into SQL queries, allowing attackers to manipulate database queries.

### 2. Plain Text Password Storage (High)
Passwords are stored and compared in plain text without encryption or hashing.

### 3. Missing Input Validation (Medium)
User inputs are not validated before processing.

### 4. Missing Error Handling (Medium)
Application crashes may expose internal system information.

### 5. Missing Logging (Low)
Authentication attempts are not logged for auditing and monitoring.

---

## Security Improvements Implemented

- Parameterized SQL Queries
- Exception Handling using try-except blocks
- Secure Coding Recommendations
- Improved Authentication Logic

---

## Screenshots

Project screenshots demonstrating:
- Vulnerable Code Review
- Login Failure Scenario
- Login Success Scenario
- Secure Code Implementation
- Secure Application Execution

---

## How to Run

### Step 1

Run database creation script:

```bash
python create_db.py
```

### Step 2

Run vulnerable application:

```bash
python vulnerable_login.py
```

### Step 3

Run secure application:

```bash
python secure_login.py
```

---

## Conclusion

The secure coding review identified several vulnerabilities within the login application. The most critical issue was SQL Injection. A secure version of the application was developed using parameterized queries and exception handling, significantly improving the security posture of the application.

---

## Author

**Deney Dasari**

CodeAlpha Cyber Security Internship – Task 3
