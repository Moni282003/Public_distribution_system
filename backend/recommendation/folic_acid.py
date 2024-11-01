def allocate_folic_acid_subsidy(folic_acid_level, income_level, age):
    allocation = {}

    if folic_acid_level < 4:
        deficiency_level = "Severe Deficiency"
    elif 4 <= folic_acid_level <= 10:
        deficiency_level = "Moderate Deficiency"
    elif 11 <= folic_acid_level <= 15:
        deficiency_level = "Mild Deficiency"
    elif 16 <= folic_acid_level <= 20:
        deficiency_level = "Normal"
    else:
        deficiency_level = "Elevated"

    if deficiency_level == "Severe Deficiency":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.4, "peanut": 0.8, "chickpeas": 1.0, "beetroot": 1.0}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 0.5, "peanut": 1.0, "chickpeas": 1.2, "beetroot": 1.2}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 0.6, "peanut": 1.0, "chickpeas": 1.0, "beetroot": 1.2}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.8}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 1.0}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 1.2}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.4}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 0.6}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 0.8}
    elif deficiency_level == "Moderate Deficiency":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.4, "chickpeas": 1.0, "potato": 1.0, "beetroot": 0.8}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 0.5, "chickpeas": 1.0, "potato": 1.0, "beetroot": 1.0}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 0.6, "chickpeas": 1.0, "potato": 1.0, "beetroot": 1.0}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 1.0, "beetroot": 0.8}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.0, "beetroot": 1.0}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.2, "beetroot": 1.0}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.5, "beetroot": 0.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.6, "beetroot": 0.6}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.8, "beetroot": 0.8}
    elif deficiency_level == "Mild Deficiency":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"potato": 0.8, "beetroot": 0.4}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.0, "beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.0, "beetroot": 0.6}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.4}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 0.5}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"soya_bean": 0.8, "potato": 0.4, "beetroot": 0.4}
            elif 8 <= age <= 20:
                allocation = {"soya_bean": 1.0, "potato": 0.4, "beetroot": 0.4}
            elif 21 <= age <= 100:
                allocation = {"soya_bean": 1.0, "potato": 0.6, "beetroot": 0.4}
    elif deficiency_level == "Elevated":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.8}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 1.0}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 1.2}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.4}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 0.6}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 0.8}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"soya_bean": 0.8, "beetroot": 0.4}
            elif 8 <= age <= 20:
                allocation = {"soya_bean": 1.0, "beetroot": 0.8}
            elif 21 <= age <= 100:
                allocation = {"soya_bean": 1.0, "beetroot": 0.8}

    return allocation, deficiency_level
