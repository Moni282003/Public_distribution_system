def allocate_vitamin_a_subsidy(vitamin_a_level, income_level, age):
    allocation = {}
    category = None

    # Define Vitamin A deficiency categories
    severe_deficiency = "Severe Deficiency"
    moderate_deficiency = "Moderate Deficiency"
    mild_deficiency = "Mild Deficiency"
    normal = "Normal"
    elevated = "Elevated"

    # Rules for Severe Vitamin A Deficiency
    if vitamin_a_level < 0.35:  # Severe Vitamin A deficiency
        category = severe_deficiency
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 1.5, "sweet_potatoes": 1.5, "pumpkin_seeds": 1, "cashew": 0.5}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 1.5, "sweet_potatoes": 1.5, "pumpkin_seeds": 1.5, "cashew": 0.5}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1.5, "sweet_potatoes": 1.5, "pumpkin_seeds": 1.5, "cashew": 1}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 1, "peanut": 1}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 1, "peanut": 1.5}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 1.5, "peanut": 1.5}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 1}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.2}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.5}

    # Rules for Moderate Vitamin A Deficiency
    elif 0.35 <= vitamin_a_level < 0.7:  # Moderate Vitamin A deficiency
        category = moderate_deficiency
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 1.5, "chickpeas": 1.5, "sweet_potatoes": 1.5, "peanut": 1}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 1.5, "chickpeas": 1.5, "sweet_potatoes": 1.5, "peanut": 1.2}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1.5, "chickpeas": 1.5, "sweet_potatoes": 1.5, "peanut": 1.5}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 1, "peanut": 0.5}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 1, "peanut": 1}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 1.5, "peanut": 1}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 1}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.2}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.5}

    elif 0.7 <= vitamin_a_level < 1.05:  # Mild Vitamin A deficiency
        category = mild_deficiency
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 1, "peanut": 0.5}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 1, "peanut": 0.5}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 1.5, "peanut": 0.5}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 1, "peanut": 0.5}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 1, "peanut": 0.5}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 1.5, "peanut": 0.5}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.5}
            elif 8 <= age <= 20:
                allocation = {"potato": 1}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.5}

    # Rules for Elevated Vitamin A Levels
    elif vitamin_a_level >= 2.0:  # Elevated Vitamin A levels
        category = elevated
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"potato": 1.5}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.5}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.5}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 1.5}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.5}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.5}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 1}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.2}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.5}

    return allocation, category
