def allocate_ration(bmi, age, income_level):
    allocation = {}
    result_level = ""

    low_income = "Low"
    medium_income = "Medium"
    high_income = "High"

    # Rules for Underweight (BMI < 18.5)
    if bmi < 18.5:
        result_level = "Underweight"
        if income_level == high_income:
            if 0 <= age <= 7:
                allocation = {"milk_powder": 1.0, "cashew": 0.4}
            elif 8 <= age <= 20:
                allocation = {"milk_powder": 1.0, "cashew": 0.3, "peanut": 0.2}
            elif 21 <= age <= 100:
                allocation = {"milk_powder": 0.8, "cashew": 0.3, "peanut": 0.2}
        elif income_level == medium_income:
            if 0 <= age <= 7:
                allocation = {"peanut": 0.2}
            elif 8 <= age <= 20:
                allocation = {"peanut": 0.2, "dry_grapes": 0.1}
            elif 21 <= age <= 100:
                allocation = {"peanut": 0.2}
        elif income_level == low_income:
            if 0 <= age <= 7:
                allocation = {"potato": 0.1}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.2}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.3}

    # Rules for Overweight (BMI 25 - 29.9)
    elif 25 <= bmi <= 29.9:
        result_level = "Overweight"
        if income_level == high_income:
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 0.4, "soybeans": 0.3, "sunflower_oil": 0.2}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 0.5, "soybeans": 0.4, "sunflower_oil": 0.3}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 0.6, "soybeans": 0.5, "sunflower_oil": 0.4}
        elif income_level == medium_income:
            if 0 <= age <= 7:
                allocation = {"sweet_potatoes": 0.3, "sunflower_seeds": 0.1}
            elif 8 <= age <= 20:
                allocation = {"sweet_potatoes": 0.4, "sunflower_seeds": 0.2}
            elif 21 <= age <= 100:
                allocation = {"sweet_potatoes": 0.5, "sunflower_seeds": 0.3}
        elif income_level == low_income:
            if 0 <= age <= 7:
                allocation = {"potato": 0.1}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.15}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.2}

    elif 18.5 <= bmi < 25:
        result_level = "Normal"

    elif bmi >= 30:
        result_level = "Obese"
        if income_level == high_income:
            if 0 <= age <= 7:
                allocation = {"soybeans": 0.3, "sunflower_oil": 0.2}
            elif 8 <= age <= 20:
                allocation = {"soybeans": 0.4, "sunflower_oil": 0.3}
            elif 21 <= age <= 100:
                allocation = {"soybeans": 0.5, "sunflower_oil": 0.4}
        elif income_level == medium_income:
            if 0 <= age <= 7:
                allocation = {"sunflower_seeds": 0.1}
            elif 8 <= age <= 20:
                allocation = {"sunflower_seeds": 0.2}
            elif 21 <= age <= 100:
                allocation = {"sunflower_seeds": 0.3}
        elif income_level == low_income:
            if 0 <= age <= 7:
                allocation = {"potato": 0.1}
            elif 8 <= age <= 20:
                allocation = {"potato": 0.15}
            elif 21 <= age <= 100:
                allocation = {"potato": 0.2}

    return allocation, result_level
