def allocate_muac_subsidy(muac, income_level, age):
    allocation = {}
    category = ""

    # Define MUAC categories
    severe_malnutrition = "Severe Malnutrition"
    moderate_malnutrition = "Moderate Malnutrition"
    normal = "Normal"
    overweight = "Overweight"

    if muac < 11.5:  # MUAC for severe malnutrition
        category = severe_malnutrition
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.5, "peanut": 2}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 0.8, "peanut": 2}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1, "peanut": 2.5}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"chickpeas": 0.8}
            elif 8 <= age <= 20:
                allocation = {"chickpeas": 1.2}
            elif 21 <= age <= 100:
                allocation = {"chickpeas": 1.5}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.25}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.5}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.75}

    # Rules for Moderate Malnutrition
    elif 11.5 <= muac < 12.5:  # MUAC for moderate malnutrition
        category = moderate_malnutrition
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.4, "chickpeas": 1.5, "sunflower_oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 0.7, "chickpeas": 2.5, "sunflower_oil": 1}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1, "chickpeas": 3, "sunflower_oil": 1.5}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 1.5}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 2.5}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 3}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.25}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.5}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.75}

    # Rules for Overweight
    elif muac > 23:  # MUAC for overweight
        category = overweight
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"soya_bean": 1.5, "milk_powder": 0.25, "sunflower_oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"soya_bean": 2, "milk_powder": 0.5, "sunflower_oil": 1}
            elif 21 <= age <= 100:
                allocation = {"soya_bean": 2.5, "milk_powder": 0.75, "sunflower_oil": 1.5}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 0.5}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 0.75}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 1}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.1}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.25}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.5}

    return allocation, category
