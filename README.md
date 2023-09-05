# Cooking-workshop-Registration
The Cooking Workshop Registration project is a web application that uses HTML/CSS/PYTHON/JAVASCRIPT that enables users to register for a cooking workshop. The application provides a user-friendly registration form where participants can input their details and preferences for the workshop. The data submitted by users is stored in a SQLite database for later use and analysis.

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

## Validation
The form includes client-side and server-side validation to ensure that all required fields are filled out correctly. For instance, the email field must contain a valid email address, the password must follow specific criteria, and the age must be within the accepted range.

## Database Storage
Upon successful form submission, the participant's registration details are saved in a SQLite database. This allows for easy retrieval and management of the registered users' information.

## JavaScript Functionality
JavaScript (JS) is used to enhance the user experience and provide additional functionality to the registration form:

-**Clear Form Button:** A "Clear Form" button is included in the form, allowing users to reset all form fields to their default values with a single click. This functionality is implemented using JS.

-**Registration Success Alert:** After successfully submitting the registration form, users receive a pop-up alert notifying them of their successful registration. This alert is displayed using JS and provides instant feedback to users.

## Getting Started
To run this project locally, follow these steps:
1. Install Python (3.6 or higher).
2. Install Flask by running `pip install Flask`.
3. Clone the project repository using `git clone https://github.com/your-username/cooking-workshop-registration.git`.
4. Navigate to the project directory.
5. Run `main.py`.
6. Open your web browser and access the application at `http://127.0.0.1:5000/register`.

## Accessing the Database
To access the SQLite database and view the stored registration data:
1. Open your terminal.
2. Navigate to the project directory.
3. Run `sqlite3 cooking_workshop.db` to start the SQLite shell.
4. Use the following commands to interact with the database:
   - `.tables` to list available tables.
   - `.mode column` and `.headers on` for a more structured output.
   - `SELECT * FROM registrations;` to view all the data stored in the database.



