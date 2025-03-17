from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from werkzeug.security import check_password_hash
import logging  # Import the logging module

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

DB_HOST = 'localhost' 
DB_USER = 'postgres'   
DB_PASS = '123456'    

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def get_db_connection(DB_NAME):
    """Establish a database connection."""
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route('/login', methods=['POST'])
def login():
    """Handle user login."""
    data = request.json
    logging.debug(f"Received data: {data}")  # Log the received data

    center_id = data.get('center_id')  # Get center ID from the request
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()
        cursor.execute("SELECT center_id, password, role FROM camp_users WHERE center_id = %s AND username = %s", (center_id, username))
        user = cursor.fetchone()

        if user and user[1] == password and role == user[2]:
            cursor.close()
            connection.close()
            return jsonify({"center_id": user[0], "message": "Login successful"}), 200  
        else:
            cursor.close()
            connection.close()
            return jsonify({"error": "Invalid center ID, username, or password"}), 401
    except Exception as e:
        logging.error(f"Error: {str(e)}")  # Log the error
        return jsonify({"error": str(e)}), 400
@app.route('/admin/login', methods=['POST'])
def admin_login():
    """Handle admin login."""
    data = request.json
    logging.debug(f"Received data for admin login: {data}")  # Log the received data

    username = data.get('username')
    password = data.get('password')

    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()
        
        # Fetch the admin details from the central_admin table
        cursor.execute("SELECT username, password FROM central_admin WHERE username = %s", (username,))
        admin = cursor.fetchone()

        if admin and admin[1] == password:  # Direct password comparison; consider hashing in production
            cursor.close()
            connection.close()
            return jsonify({"username": admin[0], "message": "Admin login successful"}), 200
        else:
            cursor.close()
            connection.close()
            return jsonify({"error": "Invalid username or password"}), 401
    except Exception as e:
        logging.error(f"Error: {str(e)}")  # Log the error
        return jsonify({"error": str(e)}), 400


@app.route('/citizen/login', methods=['POST'])
def citizen_login():
    """Handle citizen login."""
    data = request.json
    logging.debug(f"Received data for citizen login: {data}")

    aadhar = data.get('aadhar')
    password = data.get('password')

    try:
        connection = get_db_connection('login')
        cursor = connection.cursor()
        cursor.execute("SELECT aadhar, password FROM citizen WHERE aadhar = %s", (aadhar,))
        citizen = cursor.fetchone()

        if citizen and citizen[1]== password:  
            cursor.execute("UPDATE citizen SET last_login = CURRENT_TIMESTAMP WHERE aadhar = %s", (citizen[0],))
            connection.commit()

            cursor.close()
            connection.close()
            return jsonify({"aadhar": citizen[0], "message": "Citizen login successful"}), 200
        else:
            cursor.close()
            connection.close()
            return jsonify({"error": "Invalid Aadhar or password"}), 401
    except Exception as e:
        logging.error(f"Error during citizen login: {str(e)}")
        return jsonify({"error": str(e)}), 400

