from flask import Flask, request, jsonify, render_template, url_for, session
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contactform.html')
def get_users_interested_in_service(service_name):
    users = []
    with open('user_interest.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['service_name'] == service_name:
                users.append(row['username'])
    return users

@app.route('/get-interested-users', methods=['POST'])
def get_interested_users():
    service_name = request.json.get('service_name')
    users = get_users_interested_in_service(service_name)
    return jsonify(users)

# Ensure the CSV file exists for users
if not os.path.exists('users.csv'):
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'password'])  # Headers

# Ensure the CSV file exists for storing user interest
if not os.path.exists('user_interest.csv'):
    with open('user_interest.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'service_name'])  # Headers

# Render Home page (signup/login)
@app.route('/')
def home():
    return render_template('index.html')

# Handle User Signup
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"status": "error", "message": "Missing username or password"}), 400

    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                return jsonify({"status": "error", "message": "User already exists"}), 400

    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])

    return jsonify({"status": "success", "message": "User signed up successfully"})

# Handle User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"status": "error", "message": "Missing username or password"}), 400

    with open('users.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return jsonify({
                    "status": "success",
                    "message": "Login successful",
                    "redirect": url_for('dashboard', username=username)
                })

    return jsonify({"status": "error", "message": "Invalid username or password"}), 401

# Render Dashboard for the logged-in user
@app.route('/dashboard/<username>')
def dashboard(username):
    return render_template('dashboard.html', username=username)

# Store User Interest in a service
@app.route('/store-interest', methods=['POST'])
def store_interest():
    data = request.json
    username = data.get('username')
    service_name = data.get('service_name')

    if not username or not service_name:
        return jsonify({"status": "error", "message": "Missing username or service name"}), 400

    # Check if the entry already exists
    with open('user_interest.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == service_name:
                return jsonify({"status": "error", "message": "Already marked as interested"}), 400

    # Add the new interest
    with open('user_interest.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, service_name])

    return jsonify({"status": "success", "message": "Marked as interested"})

# Get users interested in a particular service
@app.route('/fetch-interested-users', methods=['POST'])
def fetch_interested_users():
    data = request.json
    service_name = data.get('service_name')

    if not service_name:
        return jsonify({"status": "error", "message": "Missing service name"}), 400

    # Read the user interest data
    with open('user_interest.csv', 'r') as file:
        reader = csv.reader(file)
        interested_users = [row[0] for row in reader if row[1] == service_name]

    return jsonify({"status": "success", "users": interested_users})

# Toggle User Interest (Add/Remove Interest)
@app.route('/toggle-interest', methods=['POST'])
def toggle_interest():
    data = request.json
    username = data.get('username')
    service_name = data.get('service_name')
    interested = data.get('interested')

    if not username or not service_name:
        return jsonify({"status": "error", "message": "Missing username or service name"}), 400

    # Read the current interest data to check for existing records
    with open('user_interest.csv', 'r') as file:
        reader = csv.reader(file)
        existing_records = list(reader)

    # If the user is interested, add their record
    if interested:
        for row in existing_records:
            if row[0] == username and row[1] == service_name:
                return jsonify({"status": "error", "message": "Already marked as interested"}), 400
        
        with open('user_interest.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, service_name])

        return jsonify({"status": "success", "message": "Marked as interested"})
    
    # If the user unchecks, remove their record
    else:
        with open('user_interest.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for row in existing_records:
                if row[0] != username or row[1] != service_name:
                    writer.writerow(row)
        
        return jsonify({"status": "success", "message": "Removed interest"})
# Store Collaboration Request
@app.route('/collaborate', methods=['POST'])
def collaborate():
    data = request.json
    username = data.get('username')
    collaborator_username = data.get('collaborator_username')
    service_name = data.get('service_name')

    if not username or not collaborator_username or not service_name:
        return jsonify({"status": "error", "message": "Missing information"}), 400

    # Store the collaboration request in a CSV
    with open('collaborations.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, collaborator_username, service_name])

    return jsonify({"status": "success", "message": f"Collaboration request sent to {collaborator_username}"})

# Remove User Interest
@app.route('/remove-interest', methods=['POST'])
def remove_interest():
    data = request.json
    username = data.get('username')
    service_name = data.get('service_name')

    if not username or not service_name:
        return jsonify({"status": "error", "message": "Missing username or service name"}), 400

    # Remove the user's interest
    with open('user_interest.csv', 'r') as file:
        rows = list(csv.reader(file))

    with open('user_interest.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            if row[0] != username or row[1] != service_name:
                writer.writerow(row)

    return jsonify({"status": "success", "message": "Removed interest"})
@app.route('/logout', methods=['POST'])
def logout():
    # Clear the session (this will log out the user)
    session.clear()

    # Send a success response
    return jsonify({'message': 'Logout successful'}), 200

if __name__ == '__main__':
    app.run(debug=True)
