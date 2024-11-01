def allocate_protein_subsidy(protein_level, income_level, age):
    # Determine protein level category based on serum protein level
    if protein_level < 6.0:
        protein_category = "Low"
    elif 6.0 <= protein_level <= 8.0:
        protein_category = "Normal"
        # Skip allocation for the Normal category
        return {"protein_category": protein_category, "allocation": {}}
    else:  # protein_level > 8.0
        protein_category = "High"

    # Initialize allocation dictionary
    allocation = {}

    if protein_category == "Low":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.5, "Peanut": 1, "Chickpeas": 1, "Sunflower seeds": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 1, "Peanut": 1.2, "Chickpeas": 1, "Sunflower seeds": 0.8}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.2, "Peanut": 1.5, "Chickpeas": 1.2, "Sunflower seeds": 1}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 1, "Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.2, "Sunflower oil": 0.7}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.3, "Sunflower oil": 0.8}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Potato": 1, "Beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.2, "Beetroot": 0.75}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.3, "Beetroot": 1}

    elif protein_category == "High":
        if income_level == "High":
            if 0 <= age <= 7:
                allocation = {"Milk powder": 0.5, "Peanut": 1, "Chickpeas": 0.5, "Sunflower seeds": 1}
            elif 8 <= age <= 20:
                allocation = {"Milk powder": 0.9, "Peanut": 1.2, "Chickpeas": 0.75, "Sunflower seeds": 1.2}
            elif 21 <= age <= 100:
                allocation = {"Milk powder": 1.2, "Peanut": 1.2, "Chickpeas": 1, "Sunflower seeds": 1.2}
        elif income_level == "Medium":
            if 0 <= age <= 7:
                allocation = {"Potato": 1, "Sunflower oil": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Potato": 1.2, "Sunflower oil": 0.5}
            elif 21 <= age <= 100:
                allocation = {"Potato": 1.3, "Sunflower oil": 0.7}
        elif income_level == "Low":
            if 0 <= age <= 7:
                allocation = {"Beetroot": 0.5}
            elif 8 <= age <= 20:
                allocation = {"Beetroot": 1}
            elif 21 <= age <= 100:
                allocation = {"Beetroot": 1.2}

    return allocation, protein_category