@app.route('/get_ration_ids', methods=['GET'])
def get_ration_ids():
    """Retrieve all ration IDs from the ration_shops table."""
    try:
        connection = get_db_connection('kms')  # Replace with your actual database name
        cursor = connection.cursor()

        # Query to get all ration IDs
        cursor.execute("SELECT shop_id FROM ration_shops")
        ration_ids = cursor.fetchall()

        # Extracting ration_ids from the fetched rows
        ration_ids_list = [row[0] for row in ration_ids]

        cursor.close()
        connection.close()

        return jsonify({'ration_ids': ration_ids_list}), 200
    except Exception as e:
        logging.error(f"Error retrieving ration IDs: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/users', methods=['GET'])
def get_users():
    """Fetch all users from the database."""
    try:
        connection = get_db_connection('login')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        # Convert the user data to a list of dictionaries
        users_list = []
        for user in users:
            users_list.append({
                "id": user[0],
                "center_id": user[1],
                "username": user[2],
                "created_at": user[4].isoformat(),  # Convert datetime to ISO format for JSON serialization
                "last_login": user[5].isoformat(),
                "is_active": user[6],
                "role": user[7]
            })

        cursor.close()
        connection.close()
        return jsonify(users_list), 200
    except Exception as e:
        logging.error(f"Error: {str(e)}")  # Log the error
        return jsonify({"error": str(e)}), 400





@app.route('/get_ration_shop_by_pin/<location_pin>', methods=['GET'])
def get_ration_shop_by_pin(location_pin):
    try:
        conn = get_db_connection('kms')
        cursor = conn.cursor()
        cursor.execute('SELECT shop_id FROM ration_shops WHERE location_pin = %s;', (location_pin,))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        
        if result:
            return jsonify({'ration_shop_id': result[0]}), 200  # Return first match
        else:
            return jsonify({'error': 'No ration shop found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

import random

@app.route('/get_center_by_ration_shop/<ration_shop_id>', methods=['GET'])
def get_center_by_ration_shop(ration_shop_id):
    try:
        conn = get_db_connection('kms')
        cursor = conn.cursor()
        cursor.execute('SELECT center_id FROM diagnostic_centers WHERE ration_id = %s;', (ration_shop_id,))
        centers = cursor.fetchall()
        cursor.close()
        conn.close()

        if centers:
            # Randomly select a center if multiple exist
            center_id = random.choice(centers)[0]
            return jsonify({'center_id': center_id}), 200
        else:
            return jsonify({'error': 'No diagnostic centers found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/add_citizen', methods=['POST'])
def add_citizen():
    data = request.get_json()
    citizen_id = data['citizen_id']
    ration_card_id = data['ration_card_id']
    location_pin = data['location_pin']
    # Derive password from dob
    password = data['dob'].replace('-', '')  # Format: YYYY-MM-DD to DDMMYYYY

    try:
        conn = get_db_connection('kms')
        cursor = conn.cursor()
        
        # Check if citizen with the same ration card ID already exists
        cursor.execute('SELECT ration_shop_id, diagnostic_center_id FROM citizens WHERE ration_card_id = %s;', (ration_card_id,))
        existing_citizen = cursor.fetchone()
  
        if existing_citizen:
            # If the citizen exists, update only the address, income level, and location pin
            ration_shop_id = existing_citizen[0]
            diagnostic_center = existing_citizen[1]
            cursor.execute('UPDATE citizens SET address = %s, income_level = %s, location_pin = %s WHERE ration_card_id = %s;',
                           (data['address'], data['income_level'], location_pin, ration_card_id))
        else:
            # If the citizen does not exist, insert new citizen
            ration_shop_id = data['ration_shop_id']
            diagnostic_center = data['diagnostic_center']
            cursor.execute('INSERT INTO citizens (citizen_id, ration_card_id, ration_shop_id, diagnostic_center_id, name, sex, dob, address, contact_number, income_level, location_pin, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);',
                           (citizen_id, ration_card_id, ration_shop_id, diagnostic_center, data['name'], data['sex'][0], data['dob'], data['address'], data['contact_number'], data['income_level'], location_pin, password))

        # Commit the transaction
        conn.commit()
        
        return jsonify({'message': 'Citizen added or updated successfully', 'ration_shop_id': ration_shop_id, 'diagnostic_center': diagnostic_center}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        conn.close()





@app.route('/add_ration_shop', methods=['POST'])
def add_ration_shop():
    """Add a new ration shop to the database."""
    data = request.json
    shop_id = data.get('shop_id')
    address = data.get('address')
    location_pin = data.get('location_pin')
    contact_number = data.get('contact_number')

    if not all([shop_id, address, location_pin, contact_number]):
        return jsonify({'error': 'All fields are required.'}), 400

    try:
        connection = get_db_connection('kms')  # Replace with your actual database name
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM ration_shops WHERE shop_id = %s", (shop_id,))
        existing_shop = cursor.fetchone()

        if existing_shop:
            cursor.close()
            connection.close()
            return jsonify({'error': 'Shop ID already exists.'}), 409

        cursor.execute('''
            INSERT INTO ration_shops (shop_id, address, location_pin, contact_number, created_at)
            VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP);
        ''', (shop_id, address, location_pin, contact_number))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Ration shop added successfully!'}), 201
    except Exception as e:
        logging.error(f"Error adding ration shop: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/add_center', methods=['POST'])
def add_center():
    """Add a new diagnostic center."""
    try:
        data = request.json
        ration_id = data.get('ration_id')
        location_pin = data.get('location_pin')
        center_name = data.get('center_name')
        address = data.get('address')
        contact_number = data.get('contact_number')
        center_id = data.get('center_id')  # New Center ID field

        connection = get_db_connection('kms')  # Replace with your actual database name
        cursor = connection.cursor()

        # SQL query to insert a new center with the new Center ID
        cursor.execute("""
            INSERT INTO diagnostic_centers (ration_id, location_pin, center_name, address, contact_number, center_id)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (ration_id, location_pin, center_name, address, contact_number, center_id))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'Center added successfully!'}), 201
    except Exception as e:
        logging.error(f"Error adding center: {str(e)}")
        return jsonify({'error': str(e)}), 500
    
@app.route('/get_ration_shops', methods=['GET'])
def get_ration_shops():
    conn = get_db_connection('kms')
    cursor = conn.cursor()
    cursor.execute('SELECT shop_id, address, location_pin, contact_number, created_at FROM ration_shops;')
    shops = cursor.fetchall()
    cursor.close()
    conn.close()

    # Convert to a list of dictionaries
    shops_list = [{'shop_id': shop[0], 'address': shop[1], 'location_pin': shop[2], 'contact_number': shop[3], 'created_at': shop[4]} for shop in shops]
    return jsonify(shops_list)

@app.route('/add_username', methods=['POST'])
def add_user():
    data = request.json
    center_id = data['centerId']
    username = data['username']
    password = data['password']  
    role=data['role']
    conn = get_db_connection('kms')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO camp_users (center_id, username, password,role) VALUES (%s, %s, %s,%s) RETURNING id;',
                   (center_id, username, password,role))
    new_user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'User added successfully', 'user_id': new_user_id})

@app.route('/get_users/<center_id>', methods=['GET'])
def getUserNames(center_id):
    conn = get_db_connection('kms')
    cursor = conn.cursor()
    cursor.execute('SELECT id, username, password, created_at, last_login, role FROM camp_users WHERE center_id = %s;', (center_id,))
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    users_list = [{'id': user[0], 'username': user[1], 'password': user[2], 'created_at': user[3], 'last_login': user[4], 'role': user[5]} for user in users]
    return jsonify(users_list)

# Delete a ration shop
@app.route('/delete_ration_shop/<shop_id>', methods=['DELETE'])
def delete_ration_shop(shop_id):
    conn = get_db_connection('kms')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM camp_users WHERE center_id = %s", (shop_id,))
    cursor.execute("DELETE FROM citizens WHERE ration_shop_id = %s", (shop_id,))
    cursor.execute("DELETE FROM ration_shops WHERE shop_id = %s;", (shop_id,))
    cursor.execute("DELETE FROM diagnostic_centers WHERE ration_id = %s", (shop_id,))
    cursor.execute("SELECT center_id FROM diagnostic_centers WHERE shop_id = %s", (shop_id,))
    center_ids = cursor.fetchall()  

    if center_ids:
        for center_id in center_ids:
            # Delete from camp_users for each center_id
            cursor.execute("DELETE FROM camp_users WHERE center_id = %s", (center_id[0],))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Ration shop and related data deleted successfully'})


@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection('kms')
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM camp_users WHERE id = %s;', (user_id,))
        conn.commit()
        message = f"User with ID {user_id} has been deleted."
    except Exception as e:
        conn.rollback()
        message = f"An error occurred: {str(e)}"
    finally:
        cursor.close()
        conn.close()
    
    return jsonify({"message": message})



@app.route('/get_diagnostic_centers', methods=['GET'])
def get_diagnostic_centers():
    """Retrieve all diagnostic centers."""
    try:
        connection = get_db_connection('kms')  # Replace with your actual database name
        cursor = connection.cursor()

        # Query to get all diagnostic centers
        cursor.execute("SELECT * FROM diagnostic_centers")
        centers = cursor.fetchall()

        # Extracting the data from fetched rows
        centers_list = [
            {
                'center_id': row[0],
                'location_pin': row[1],
                'center_name': row[2],
                'address': row[3],
                'contact_number': row[4],
                'created_at': row[5],
                'ration_id': row[6]
            } for row in centers
        ]

        cursor.close()
        connection.close()

        return jsonify({'centers': centers_list}), 200
    except Exception as e:
        logging.error(f"Error retrieving diagnostic centers: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/add_diagnostic_user', methods=['POST'])
def add_diagnostic_user():
    """Add a new user for a diagnostic center."""
    data = request.json
    center_id = data.get('centerId')
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'diag')

    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()

        # Insert the new user
        cursor.execute("""
            INSERT INTO camp_users (center_id, username, password, role)
            VALUES (%s, %s, %s, %s)
        """, (center_id, username, password, role))

        connection.commit()
        cursor.close()
        connection.close()

        return jsonify({'message': 'User added successfully'}), 201
    except Exception as e:
        logging.error(f"Error adding user: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/delete_diagnostic_center/<center_id>', methods=['DELETE'])
def delete_diagnostic_center(center_id):
    """Delete a diagnostic center."""
    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()

        # Delete the center
        cursor.execute("DELETE FROM diagnostic_centers WHERE center_id = %s", (center_id,))
        cursor.execute("DELETE FROM camp_users WHERE center_id = %s", (center_id,))
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({'message': 'Diagnostic center deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error deleting diagnostic center: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/get_diag/<center_id>', methods=['GET'])
def get_diag(center_id):
    """Retrieve all users for a specific diagnostic center."""
    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()

        # Query to get users for the specific center
        cursor.execute("SELECT * FROM camp_users WHERE center_id = %s", (center_id,))
        users = cursor.fetchall()

        # Extracting the data from fetched rows
        users_list = [
            {
                'id': row[0],
                'center_id': row[1],
                'username': row[2],
                'password': row[3],
                'created_at': row[4],
                'last_login': row[5],
                'role': row[6]
            } for row in users

        ]

        cursor.close()
        connection.close()

        return jsonify({'users': users_list}), 200
    except Exception as e:
        logging.error(f"Error retrieving users: {str(e)}")
        return jsonify({'error': str(e)}), 500


@app.route('/delete_diag/<user_id>', methods=['DELETE'])
def delete_diag(user_id):
    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()

        # Delete the user based on user_id
        cursor.execute("DELETE FROM camp_users WHERE id = %s", (user_id,))  # Ensure the query uses the correct column name
        connection.commit()

        cursor.close()
        connection.close()

        return jsonify({'message': 'User deleted successfully'}), 200
    except Exception as e:
        logging.error(f"Error deleting user: {str(e)}")
        return jsonify({'error': str(e)}), 500






@app.route('/admin/change_password', methods=['PUT'])
def change_password():
    data = request.get_json()
    username = data.get('username')
    current_password = data.get('currentPassword')
    new_password = data.get('newPassword')

    # Validate input
    if not username or not current_password or not new_password:
        return jsonify({'error': 'All fields are required'}), 400

    # Connect to the database
    conn = get_db_connection('kms')
    cursor = conn.cursor()

    # Check if the username and current password match
    cursor.execute('SELECT * FROM central_admin WHERE username = %s AND password = %s;', (username, current_password))
    admin = cursor.fetchone()

    if admin is None:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Invalid username or current password'}), 401

    # Update the password
    cursor.execute('UPDATE central_admin SET password = %s WHERE username = %s;', (new_password, username))
    
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Password changed successfully'})
@app.route('/add_admin', methods=['POST'])
def add_admin():
    data = request.get_json()
    
    username = data.get('username')
    contact_number = data.get('contact_number')
    password = data.get('password')

    # Validate input
    if not username or not contact_number or not password:
        return jsonify({'error': 'All fields are required'}), 400

    try:
        # Connect to the database
        connection = get_db_connection('kms')
        cursor = connection.cursor()

        # Generate new admin_id
        cursor.execute('SELECT COALESCE(MAX(admin_id), 0) + 1 FROM central_admin;')
        new_admin_id = cursor.fetchone()[0]

        # Insert admin into the central_admin table
        cursor.execute(
            'INSERT INTO central_admin (admin_id, username, contact_number, password) VALUES (%s, %s, %s, %s)',
            (new_admin_id, username, contact_number, password)
        )

        # Commit the transaction
        connection.commit()
        
        return jsonify({'message': 'Admin added successfully', 'admin_id': new_admin_id}), 201
    
    except Exception as e:
        # Rollback if there is an error
        connection.rollback()
        return jsonify({'error': str(e)}), 500
    
    finally:
        # Ensure resources are closed
        cursor.close()
        connection.close()


@app.route('/view_citizens', methods=['GET'])
def view_citizens():
    ration_card_id = request.args.get('ration_card_id')
    ration_shop_id = request.args.get('ration_shop_id')
    diagnostic_center_id = request.args.get('diagnostic_center_id')
    location_pin = request.args.get('location_pin')

    # Start building the query
    query = "SELECT * FROM citizens WHERE TRUE"
    params = []

    

    if ration_shop_id:
        query += " AND ration_shop_id = %s"
        params.append(ration_shop_id)

    if diagnostic_center_id:
        query += " AND diagnostic_center_id = %s"
        params.append(diagnostic_center_id)

    if location_pin:
        query += " AND location_pin = %s"
        params.append(location_pin)

    try:
        # Connect to the database
        connection = get_db_connection('kms')
        cursor = connection.cursor()

        # Execute the query with parameters
        cursor.execute(query, params)
        citizens = cursor.fetchall()

        # Get column names for response
        column_names = [desc[0] for desc in cursor.description]
        result = [dict(zip(column_names, citizen)) for citizen in citizens]

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        cursor.close()
        connection.close()

@app.route('/unique_ration_cards', methods=['GET'])
def unique_ration_cards():
    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()
        cursor.execute('SELECT DISTINCT ration_card_id FROM citizens;')
        ration_cards = [row[0] for row in cursor.fetchall()]
        return jsonify(ration_cards), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/unique_ration_shops', methods=['GET'])
def unique_ration_shops():
    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()
        cursor.execute('SELECT DISTINCT ration_shop_id FROM citizens;')
        ration_shops = [row[0] for row in cursor.fetchall()]
        return jsonify(ration_shops), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/unique_diagnostic_centers', methods=['GET'])
def unique_diagnostic_centers():
    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()
        cursor.execute('SELECT DISTINCT diagnostic_center_id FROM citizens;')
        diagnostic_centers = [row[0] for row in cursor.fetchall()]
        return jsonify(diagnostic_centers), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/unique_location_pins', methods=['GET'])
def unique_location_pins():
    try:
        connection = get_db_connection('kms')
        cursor = connection.cursor()
        cursor.execute('SELECT DISTINCT location_pin FROM citizens;')
        location_pins = [row[0] for row in cursor.fetchall()]
        return jsonify(location_pins), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/get_citizens', methods=['GET'])
def get_citizens():
    diagnostic_center_id = request.args.get('diagnostic_center_id')
    print(diagnostic_center_id)

    conn = get_db_connection('kms')
    cursor = conn.cursor()
    cursor.execute('SELECT citizen_id, ration_card_id, name, sex, dob, address, contact_number,ration_shop_id,report_id '
                   'FROM citizens WHERE diagnostic_center_id = %s;', (diagnostic_center_id,))
    citizens = cursor.fetchall()
    

    # Convert to a list of dictionaries
    citizens_list = [
        {
            'citizen_id': citizen[0],
            'ration_card_id': citizen[1],
            'name': citizen[2],
            'sex': citizen[3],
            'dob': citizen[4],
            'address': citizen[5],
            'contact_number': citizen[6],
            'ration_shop_id':citizen[7],
            'report_id': citizen[8]
        } for citizen in citizens
    ]
    return jsonify(citizens_list)

from datetime import datetime, timedelta

@app.route('/validate_citizen', methods=['GET'])
def validate_citizen():
    citizen_id = request.args.get('id')
    
    conn = get_db_connection('kms')
    cursor = conn.cursor()

    # Check if citizen exists in the 'citizens' table
    cursor.execute('SELECT COUNT(*) FROM citizens WHERE citizen_id = %s;', (citizen_id,))
    citizen_exists = cursor.fetchone()[0] > 0

    if not citizen_exists:
        cursor.close()
        conn.close()
        return jsonify({'exists': False, 'message': 'Citizen ID not found in citizens table.'})

    # Check if the citizen is already in 'nutrition_data' with a report date within the last 3 months
    three_months_ago = datetime.now() - timedelta(days=90)
    cursor.execute("""
        SELECT COUNT(*)
        FROM nutrition_data
        WHERE citizen_id = %s;
    """, (citizen_id,))

    nutrition_data_exists = cursor.fetchone()[0] > 0

    if nutrition_data_exists:
        cursor.execute("""
            SELECT COUNT(*)
            FROM nutrition_data
            WHERE citizen_id = %s AND report_date > %s;
        """, (citizen_id, three_months_ago))

        recent_report_exists = cursor.fetchone()[0] > 0

        if recent_report_exists:
            cursor.close()
            conn.close()
            return jsonify({'exists': False, 'message': 'Citizen has a recent report within the last 3 months.'})

    cursor.close()
    conn.close()

    return jsonify({'exists': True, 'message': 'Citizen is valid for nutrition data submission.'})



from datetime import datetime 
from allocation import allocation_final
from Growth import calculate_stunting_wasting,categorize_bmi
@app.route('/submit_nutrition_data', methods=['POST'])
def submit_nutrition_data():
    data = request.get_json()

    # Validate required fields
    if 'report_id' not in data:
        return jsonify({'message': 'Missing required fields: report_id is required.'}), 400

    sex = None
    age = None
    citizen_id = data.get('citizen_id')

    try:
        if citizen_id:
            # Retrieve citizen information
            citizen_query = ''' 
                SELECT sex, dob, income_level, ration_card_id, ration_shop_id FROM citizens WHERE citizen_id = %s;
            '''
            with get_db_connection('kms') as conn:
                cursor = conn.cursor()
                cursor.execute(citizen_query, (citizen_id,))
                result = cursor.fetchone()

                if result:
                    sex, dob, income_level, ration_card_id, ration_shop_id = result
                    app.logger.info('Retrieved sex: %s and dob: %s for citizen_id: %s', sex, dob, citizen_id)

                    # Calculate age from dob
                    if dob:
                        dob_date = dob.date() if isinstance(dob, datetime) else dob
                        age = (datetime.now().date() - dob_date).days // 365
                else:
                    app.logger.warning('Citizen with ID %s not found', citizen_id)
                    return jsonify({'message': f'Citizen with ID {citizen_id} not found.'}), 404  # Added response for not found citizen

        # Calculate nutritional indicators
        height = float(data.get('height', 0))
        weight = float(data.get('weight', 0))
        result = calculate_stunting_wasting(age, sex, height, weight)
        bmi_calc = categorize_bmi(height, weight)

        # Get final allocation
        final_alloc = allocation_final(
            float(data.get('zinc', 0)), float(data.get('iodine', 0)), round(result["stunting"], 2),
            float(data.get('calcium', 0)), float(data.get('potassium', 0)), float(data.get('vitamin_a', 0)),
            float(data.get('vitamin_d', 0)), float(data.get('lipid_profile', 0)), float(data.get('iron_level', 0)),
            float(data.get('sodium', 0)), float(data.get('serum_protein', 0)), float(data.get('blood_glucose', 0)),
            float(data.get('folic_acid', 0)), float(data.get('muac', 0)), bmi_calc[0], round(result["wasting"], 2),
            income_level, age
        )

        # Prepare final allocations
        final_allocations = {}
        for allocation in final_alloc:
            item, quantity = allocation.split(': ')
            final_allocations[item.lower()] = float(quantity.split(' ')[0])

        # Prepare ration items dictionary
        ration_items = {
            'rice_kg': 0, 'wheat_kg': 0, 'cornmeal_kg': 0, 'milk_powder_kg': 0, 'peanut_kg': 0,
            'oats_kg': 0, 'brown_rice_kg': 0, 'quinoa_kg': 0, 'potato_kg': 0, 'sunflower_oil_liters': 0,
            'cashew_kg': 0, 'dry_grapes_kg': 0, 'wheat_bread_kg': 0, 'chickpeas_kg': 0, 'beetroot_kg': 0,
            'pumpkin_seeds_kg': 0, 'sunflower_seeds_kg': 0, 'sweet_potatoes_kg': 0, 'iodized_salt_kg': 0,
            'yam_kg': 0, 'elephant_foot_yam_kg': 0, 'soybean_kg': 0
        }

        # Populate ration items with final allocations
        for item_name, item_qty in final_allocations.items():
            item_key = item_name.replace(" ", "_") + '_kg'
            if item_key in ration_items:
                ration_items[item_key] = item_qty

        # Insert nutrition data
        values = (
            data['report_id'], citizen_id, data.get('center_id'), height,
            weight, round(result["stunting"], 2), round(result["wasting"], 2), bmi_calc[0],
            float(data.get('muac', 0)), float(data.get('iron_level', 0)), float(data.get('vitamin_a', 0)),
            float(data.get('vitamin_d', 0)), float(data.get('zinc', 0)), float(data.get('folic_acid', 0)),
            float(data.get('iodine', 0)), float(data.get('blood_glucose', 0)), float(data.get('lipid_profile', 0)),
            float(data.get('serum_protein', 0)), float(data.get('sodium', 0)), float(data.get('potassium', 0)),
            float(data.get('calcium', 0))
        )

        insert_query = ''' 
            INSERT INTO nutrition_data 
            (report_id, citizen_id, center_id, report_date, height, weight, stunting, wasting, bmi, muac, 
            iron_level, vitamin_a, vitamin_d, zinc, folic_acid, iodine, blood_glucose, lipid_profile, serum_protein,
            sodium, potassium, calcium) 
            VALUES (%s, %s, %s, NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s);
        '''

        with get_db_connection('kms') as conn:
            cursor = conn.cursor()
            cursor.execute(insert_query, values)
            conn.commit()

            # Update citizen's report ID
            if citizen_id:
                cursor.execute(''' 
                    UPDATE citizens
                    SET report_id = %s
                    WHERE citizen_id = %s;
                ''', (data['report_id'], citizen_id))
                conn.commit()

            # Insert ration distribution data
        ration_query = '''
            INSERT INTO ration_distribution_reports 
            (distribution_id, citizen_id, distribution_date, ration_card_id, ration_shop_id, rice_kg, wheat_kg, cornmeal_kg, milk_powder_kg, peanut_kg, oats_kg, 
            brown_rice_kg, quinoa_kg, potato_kg, sunflower_oil_liters, cashew_kg, dry_grapes_kg, wheat_bread_kg, 
            chickpeas_kg, beetroot_kg, pumpkin_seeds_kg, sunflower_seeds_kg, sweet_potatoes_kg, iodized_salt_kg, 
            yam_kg, elephant_foot_yam_kg, soybean_kg, created_at) 
            VALUES (%s, %s, NOW(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 
            %s, %s, %s, %s, %s, NOW());
        '''
        cursor.execute(ration_query, [data['report_id'], citizen_id, ration_card_id, ration_shop_id] + list(ration_items.values()))
        conn.commit()

        # Check if shop_id exists in ration_allocation
        check_allocation_query = '''
            SELECT EXISTS (SELECT 1 FROM ration_allocations WHERE shop_id = %s);
        '''
        cursor.execute(check_allocation_query, (ration_shop_id,))
        exists = cursor.fetchone()[0]

        if exists:
            # Update ration allocation data
            allocation_update_query = '''
                UPDATE ration_allocations 
                SET rice_kg = rice_kg + %s, wheat_kg = wheat_kg + %s, cornmeal_kg = cornmeal_kg + %s,
                    milk_powder_kg = milk_powder_kg + %s, peanut_kg = peanut_kg + %s,
                    oats_kg = oats_kg + %s, brown_rice_kg = brown_rice_kg + %s,
                    quinoa_kg = quinoa_kg + %s, potato_kg = potato_kg + %s,
                    sunflower_oil_liters = sunflower_oil_liters + %s, cashew_kg = cashew_kg + %s,
                    dry_grapes_kg = dry_grapes_kg + %s, wheat_bread_kg = wheat_bread_kg + %s,
                    chickpeas_kg = chickpeas_kg + %s, beetroot_kg = beetroot_kg + %s,
                    pumpkin_seeds_kg = pumpkin_seeds_kg + %s, sunflower_seeds_kg = sunflower_seeds_kg + %s,
                    sweet_potatoes_kg = sweet_potatoes_kg + %s, iodized_salt_kg = iodized_salt_kg + %s,
                    yam_kg = yam_kg + %s, elephant_foot_yam_kg = elephant_foot_yam_kg + %s,
                    soybean_kg = soybean_kg + %s
                WHERE shop_id = %s;
            '''
            cursor.execute(allocation_update_query, list(ration_items.values()) + [ration_shop_id])
            conn.commit()
            return jsonify({'message': 'Nutrition data submitted successfully.'}), 201

        else:
            app.logger.warning('Shop ID %s does not exist in ration_allocations, creating a new entry.', ration_shop_id)
            
            insert_allocation_query = '''
                INSERT INTO ration_allocations 
                (shop_id, rice_kg, wheat_kg, cornmeal_kg, milk_powder_kg, peanut_kg, oats_kg, 
                brown_rice_kg, quinoa_kg, potato_kg, sunflower_oil_liters, cashew_kg, 
                dry_grapes_kg, wheat_bread_kg, chickpeas_kg, beetroot_kg, 
                pumpkin_seeds_kg, sunflower_seeds_kg, sweet_potatoes_kg, iodized_salt_kg, 
                yam_kg, elephant_foot_yam_kg, soybean_kg,allocation_date, created_at) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, Now(), NOW());
            '''
            cursor.execute(insert_allocation_query, [ration_shop_id] + list(ration_items.values()))
            conn.commit()

            return jsonify({'message': 'Nutrition data submitted successfully.'}), 201

    except Exception as e:
        app.logger.error('Error while submitting nutrition data: %s', str(e))
        return jsonify({'message': 'An error occurred while submitting nutrition data.'}), 500

















# Analytical data

@app.route('/three_avg_metrics', methods=['GET'])
def three_avg_metrics():
    conn = get_db_connection('kms')
    cursor = conn.cursor()

    cursor.execute("""
        WITH recent_records AS (
            SELECT 
                citizen_id,
                height,
                weight,
                stunting,
                wasting,
                bmi,
                muac,
                iron_level,
                vitamin_a,
                vitamin_d,
                zinc,
                folic_acid,
                iodine,
                blood_glucose,
                lipid_profile,
                serum_protein,
                sodium,
                potassium,
                calcium,
                ROW_NUMBER() OVER (PARTITION BY citizen_id ORDER BY created_at DESC) AS rn
            FROM nutrition_data
        )
        SELECT 
            citizen_id,
            AVG(CASE WHEN rn = 1 THEN height END) AS avg_height_1,
            AVG(CASE WHEN rn = 2 THEN height END) AS avg_height_2,
            AVG(CASE WHEN rn = 3 THEN height END) AS avg_height_3,
            AVG(CASE WHEN rn = 1 THEN weight END) AS avg_weight_1,
            AVG(CASE WHEN rn = 2 THEN weight END) AS avg_weight_2,
            AVG(CASE WHEN rn = 3 THEN weight END) AS avg_weight_3,
            AVG(CASE WHEN rn = 1 THEN stunting END) AS avg_stunting_1,
            AVG(CASE WHEN rn = 2 THEN stunting END) AS avg_stunting_2,
            AVG(CASE WHEN rn = 3 THEN stunting END) AS avg_stunting_3,
            AVG(CASE WHEN rn = 1 THEN wasting END) AS avg_wasting_1,
            AVG(CASE WHEN rn = 2 THEN wasting END) AS avg_wasting_2,
            AVG(CASE WHEN rn = 3 THEN wasting END) AS avg_wasting_3,
            AVG(CASE WHEN rn = 1 THEN bmi END) AS avg_bmi_1,
            AVG(CASE WHEN rn = 2 THEN bmi END) AS avg_bmi_2,
            AVG(CASE WHEN rn = 3 THEN bmi END) AS avg_bmi_3,
            AVG(CASE WHEN rn = 1 THEN muac END) AS avg_muac_1,
            AVG(CASE WHEN rn = 2 THEN muac END) AS avg_muac_2,
            AVG(CASE WHEN rn = 3 THEN muac END) AS avg_muac_3,
            AVG(CASE WHEN rn = 1 THEN iron_level END) AS avg_iron_level_1,
            AVG(CASE WHEN rn = 2 THEN iron_level END) AS avg_iron_level_2,
            AVG(CASE WHEN rn = 3 THEN iron_level END) AS avg_iron_level_3,
            AVG(CASE WHEN rn = 1 THEN vitamin_a END) AS avg_vitamin_a_1,
            AVG(CASE WHEN rn = 2 THEN vitamin_a END) AS avg_vitamin_a_2,
            AVG(CASE WHEN rn = 3 THEN vitamin_a END) AS avg_vitamin_a_3,
            AVG(CASE WHEN rn = 1 THEN vitamin_d END) AS avg_vitamin_d_1,
            AVG(CASE WHEN rn = 2 THEN vitamin_d END) AS avg_vitamin_d_2,
            AVG(CASE WHEN rn = 3 THEN vitamin_d END) AS avg_vitamin_d_3,
            AVG(CASE WHEN rn = 1 THEN zinc END) AS avg_zinc_1,
            AVG(CASE WHEN rn = 2 THEN zinc END) AS avg_zinc_2,
            AVG(CASE WHEN rn = 3 THEN zinc END) AS avg_zinc_3,
            AVG(CASE WHEN rn = 1 THEN folic_acid END) AS avg_folic_acid_1,
            AVG(CASE WHEN rn = 2 THEN folic_acid END) AS avg_folic_acid_2,
            AVG(CASE WHEN rn = 3 THEN folic_acid END) AS avg_folic_acid_3,
            AVG(CASE WHEN rn = 1 THEN iodine END) AS avg_iodeine_1,
            AVG(CASE WHEN rn = 2 THEN iodine END) AS avg_iodeine_2,
            AVG(CASE WHEN rn = 3 THEN iodine END) AS avg_iodeine_3,
            AVG(CASE WHEN rn = 1 THEN blood_glucose END) AS avg_blood_glucose_1,
            AVG(CASE WHEN rn = 2 THEN blood_glucose END) AS avg_blood_glucose_2,
            AVG(CASE WHEN rn = 3 THEN blood_glucose END) AS avg_blood_glucose_3,
            AVG(CASE WHEN rn = 1 THEN lipid_profile END) AS avg_lipid_profile_1,
            AVG(CASE WHEN rn = 2 THEN lipid_profile END) AS avg_lipid_profile_2,
            AVG(CASE WHEN rn = 3 THEN lipid_profile END) AS avg_lipid_profile_3,
            AVG(CASE WHEN rn = 1 THEN serum_protein END) AS avg_serum_protein_1,
            AVG(CASE WHEN rn = 2 THEN serum_protein END) AS avg_serum_protein_2,
            AVG(CASE WHEN rn = 3 THEN serum_protein END) AS avg_serum_protein_3,
            AVG(CASE WHEN rn = 1 THEN sodium END) AS avg_sodium_1,
            AVG(CASE WHEN rn = 2 THEN sodium END) AS avg_sodium_2,
            AVG(CASE WHEN rn = 3 THEN sodium END) AS avg_sodium_3,
            AVG(CASE WHEN rn = 1 THEN potassium END) AS avg_potassium_1,
            AVG(CASE WHEN rn = 2 THEN potassium END) AS avg_potassium_2,
            AVG(CASE WHEN rn = 3 THEN potassium END) AS avg_potassium_3,
            AVG(CASE WHEN rn = 1 THEN calcium END) AS avg_calcium_1,
            AVG(CASE WHEN rn = 2 THEN calcium END) AS avg_calcium_2,
            AVG(CASE WHEN rn = 3 THEN calcium END) AS avg_calcium_3
        FROM recent_records
        WHERE rn <= 3
        GROUP BY citizen_id;
    """)

    records = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description]

    # Prepare the data in a structured format
    data = []
    for row in records:
        data.append(dict(zip(column_names, row)))

    cursor.close()
    conn.close()
    
    import pprint
    pprint.pprint(data)

    return jsonify(data)  # Return the averages as JSON




@app.route('/unique_citizens/count', methods=['GET'])
def get_unique_citizens_details():
    # Get the diagnostic center ID from the request args
    diagnostic_center_id = request.args.get('diagnostic_center_id')

    try:
        # Connect to the database
        conn = get_db_connection('kms')
        cursor = conn.cursor()

        # SQL query to get the required counts
        query = """
            SELECT 
                (SELECT COUNT(*) FROM citizens WHERE diagnostic_center_id = %s) AS total_citizens,
                (SELECT COUNT(*) FROM nutrition_data WHERE center_id = %s) AS total_nutrition_data,
                (SELECT COUNT(*) FROM nutrition_data WHERE center_id = %s AND report_date < CURRENT_DATE - INTERVAL '3 months') AS recent_nutrition_data;
        """

        cursor.execute(query, (diagnostic_center_id, diagnostic_center_id, diagnostic_center_id))
        result = cursor.fetchone()

        # Structure the response
        response = {
            'citizens_count': result[0] if result[0] is not None else 0,
            'nutrition_data_count': result[1] if result[1] is not None else 0,
            'recent_nutrition_data': result[2] if result[2] is not None else 0,
        }

        return jsonify(response), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "An error occurred while fetching data."}), 500

    finally:
        # Close the database connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()


@app.route('/diag/change_password', methods=['PUT'])
def changediag_password():
    data = request.get_json()
    username = data.get('username')
    current_password = data.get('currentPassword')
    new_password=data.get('newPassword')
    

    # Connect to the database
    conn = get_db_connection('kms')
    cursor = conn.cursor()

    # Check if the username and current password match
    cursor.execute('SELECT * FROM camp_users WHERE username = %s AND password = %s;', (username, current_password))
    admin = cursor.fetchone()

    if admin is None:
        cursor.close()
        conn.close()
        return jsonify({'error': 'Invalid username or current password'}), 401

    # Update the password
    cursor.execute('UPDATE camp_users SET password = %s WHERE username = %s;', (new_password, username))
    
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Password changed successfully'})

from pds import nutritional_data
from datetime import datetime

@app.route('/nutrition_data', methods=['GET'])
def get_nutrition_data():
    citizen_id = request.args.get('citizen_id')
    conn = get_db_connection('kms')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM nutrition_data WHERE citizen_id = %s", (citizen_id,))
    nutrition_reports = cursor.fetchall()

    report_list = []
    for report in nutrition_reports:
        report_list.append({
            'report_id': report[0],
            'citizen_id': report[1],
            'center_id': report[2],
            'report_date': report[3].strftime('%Y-%m-%d'), 
            'height': report[4],
            'weight': report[5],
            'stunting': report[6],
            'wasting': report[7],
            'bmi': report[8],
            'muac': report[9],
            'iron_level': report[10],
            'vitamin_a': report[11],
            'vitamin_d': report[12],
            'zinc': report[13],
            'folic_acid': report[14],
            'iodine': report[15],
            'blood_glucose': report[16],
            'lipid_profile': report[17],
            'serum_protein': report[18],
            'sodium': report[19],
            'potassium': report[20],
            'calcium': report[21],
            'created_at': report[22].strftime('%Y-%m-%d %H:%M:%S')
        })


    cursor.close()
    conn.close()

    return jsonify(report_list)

@app.route('/ViewPDF', methods=['GET'])
def ViewPDF():
    report_id = request.args.get('report_id')
    conn = get_db_connection('kms')
    cursor = conn.cursor()

    # Fetch the nutrition report using the provided report_id
    cursor.execute("SELECT * FROM nutrition_data WHERE report_id = %s", (report_id,))
    nutrition_report = cursor.fetchone()
    
    # If no report is found, return an error message
    if nutrition_report is None:
        return jsonify({'error': 'Nutrition report not found'}), 404

    # Create a dictionary for the nutrition report
    nutrition_data = {
        'report_id': nutrition_report[0],
        'citizen_id': nutrition_report[1],
        'center_id': nutrition_report[2],
        'report_date': nutrition_report[3].strftime('%Y-%m-%d'),
        'height': nutrition_report[4],
        'weight': nutrition_report[5],
        'stunting': nutrition_report[6],
        'wasting': nutrition_report[7],
        'bmi': nutrition_report[8],
        'muac': nutrition_report[9],
        'iron_level': nutrition_report[10],
        'vitamin_a': nutrition_report[11],
        'vitamin_d': nutrition_report[12],
        'zinc': nutrition_report[13],
        'folic_acid': nutrition_report[14],
        'iodine': nutrition_report[15],
        'blood_glucose': nutrition_report[16],
        'lipid_profile': nutrition_report[17],
        'serum_protein': nutrition_report[18],
        'sodium': nutrition_report[19],
        'potassium': nutrition_report[20],
        'calcium': nutrition_report[21],
        'created_at': nutrition_report[22].strftime('%Y-%m-%d %H:%M:%S')
    }
    
    # Fetch citizen info using citizen_id from the nutrition report
    cursor.execute("SELECT * FROM citizens WHERE citizen_id = %s", (nutrition_data['citizen_id'],))
    citizen_info = cursor.fetchone()

    # If no citizen info is found, return an error message
    if citizen_info is None:
        return jsonify({'error': 'Citizen not found'}), 404

    citizen_data = {
        'citizen_id': citizen_info[1],              # citizen_id
        'ration_card_id': citizen_info[2],          # ration_card_id
        'ration_shop_id': citizen_info[3],          # ration_shop_id
        'name': citizen_info[4],                     # name
        'sex': citizen_info[5],                      # sex
        'dob': citizen_info[6].strftime('%Y-%m-%d'), # date of birth
        'address': citizen_info[7],                  # address
        'contact_number': citizen_info[8],           # contact_number
        'income_level': citizen_info[9],             # income_level
        'family_size': citizen_info[10],             # family_size
        'location_pin': citizen_info[11],            # location_pin
        'diagnostic_center_id': citizen_info[12],   # diagnostic_center_id
    }
    import base64
    pdf=nutritional_data(nutrition_data, citizen_data)
    file_path = r'C:\Users\monis\OneDrive\Documents\pds\backend\nutritional_results_with_units.pdf'
    try:
        with open(file_path, 'rb') as file:
            blob_data = file.read()  # Read the file as binary
        
        # Encode the binary data to Base64
        encoded_blob = base64.b64encode(blob_data).decode('utf-8')
        
        return jsonify({
            'blob_data': encoded_blob
        })
    
    except FileNotFoundError:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/nutrition-citizen', methods=['GET'])
def get_visuals_data():
    citizen_id = request.args.get('citizen_id')
    if not citizen_id:
        return jsonify({"error": "Citizen ID is required"}), 400

    conn = get_db_connection('kms')
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM nutrition_data
        WHERE citizen_id = %s
        ORDER BY report_date DESC
        LIMIT 3;
    """, (citizen_id,))
    
    records = cur.fetchall()
    cur.close()
    conn.close()

    # Convert records to a list of dictionaries
    columns = [desc[0] for desc in cur.description]
    results = [dict(zip(columns, record)) for record in records]

    return jsonify(results)



if __name__ == '__main__':
    app.run(debug=True)



