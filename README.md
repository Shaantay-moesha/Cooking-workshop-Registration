# Cooking-workshop-Registration
The Cooking Workshop Registration project is a web application that uses HTML/CSS/PYTHON  that enables users to register for a cooking workshop. The application provides a user-friendly registration form where participants can input their details and preferences for the workshop. The data submitted by users is stored in a SQLite database for later use and analysis.

Registration Form: The application features a registration form that collects the following information from participants:
        First Name
        Last Name
        Email
        New Password
        Cooking Workshop Type (Italian Cuisine, Asian Delights, French Pastries, Vegan Cooking)
        Cooking Experience Level (Beginner, Intermediate, Advanced)
        Acceptance of Terms and Conditions
        Profile Picture Upload
        Age (Must be 18 years or older)
        How They Heard About the Workshop (Social Media, Friend/Family Referral, Website Advertisement, Other)
        Special Dietary Requirements or Requests

Validation: The form includes client-side and server-side validation to ensure that all required fields are filled out correctly. For instance, the email field must contain a valid email address, the password must follow specific criteria, and the age must be within the accepted range.

Database Storage: Upon successful form submission, the participant's registration details are saved in a SQLite database. This allows for easy retrieval and management of the registered users' information.

## Getting Started

These instructions will help you set up and run the application on your local machine for development and testing purposes.

### Install

- Python (3.6 or higher)
- Flask (Install with `pip install Flask`)
- SQLite3 (already included in Python standard library)


## TO RUN THIS PROGRAM
-This program is running locally: http://127.0.0.1:5000/register
-Clone the project :git clone https://github.com/your-username/cooking-workshop-registration.git
-Go to the directory the project is located
-Run main.py
-Open the url in browser /copy and paste URL

## How to Use
1. Fill out the registration form with your details, including your first name, last name, email, new password, cooking workshop type, experience level, age, how you heard about the workshop, and any special dietary requirements or requests.

2. Accept the terms and conditions by checking the checkbox.

3. Click on the "Register for Cooking Workshop" button to submit your registration.

4. Your registration details will be stored in the SQLite database for further processing.

## HOW TO ACCESS DATABASE
-sqlite3 cooking_workshop.db
- . tables
- .mode column
- .headers on
- SELECT * FROM registrations;   //To show all  data stored in the database



