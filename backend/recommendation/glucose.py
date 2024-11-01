def allocate_glucose_subsidy(glucose_level, income_level, age):
    # Determine deficiency level based on blood glucose level
    if glucose_level < 70:
        deficiency_level = "Hypoglycemia"
    elif 70 <= glucose_level <= 99:
        deficiency_level = "Normal"
    elif 100 <= glucose_level <= 125:
        deficiency_level = "Prediabetes"
    else:  # glucose_level >= 126
        deficiency_level = "Diabetes"
    
    # Initialize allocation dictionary
    allocation = {}

    # Allocate subsidies based on deficiency level, income level, and age
    if deficiency_level == "Hypoglycemia":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.5, "Peanut": 1, "Chickpeas": 0.5, "Sunflower seeds": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 0.8, "Peanut": 1.5, "Chickpeas": 1, "Sunflower seeds": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.2, "Peanut": 2, "Chickpeas": 1.5, "Sunflower seeds": 1}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1, "Sunflower oil": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Sunflower oil": 1}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 0.5, "Beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Beetroot": 0.5}

    elif deficiency_level == "Prediabetes":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.5, "Chickpeas": 0.5, "Beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 0.9, "Chickpeas": 1, "Beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1, "Chickpeas": 1, "Beetroot": 1}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1, "Sunflower oil": 1}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Sunflower oil": 1}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 0.5, "Sunflower oil": 1}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Sunflower oil": 1}

    elif deficiency_level == "Diabetes":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.5, "Peanut": 1, "Chickpeas": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 1, "Peanut": 1, "Chickpeas": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1, "Peanut": 1, "Chickpeas": 1}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1, "Sunflower oil": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Sunflower oil": 1}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 0.5, "Beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Beetroot": 0.5}

    # Return the deficiency level and allocation
    return allocation, deficiency_level
