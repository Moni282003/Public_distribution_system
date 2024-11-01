def allocate_zinc_subsidy(zinc_level, income_level, age):
    # Initialize the allocation dictionary
    allocation = {}
    category = ""

    # Determine the allocation based on zinc levels and category
    if zinc_level < 50:  # Severe Deficiency
        category = "Severe Deficiency"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.5, "peanut": 0.5, "chickpeas": 0.5, "sweet_potatoes": 0.5}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 0.6, "peanut": 0.6, "chickpeas": 0.6, "sweet_potatoes": 0.6}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 0.7, "peanut": 0.7, "chickpeas": 0.7, "sweet_potatoes": 0.7}  # Reduced quantities
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"peanut": 0.4, "chickpeas": 0.5, "sweet_potatoes": 0.5}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"peanut": 0.5, "chickpeas": 0.6, "sweet_potatoes": 0.6}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"peanut": 0.6, "chickpeas": 0.7, "sweet_potatoes": 0.7}  # Reduced quantities
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"peanut": 0.3}  # Reduced quantity
            elif 8 <= age <= 20:
                allocation = {"peanut": 0.4}  # Reduced quantity
            elif 21 <= age <= 100:
                allocation = {"peanut": 0.5}  # Reduced quantity

    elif 50 <= zinc_level <= 70:  # Moderate Deficiency
        category = "Moderate Deficiency"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.5, "chickpeas": 0.5, "potato": 0.5, "peanut": 0.5}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 0.6, "chickpeas": 0.6, "potato": 0.6, "peanut": 0.6}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 0.7, "chickpeas": 0.7, "potato": 0.7, "peanut": 0.7}  # Reduced quantities
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 0.4, "peanut": 0.3}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"potato": 0.5, "peanut": 0.4}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"potato": 0.6, "peanut": 0.5}  # Reduced quantities
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.2}  # Reduced quantity
            elif 8 <= age <= 20:
                allocation = {"potato": 0.3}  # Reduced quantity
            elif 21 <= age <= 100:
                allocation = {"potato": 0.4}  # Reduced quantity

    elif 71 <= zinc_level <= 90:  # Mild Deficiency
        category = "Mild Deficiency"
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"potato": 0.4, "peanut": 0.2}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"potato": 0.5, "peanut": 0.3}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"potato": 0.6, "peanut": 0.4}  # Reduced quantities
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"peanut": 0.2}  # Reduced quantity
            elif 8 <= age <= 20:
                allocation = {"peanut": 0.3}  # Reduced quantity
            elif 21 <= age <= 100:
                allocation = {"peanut": 0.4}  # Reduced quantity
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"soya_bean": 0.2, "potato": 0.2}  # Reduced quantities
            elif 8 <= age <= 20:
                allocation = {"soya_bean": 0.3, "potato": 0.3}  # Reduced quantities
            elif 21 <= age <= 100:
                allocation = {"soya_bean": 0.4, "potato": 0.4}  # Reduced quantities

    return allocation, category
