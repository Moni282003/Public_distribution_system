def allocate_potassium_subsidy(potassium_level, income_level, age):
    # Determine potassium level category based on potassium level
    if potassium_level < 3.5:
        potassium_category = "Low"
    elif 3.5 <= potassium_level <= 5.0:
        potassium_category = "Normal"
        # Skip allocation for the Normal category
        return {"potassium_category": potassium_category, "allocation": {}}
    else:  # potassium_level > 5.0
        potassium_category = "High"
    
    # Initialize allocation dictionary
    allocation = {}

    # Allocate subsidies based on potassium category, income level, and age group
    if potassium_category == "Low":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Milk powder": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1, "Milk powder": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Milk powder": 1}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Sweet potatoes": 0.5, "Peanut": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Sweet potatoes": 1, "Peanut": 1}
            elif 21 <= age <= 100:
                allocation = {"Sweet potatoes": 1.5, "Peanut": 1.5}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.25}
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 0.75}

    elif potassium_category == "High":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Sunflower seeds": 0.25}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1, "Sunflower seeds": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Sunflower seeds": 1}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Peanut": 0.25, "Beetroot": 0.1}
            elif 8 <= age <= 20:
                allocation = {"Peanut": 0.5, "Beetroot": 0.25}
            elif 21 <= age <= 100:
                allocation = {"Peanut": 0.75, "Beetroot": 0.5}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 0.1}
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 0.25}
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 0.5}

    return allocation, potassium_category
