def allocate_vitamin_d_subsidy(vitamin_d_level, income_level, age):
    # Determine the Vitamin D category
    if vitamin_d_level < 10:
        deficiency = "Severe Deficiency"
    elif 10 <= vitamin_d_level < 20:
        deficiency = "Moderate Deficiency"
    elif 20 <= vitamin_d_level < 30:
        deficiency = "Mild Deficiency"
    elif 30 <= vitamin_d_level < 50:
        deficiency = "Normal"
    else:
        deficiency = "High"

    allocation = {}

    if deficiency == "Severe Deficiency":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 1.4, "Peanut": 1.4, "Chickpeas": 1.4, "Sunflower oil": 1}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 1.4, "Peanut": 1.4, "Chickpeas": 1.4, "Sunflower oil": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.4, "Peanut": 1.4, "Chickpeas": 1.4, "Sunflower oil": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 1.4, "Chickpeas": 1, "Sunflower oil": 1}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.4, "Chickpeas": 1.4, "Sunflower oil": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.4, "Chickpeas": 1.4, "Sunflower oil": 1.4}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 1, "Sweet potatoes": 1.4}
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 1.4, "Sweet potatoes": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 1.4, "Sweet potatoes": 1.4}

    elif deficiency == "Moderate Deficiency":
        if income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Potato": 1.4, "Chickpeas": 1}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.4, "Chickpeas": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.4, "Chickpeas": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Sunflower oil": 1}
            elif 8 <= age <= 20:
                allocation = {"Sunflower oil": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Sunflower oil": 1.4}
        elif income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Peanut": 1, "Sweet potatoes": 1}
            elif 8 <= age <= 20:
                allocation = {"Peanut": 1.4, "Sweet potatoes": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Peanut": 1.4, "Sweet potatoes": 1.4}

    elif deficiency == "Mild Deficiency":
        if income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Potato": 1}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Sunflower oil": 1}
            elif 8 <= age <= 20:
                allocation = {"Sunflower oil": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Sunflower oil": 1.4}
        elif income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 1}
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 1.4}

    elif deficiency == "High":
        if income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Potato": 1, "Peanut": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.4, "Peanut": 1}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.4, "Peanut": 1.4}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 1}
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 1.4}
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 1.4}
        elif income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 1}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.4}

    # Exclude the allocation for "Normal" category
    if deficiency == "Normal":
        return {}, deficiency

    return allocation, deficiency
