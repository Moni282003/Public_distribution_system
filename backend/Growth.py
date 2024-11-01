
stunting_data = {
    "M": [
        {"age": 1, "median_height": 75.7, "sd": 3.0},
        {"age": 2, "median_height": 87.1, "sd": 3.5},
        {"age": 3, "median_height": 96.1, "sd": 3.8},
        {"age": 4, "median_height": 103.3, "sd": 4.0},
        {"age": 5, "median_height": 110.0, "sd": 4.5},
        {"age": 6, "median_height": 116.0, "sd": 4.7},
        {"age": 7, "median_height": 121.7, "sd": 4.9},
        {"age": 8, "median_height": 127.2, "sd": 5.0},
        {"age": 9, "median_height": 132.6, "sd": 5.3},
        {"age": 10, "median_height": 138.0, "sd": 5.5},
        {"age": 11, "median_height": 143.3, "sd": 5.7},
        {"age": 12, "median_height": 149.1, "sd": 5.9},
        {"age": 13, "median_height": 156.0, "sd": 6.1},
        {"age": 14, "median_height": 162.7, "sd": 6.2},
        {"age": 15, "median_height": 169.0, "sd": 6.5},
        {"age": 16, "median_height": 172.8, "sd": 6.7},
        {"age": 17, "median_height": 175.2, "sd": 6.9},
        {"age": 18, "median_height": 176.0, "sd": 7.0},
        {"age_range": "19-100", "median_height": 176.5, "sd": 7.1}
    ],
    "F": [
        {"age": 1, "median_height": 74.0, "sd": 2.8},
        {"age": 2, "median_height": 85.5, "sd": 3.3},
        {"age": 3, "median_height": 94.1, "sd": 3.6},
        {"age": 4, "median_height": 101.5, "sd": 4.0},
        {"age": 5, "median_height": 108.4, "sd": 4.3},
        {"age": 6, "median_height": 115.0, "sd": 4.5},
        {"age": 7, "median_height": 121.7, "sd": 4.8},
        {"age": 8, "median_height": 128.2, "sd": 5.0},
        {"age": 9, "median_height": 134.1, "sd": 5.2},
        {"age": 10, "median_height": 139.8, "sd": 5.4},
        {"age": 11, "median_height": 145.2, "sd": 5.6},
        {"age": 12, "median_height": 151.2, "sd": 5.8},
        {"age": 13, "median_height": 157.0, "sd": 6.0},
        {"age": 14, "median_height": 160.4, "sd": 6.2},
        {"age": 15, "median_height": 162.0, "sd": 6.5},
        {"age": 16, "median_height": 162.5, "sd": 6.7},
        {"age": 17, "median_height": 162.7, "sd": 6.9},
        {"age": 18, "median_height": 163.0, "sd": 7.0},
        {"age_range": "19-100", "median_height": 163.5, "sd": 7.1}
    ]
}

wasting_data = {
    "M": [
        {"age": 1, "median_weight": 9.2, "sd": 1.5},
        {"age": 2, "median_weight": 12.5, "sd": 1.7},
        {"age": 3, "median_weight": 14.8, "sd": 1.9},
        {"age": 4, "median_weight": 16.8, "sd": 2.0},
        {"age": 5, "median_weight": 18.5, "sd": 2.3},
        {"age": 6, "median_weight": 20.0, "sd": 2.5},
        {"age": 7, "median_weight": 21.5, "sd": 2.6},
        {"age": 8, "median_weight": 23.0, "sd": 2.8},
        {"age": 9, "median_weight": 25.0, "sd": 3.0},
        {"age": 10, "median_weight": 27.0, "sd": 3.2},
        {"age": 11, "median_weight": 30.0, "sd": 3.5},
        {"age": 12, "median_weight": 35.0, "sd": 3.8},
        {"age": 13, "median_weight": 40.0, "sd": 4.0},
        {"age": 14, "median_weight": 50.0, "sd": 4.5},
        {"age": 15, "median_weight": 60.0, "sd": 5.0},
        {"age_range": "16-100", "median_weight": 70.0, "sd": 5.5}
    ],
    "F": [
        {"age": 1, "median_weight": 8.9, "sd": 1.4},
        {"age": 2, "median_weight": 11.8, "sd": 1.6},
        {"age": 3, "median_weight": 13.5, "sd": 1.8},
        {"age": 4, "median_weight": 15.3, "sd": 1.9},
        {"age": 5, "median_weight": 17.0, "sd": 2.1},
        {"age": 6, "median_weight": 19.0, "sd": 2.3},
        {"age": 7, "median_weight": 20.5, "sd": 2.5},
        {"age": 8, "median_weight": 22.0, "sd": 2.7},
        {"age": 9, "median_weight": 24.0, "sd": 3.0},
        {"age": 10, "median_weight": 26.0, "sd": 3.2},
        {"age": 11, "median_weight": 28.0, "sd": 3.5},
        {"age": 12, "median_weight": 32.0, "sd": 3.8},
        {"age": 13, "median_weight": 36.0, "sd": 4.0},
        {"age": 14, "median_weight": 42.0, "sd": 4.5},
        {"age_range": "15-100", "median_weight": 60.0, "sd": 5.0}
    ]
}








def categorize_bmi(height, weight):
    bmi = weight / (height * height / 10000)  # height in cm
    bmi = round(bmi, 2)  # Round to 2 decimal points
    if bmi < 18.5:
        return bmi, "Underweight"
    elif 18.5 <= bmi < 24.9:
        return bmi, "Normal"
    elif 25 <= bmi < 29.9:
        return bmi, "Overweight"
    else:
        return bmi, "Obesity"
    

    
def calculate_stunting_wasting(age, gender, height=None, weight=None):
    z_score_stunting = None
    z_score_wasting = None

    def find_data_by_age(age, data):
        # Look for an exact age match first
        exact_match = next((item for item in data if item.get("age") == age), None)
        if exact_match:
            return exact_match
        
        # Look for an age range match
        range_match = next((item for item in data if "age_range" in item and
                            int(item["age_range"].split("-")[0]) <= age <= int(item["age_range"].split("-")[1])), None)
        return range_match

    # Select the data based on gender
    if gender == "M":
        height_data = find_data_by_age(age, stunting_data["M"])
        weight_data = find_data_by_age(age, wasting_data["M"])
    else:
        height_data = find_data_by_age(age, stunting_data["F"])
        weight_data = find_data_by_age(age, wasting_data["F"])

    # Calculate the Z-score for stunting (height-for-age)
    if height and height_data:
        z_score_stunting = (height - height_data["median_height"]) / height_data["sd"]
    
    # Calculate the Z-score for wasting (weight-for-height)
    if weight and weight_data:
        z_score_wasting = (weight - weight_data["median_weight"]) / weight_data["sd"]

    return {"stunting": z_score_stunting, "wasting": z_score_wasting}
