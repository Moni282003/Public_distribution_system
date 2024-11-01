def allocate_wasting_subsidy(z_score, income_level, age):
    allocation = {}
    category = ""

    # Rules for Severe Wasting
    if z_score < -3:  # Z-score for severe wasting
        category = "Severe Wasting"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.8, "peanut": 0.5}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 1, "peanut": 0.6}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1.1, "peanut": 0.7}  # Reduced quantities
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"chickpeas": 0.5}  # Reduced quantity
            elif 8 <= age <= 20:
                allocation = {"chickpeas": 0.7}  # Reduced quantity
            elif 21 <= age <= 100:
                allocation = {"chickpeas": 0.8}  # Reduced quantity
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.5}  # Reduced quantity
            elif 8 <= age <= 20:
                allocation = {"potato": 0.6}  # Reduced quantity
            elif 21 <= age <= 100:
                allocation = {"potato": 0.8}  # Reduced quantity

    # Rules for Moderate Wasting
    elif -3 <= z_score < -2:  # Z-score for moderate wasting
        category = "Moderate Wasting"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.8, "chickpeas": 0.5, "sunflower_oil": 0.1}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 1, "chickpeas": 0.6, "sunflower_oil": 0.5}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1.1, "chickpeas": 0.7, "sunflower_oil": 0.5}  # Reduced quantities
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 0.8, "peanut": 0.5}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 1, "peanut": 0.6}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 1.1, "peanut": 0.7}  # Reduced quantities
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.5}  # Reduced quantity
            elif 8 <= age <= 20:
                allocation = {"potato": 0.6}  # Reduced quantity
            elif 21 <= age <= 100:
                allocation = {"potato": 0.8}  # Reduced quantity

    # Rules for Overweight
    elif z_score > 2:  # Z-score for overweight
        category = "Overweight"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"soya_bean": 0.8, "milk_powder": 0.5, "sunflower_oil": 0.5}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"soya_bean": 1, "milk_powder": 0.6, "sunflower_oil": 0.5}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"soya_bean": 1.1, "milk_powder": 0.7, "sunflower_oil": 0.5}  # Reduced quantities
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 0.8, "peanut": 0.3}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 1, "peanut": 0.3}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 1.1, "peanut": 0.3}  # Reduced quantities
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.5}  # Reduced quantity
            elif 8 <= age <= 20:
                allocation = {"potato": 0.6}  # Reduced quantity
            elif 21 <= age <= 100:
                allocation = {"potato": 0.8}  # Reduced quantity

    return allocation, category
