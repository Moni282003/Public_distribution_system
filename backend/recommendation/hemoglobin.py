def allocate_hemoglobin_subsidy(hemoglobin_level, income_level, age):
    # Determine hemoglobin level category based on hemoglobin level
    if hemoglobin_level < 7:
        hemoglobin_category = "Severe Anemia"
    elif 7 <= hemoglobin_level < 10:
        hemoglobin_category = "Moderate Anemia"
    elif 10 <= hemoglobin_level < 12:
        hemoglobin_category = "Mild Anemia"
    elif hemoglobin_level > 15:
        hemoglobin_category = "High"
    else:
        hemoglobin_category = "Normal"

    allocation = {}

    if hemoglobin_category == "Severe Anemia":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.5, "Peanut": 0.8, "Chickpeas": 1}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 1, "Peanut": 0.8, "Chickpeas": 1}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.2, "Peanut": 0.8, "Chickpeas": 1}

        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Sunflower oil": 1}
            elif 21 <= age <= 100:
                allocation = {"Sunflower oil": 1.2}

        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.5, "Sweet potatoes": 0.7}
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 1, "Sweet potatoes": 0.8}
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 1, "Sweet potatoes": 1.1}

    elif hemoglobin_category == "Moderate Anemia":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Potato": 1, "Milk powder": 0.5, "Peanut": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.2, "Milk powder": 0.7, "Peanut": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.2, "Milk powder": 0.7, "Peanut": 0.7}

        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Sunflower oil": 0.5, "Chickpeas": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Sunflower oil": 1, "Chickpeas": 1}
            elif 21 <= age <= 100:
                allocation = {"Sunflower oil": 1.2, "Chickpeas": 1}

        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 1}
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 1.2}

    elif hemoglobin_category == "Mild Anemia":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 1, "Potato": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 1.2, "Potato": 0.7}
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 1.2, "Potato": 0.8}

        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Sunflower oil": 1}
            elif 21 <= age <= 100:
                allocation = {"Sunflower oil": 1.2}

        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Peanut": 0.5, "Sweet potatoes": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Peanut": 0.8, "Sweet potatoes": 0.8}
            elif 21 <= age <= 100:
                allocation = {"Peanut": 1, "Sweet potatoes": 1}

    elif hemoglobin_category == "High":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Potato": 0.5, "Peanut": 0.2}
            elif 8 <= age <= 20:
                allocation = {"Potato": 0.8, "Peanut": 0.3}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1, "Peanut": 0.5}

        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Chickpeas": 0.2}
            elif 8 <= age <= 20:
                allocation = {"Chickpeas": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Chickpeas": 0.8}

        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.2}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1}

    return allocation, hemoglobin_category
