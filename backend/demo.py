import requests
import random
from faker import Faker

# Initialize Faker to generate random data
fake = Faker()

# URL of your Flask application
url = 'http://127.0.0.1:5000/submit_nutrition_data'  # Adjust the URL and port as necessary

# Function to generate fake nutrition data
def generate_fake_nutrition_data():
    return {
        "report_id": fake.uuid4(),  # Unique report ID
        "citizen_id": fake.random_int(min=1, max=1000),  # Random citizen ID
        "center_id": fake.random_int(min=1, max=100),  # Random center ID
        "report_date": fake.date(),  # Random date
        "height": random.uniform(140.0, 200.0),  # Height in cm
        "weight": random.uniform(30.0, 100.0),  # Weight in kg
        "stunting": random.choice([True, False]),  # Random stunting
        "wasting": random.choice([True, False]),  # Random wasting
        "bmi": random.uniform(15.0, 40.0),  # Random BMI
        "muac": random.uniform(10.0, 40.0),  # MUAC in cm
        "iron_level": random.uniform(5.0, 200.0),  # Iron level
        "vitamin_a": random.uniform(0.0, 100.0),  # Vitamin A
        "vitamin_d": random.uniform(0.0, 100.0),  # Vitamin D
        "zinc": random.uniform(0.0, 100.0),  # Zinc
        "folic_acid": random.uniform(0.0, 100.0),  # Folic Acid
        "iodine": random.uniform(0.0, 200.0),  # Iodine
        "blood_glucose": random.uniform(70.0, 180.0),  # Blood glucose
        "lipid_profile": random.uniform(0.0, 500.0),  # Lipid profile
        "serum_protein": random.uniform(0.0, 10.0),  # Serum protein
        "sodium": random.uniform(0.0, 200.0),  # Sodium
        "potassium": random.uniform(0.0, 200.0),  # Potassium
        "calcium": random.uniform(0.0, 200.0),  # Calcium
    }

# Generate sample nutrition data
nutrition_data = generate_fake_nutrition_data()

# Send POST request
response = requests.post(url, json=nutrition_data)

# Print the response from the server
print('Status Code:', response.status_code)
print('Response:', response.json())
