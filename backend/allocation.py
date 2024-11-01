from recommendation.bmi import allocate_ration
from recommendation.calcium import allocate_calcium_subsidy
from recommendation.cholesterol import allocate_cholesterol_subsidy
from recommendation.folic_acid import allocate_folic_acid_subsidy
from recommendation.glucose import allocate_glucose_subsidy
from recommendation.hemoglobin import allocate_hemoglobin_subsidy
from recommendation.muac import allocate_muac_subsidy
from recommendation.potassium import allocate_potassium_subsidy
from recommendation.protein import allocate_protein_subsidy
from recommendation.sodium import allocate_sodium_subsidy
from recommendation.vitamin_a import allocate_vitamin_a_subsidy
from recommendation.vitamin_d import allocate_vitamin_d_subsidy
from recommendation.wasting import allocate_wasting_subsidy
from recommendation.zinc import allocate_zinc_subsidy
from recommendation.iodine import allocate_iodine_subsidy
from recommendation.stunting import allocate_subsidy

# from User_input import zinc_level,income_level, iodine_level,zscore, age,calcium_level,potassium_level,vitamin_a_level,vitamin_d_level,cholesterol_level,hemoglobin_level,sodium_level,serum_protein_level,glucose_level,folic_acid_level,muac_value,bmi,wasting_level

def allocate_nutritional_subsidies(zinc_level, iodine_level,zscore,calcium_level,potassium_level,vitamin_a_level,vitamin_d_level,cholesterol_level,hemoglobin_level,sodium_level,serum_protein_level,glucose_level,folic_acid_level,muac_value,bmi,wasting_level,income_level,age):
    allocations = {
        "zinc": allocate_zinc_subsidy(zinc_level, income_level, age)[0],
        "iodine": allocate_iodine_subsidy(iodine_level, income_level, age)[0],
        "stunting": allocate_subsidy(zscore, income_level, age)[0],
        "calcium": allocate_calcium_subsidy(calcium_level, income_level, age)[0],
        "vitamin_d": allocate_vitamin_d_subsidy(vitamin_d_level, income_level, age)[0],
        "hemoglobin": allocate_hemoglobin_subsidy(hemoglobin_level, income_level, age)[0],
        "cholesterol": allocate_cholesterol_subsidy(cholesterol_level, income_level, age)[0],
        "potassium": allocate_potassium_subsidy(potassium_level, income_level, age)[0],
        "sodium": allocate_sodium_subsidy(sodium_level, income_level, age)[0],
        "protein": allocate_protein_subsidy(serum_protein_level, income_level, age)[0],
        "glucose": allocate_glucose_subsidy(glucose_level, income_level, age)[0],
        "folic_acid": allocate_folic_acid_subsidy(folic_acid_level, income_level, age)[0],
        "vitamin_a": allocate_vitamin_a_subsidy(vitamin_a_level, income_level, age)[0],
        "muac": allocate_muac_subsidy(muac_value, "Low", age)[0],
        "bmi": allocate_ration(bmi, age, income_level)[0],
        "wasting": allocate_wasting_subsidy(wasting_level, income_level, age)[0]
    }
    
    cleaned_allocations = {}
    for metric, allocation in allocations.items():
        for item, quantity in allocation.items():
            normalized_item = item.lower()
            if normalized_item not in cleaned_allocations:
                cleaned_allocations[normalized_item] = quantity
            else:
                cleaned_allocations[normalized_item] = max(cleaned_allocations[normalized_item], quantity)

    return cleaned_allocations

# Function for monthly food subsidy allocation based on income and age
def allocate_food_subsidy(income_level, age):
    allocation = {}
    if income_level == "Low":
        if 0 <= age <= 7:
            allocation = {"quinoa": 2.00, "cornmeal": 4.00, "oats": 3.00, "iodized salt": 0.5}
        elif 8 <= age <= 20:
            allocation = {"quinoa": 3.00, "cornmeal": 5.00, "oats": 4.00, "iodized salt": 0.5}
        elif 21 <= age <= 100:
            allocation = {"quinoa": 4.00, "cornmeal": 6.00, "oats": 5.00, "iodized salt": 0.5}

    elif income_level == "Medium":
        if 0 <= age <= 7:
            allocation = {"brown rice": 3.00, "wheat": 2.00, "oats": 2.00, "iodized salt": 0.5}
        elif 8 <= age <= 20:
            allocation = {"brown rice": 4.00, "wheat": 3.00, "oats": 3.00, "iodized salt": 0.5}
        elif 21 <= age <= 100:
            allocation = {"brown rice": 5.00, "wheat": 5.00, "oats": 4.00, "iodized salt": 0.5}

    elif income_level == "High":
        if 0 <= age <= 7:
            allocation = {"rice": 3.00, "wheat": 2.00, "oats": 1.00, "iodized salt": 0.5}
        elif 8 <= age <= 20:
            allocation = {"rice": 4.00, "wheat": 3.00, "oats": 2.00, "iodized salt": 0.5}
        elif 21 <= age <= 100:
            allocation = {"rice": 5.00, "wheat": 5.00, "oats": 3.00, "iodized salt": 0.5}
            
    return allocation

