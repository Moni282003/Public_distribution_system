def allocate_iodine_subsidy(iodine_level, income_level, age):
    # Define allocation based on iodine level, income level, and age
    allocation = {}

    # Determine deficiency level
    if iodine_level < 20:
        deficiency_level = "Severe Deficiency"
    elif 20 <= iodine_level <= 49:
        deficiency_level = "Moderate Deficiency"
    elif 50 <= iodine_level <= 99:
        deficiency_level = "Mild Deficiency"
    elif 100 <= iodine_level <= 199:
        deficiency_level = "Normal"
    else:
        deficiency_level = "Excess"

    # Allocate based on deficiency level
    if deficiency_level == "Severe Deficiency":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 1, "peanut": 1.0, "beetroot": 1.5}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 1.0, "peanut": 1.0, "beetroot": 1.5}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1.0, "peanut": 1.5, "beetroot": 1.5}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 1.0}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.0}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.0}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.5, "beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.5, "beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.5, "beetroot": 0.5}

    elif deficiency_level == "Moderate Deficiency":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"milk_powder": 0.5, "chickpeas": 1.5, "beetroot": 1.0}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 0.7, "chickpeas": 2.0, "beetroot": 1.0}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 1.0, "chickpeas": 1.0, "beetroot": 1.0}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"potato": 1.0}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.0}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.0}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"potato": 0.25, "beetroot": 0.25}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.5, "beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.75, "beetroot": 0.75}

    elif deficiency_level == "Mild Deficiency":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"potato": 0.75}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.0}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.0}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.25, "potato": 0.5}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 0.25, "potato": 0.75}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 0.25, "potato": 0.75}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.25}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 0.5}

    elif deficiency_level == "Excess":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"potato": 1.0}
            elif 8 <= age <= 20:
                allocation = {"potato": 1.0}
            elif 21 <= age <= 100:
                allocation = {"potato": 1.0}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 0.75}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"beetroot": 0.25}
            elif 8 <= age <= 20:
                allocation = {"beetroot": 0.5}
            elif 21 <= age <= 100:
                allocation = {"beetroot": 0.5}

    return allocation, deficiency_level
