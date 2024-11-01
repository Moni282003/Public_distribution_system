def allocate_subsidy(z_score, income_level, age):
    allocation = {}
    category = ""

    if z_score < -3:  # Z-score for severe stunting
        category = "Severe Stunting"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 1.4, "cashew": 1.4}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 1.4, "cashew": 1.4, "peanut": 1.4}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1.4, "cashew": 1.4, "peanut": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 1.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.4, "dry_grapes": 1.4}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.4}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 1.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.4}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.4}

    elif -3 <= z_score < -2:  # Z-score for moderate stunting
        category = "Moderate Stunting"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"chickpeas": 1.4, "sunflower_seeds": 1.4}
            elif 8 <= age <= 20:
                allocation = {"chickpeas": 1.4, "sunflower_seeds": 1.4, "pumpkin_seeds": 1.4}
            elif 21 <= age <= 100:
                allocation = {"chickpeas": 1.4, "sunflower_seeds": 1.4, "pumpkin_seeds": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 1.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.4}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.4}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 1.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.4}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.4}

    elif -2 <= z_score < 1: 
        category = "Normal Stunting"
        # No allocation for normal category

    elif z_score >= 1:  # Z-score for tall
        category = "Tall"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"chickpeas": 1.4, "sunflower_seeds": 1.4}
            elif 8 <= age <= 20:
                allocation = {"chickpeas": 1.4, "sunflower_seeds": 1.4}
            elif 21 <= age <= 100:
                allocation = {"chickpeas": 1.4, "sunflower_seeds": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 1.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.4}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.4}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 1.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.4}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.4}

    return allocation, category
