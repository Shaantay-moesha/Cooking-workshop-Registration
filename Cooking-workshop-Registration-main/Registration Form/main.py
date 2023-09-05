import sqlite3
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='templates',static_folder='static')

# Create a rout
@app.route('/register', methods=['GET'])
def show_registration_form():
    return render_template('registration_form.html')

# route to form sub
@app.route('/register', methods=['POST'])
def process_registration():
    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    new_password = request.form.get('new-password')
    cooking_type = request.form.get('cooking-type')
    experience_level = request.form.get('experience-level')
    terms_and_conditions = request.form.get('terms-and-conditions')
    profile_picture = request.files.get('profile-picture')
    age = request.form.get('age')
    how_did_you_hear = request.form.get('how-did-you-hear')
    special_requests = request.form.get('special-requests')
    

    # Connect to the SQLite database
    conn = sqlite3.connect('cooking_workshop.db')
    cursor = conn.cursor()
    if profile_picture is not None:
        # Read the binary data from the file
        profile_picture_data = profile_picture.read()
    else:
        # If no file was provided, set profile_picture_data to None
        profile_picture_data = None

    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS registrations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        new_password TEXT NOT NULL,
                        cooking_type TEXT NOT NULL,
                        experience_level TEXT NOT NULL,
                        terms_and_conditions TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        how_did_you_hear TEXT NOT NULL,
                        special_requests TEXT,
                        profile_picture BLOB  -- Added a BLOB column for the photo

                    )''')

    # Insert the form data into the table
    # Insert the form data including the photo into the table
    cursor.execute('''INSERT INTO registrations
                    (first_name, last_name, email, new_password, cooking_type,
                    experience_level, terms_and_conditions, age,
                    how_did_you_hear, special_requests, profile_picture)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (first_name, last_name, email, new_password, cooking_type,
                    experience_level, terms_and_conditions,
                    age, how_did_you_hear, special_requests, profile_picture_data))


    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return render_template("registration_success.html")

if __name__ == '__main__':
    app.run(debug=True)
