def allocate_calcium_subsidy(calcium_level, income_level, age):
    # Determine calcium level category based on calcium level
    if calcium_level < 8.5:
        calcium_category = "Low"
    elif calcium_level > 10.2:
        calcium_category = "High"
    else:
        calcium_category = "Normal"
    
    allocation = {}

    if calcium_category == "Low":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.8, "Chickpeas": 0.8}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 1.0, "Chickpeas": 0.5}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.0, "Chickpeas": 1.0}  # Monthly allocation
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.8, "Sunflower oil": 0.4}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.0, "Sunflower oil": 0.5}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.0, "Sunflower oil": 0.6}  # Monthly allocation
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.8}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 0.8}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 0.8}  # Monthly allocation

    elif calcium_category == "High":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.8}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Potato": 0.8}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Potato": 0.8}  # Monthly allocation
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.8}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 0.8}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 0.8}  # Monthly allocation
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.4}  # Monthly allocation
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 0.4}  # Monthly allocation
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 0.8}  # Monthly allocation

    return allocation, calcium_category
