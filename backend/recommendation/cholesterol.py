def allocate_cholesterol_subsidy(cholesterol_level, income_level, age):
    if cholesterol_level < 200:
        cholesterol_category = "Low"
    elif cholesterol_level >= 240:
        cholesterol_category = "High"
    else:
        cholesterol_category = "Normal"
    
    allocation = {}

    if cholesterol_category == "Low":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.8, "Peanut": 0.4}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 1.0, "Peanut": 0.5}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.0, "Peanut": 0.6}  # Monthly allocation
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 0.8, "Sunflower oil": 0.4}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 1.0, "Sunflower oil": 0.5}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 1.0, "Sunflower oil": 0.6}  # Monthly allocation
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.4, "Sweet potatoes": 0.8}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 0.6, "Sweet potatoes": 0.8}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 0.8, "Sweet potatoes": 1.0}  # Monthly allocation

    elif cholesterol_category == "High":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.8}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.0}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.0}  # Monthly allocation
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.4}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 0.6}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 0.8}  # Monthly allocation
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 0.4}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 0.6}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 0.8}  # Monthly allocation

    return allocation, cholesterol_category
