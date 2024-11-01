def allocate_sodium_subsidy(sodium_level, income_level, age):
    # Determine sodium level category based on sodium level
    if sodium_level < 135:
        sodium_category = "Low"
    elif 135 <= sodium_level <= 145:
        sodium_category = "Normal"
        # Skip allocation for the Normal category
        return {"sodium_category": sodium_category, "allocation": {}}
    else:  # sodium_level > 145
        sodium_category = "High"

    allocation = {}

    if sodium_category == "Low":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Potato": 1.2, "Sunflower seeds": 1.2}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.3, "Sunflower seeds": 1.3}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.4, "Sunflower seeds": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 1.2}
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 1.3}
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 1.4}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 1.2}
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 1.3}
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 1.4}

    elif sodium_category == "High":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Peanut": 1.2, "Sunflower seeds": 1.2}
            elif 8 <= age <= 20:
                allocation = {"Peanut": 1.3, "Sunflower seeds": 1.3}
            elif 21 <= age <= 100:
                allocation = {"Peanut": 1.4, "Sunflower seeds": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 1.2, "Beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.3, "Beetroot": 1.2}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.4, "Beetroot": 1.2}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 1.2}
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 1.3}

    return allocation, sodium_category