# Combine both allocations into a single dictionary ensuring unique items
def combine_allocations(allocations, food_subsidy):
    combined = {}
    # Include all items from food subsidy first
    for item, quantity in food_subsidy.items():
        normalized_item = item.lower()
        combined[normalized_item] = quantity

    # Add items from allocations ensuring not to exceed 7 total items
    for item, quantity in allocations.items():
        if item not in combined and len(combined) < 7:
            combined[item] = quantity

    return combined

high_priority_items = {
    'Low': ['potato', 'sunflower oil', 'chickpeas', 'peanut'],
    'Medium': ['wheat bread', 'sweet potatoes', 'soybean', 'milk powder'],
    'High': ['cashew', 'dry grapes', 'pumpkin seed', 'sunflower seed']
}

# Calculate credits based on income level
def calculate_credits(income_level):
    base_credits = {
        'Low': 100,
        'Medium': 75,
        'High': 50,
    }
    return base_credits.get(income_level, 50)

# Allocation logic based on income level and credits
def allocate_items_based_on_income(credits, allocation_dict, food_subsidy, income_level):
    final_allocation = {}

    # Prioritize allocating basic items first
    basic_items = food_subsidy.keys()
    for item in basic_items:
        if item in food_subsidy and len(final_allocation) < 7:
            final_allocation[item] = food_subsidy[item]

    remaining_slots = 7 - len(final_allocation)

    # Add high-priority items based on income level, without duplicates
    prioritized_items = high_priority_items[income_level]

    for item in prioritized_items:
        if item in allocation_dict and len(final_allocation) < 7:
            final_allocation[item] = allocation_dict[item]

    for item, quantity in allocation_dict.items():
        if item not in final_allocation and len(final_allocation) < 7:
            final_allocation[item] = quantity

    return final_allocation
def allocation_final(zinc_level, iodine_level,zscore, calcium_level,potassium_level,vitamin_a_level,vitamin_d_level,cholesterol_level,hemoglobin_level,sodium_level,serum_protein_level,glucose_level,folic_acid_level,muac_value,bmi,wasting_level,income_level,age):
    allocations = allocate_nutritional_subsidies(zinc_level, iodine_level,zscore, calcium_level,potassium_level,vitamin_a_level,vitamin_d_level,cholesterol_level,hemoglobin_level,sodium_level,serum_protein_level,glucose_level,folic_acid_level,muac_value,bmi,wasting_level,income_level,age)
    food_subsidy = allocate_food_subsidy(income_level, age)

    # Calculate credits based on income level
    credits = calculate_credits(income_level)

    # Allocate final items
    final_items = allocate_items_based_on_income(credits, allocations, food_subsidy, income_level)
    final_allocations = combine_allocations(final_items, food_subsidy)

    # Print final item allocations
    print("Final Item Allocations:")
    for item, quantity in final_allocations.items():
        print(f"{item}: {quantity} kg")
    formatted_allocations_array = [f"{item}: {quantity} kg" for item, quantity in final_allocations.items()]
    rates = {
        "rice": {"low": 0, "medium": 0, "high": 0},
        "wheat": {"low": 0, "medium": 0, "high": 0},
        "cornmeal": {"low": 0, "medium": 0, "high": 0},
        "milk powder": {"low": 30.00, "medium": 40.00, "high": 70.00},
        "peanut": {"low": 8.00, "medium": 12.00, "high": 20.00},
        "oats": {"low":0, "medium": 0, "high": 0},
        "brown rice": {"low": 0, "medium": 0, "high": 0},
        "quinoa": {"low": 0, "medium": 0, "high": 0},
        "potato": {"low": 0.80, "medium": 1.20, "high": 2.00},
        "sunflower oil": {"low": 15.00, "medium": 25.00, "high": 40.00},
        "cashew": {"low": 40.00, "medium": 60.00, "high": 100.00},
        "dry grapes": {"low": 35.00, "medium": 50.00, "high": 70.00},
        "wheat bread": {"low": 8.00, "medium": 12.00, "high": 20.00},
        "chickpeas": {"low": 10.00, "medium": 15.00, "high": 25.00},
        "beetroot": {"low": 4.00, "medium": 6.00, "high": 10.00},
        "pumpkin seeds": {"low": 30.00, "medium": 40.00, "high": 50.00},
        "sunflower seeds": {"low": 20.00, "medium": 30.00, "high": 50.00},
        "sweet potatoes": {"low": 8.00, "medium": 12.00, "high": 20.00},
        "iodized salt": {"low": 0, "medium": 0, "high": 0},
        "yam": {"low": 10.00, "medium": 15.00, "high": 25.00},
        "elephant foot yam": {"low": 15.00, "medium": 25.00, "high": 40.00},
        "soybean": {"low": 25.00, "medium": 35.00, "high": 50.00}
    }


    def calculate_total_cost(allocations, income_level):
        total_cost = 0.00
        for item, quantity in allocations.items():
            item_lower = item.lower()
            if item_lower in rates:
                total_cost += rates[item_lower][income_level.lower()] * quantity
        return total_cost


    total_cost = calculate_total_cost(final_allocations,income_level)
    print(total_cost)
    return formatted_allocations_array


