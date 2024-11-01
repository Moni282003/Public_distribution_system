from Growth import calculate_stunting_wasting, categorize_bmi


personal_details = {
    "First Name": "Jayasree",
    "Last Name": "KS",
    "Sex": "Female",
    "Age": 20,
    "Date of Birth": "13th May 2004",
    "Address": "No:2 karumari amman kovil 2nd street kapsa A, Ambur-635802",
    "Contact Number": "9487504821",
    "Emergency Contact": "9342314749",
    "Report Date": "14th September 2024",
    "Medical Record Number": "270-XYZ-123"
}


age = personal_details["Age"]
height = 169 
weight = 59  


result=calculate_stunting_wasting(age,"girl",height,weight)
bmi_calc =categorize_bmi(height,weight)

vitamin_a_level = 4
zinc_level = 72
iodine_level = 45  
income_level = "Low"
calcium_level = 7.8  
vitamin_d_level = 100 
hemoglobin_level = 8.5
cholesterol_level = 210  
potassium_level = 3.2  
sodium_level = 110  
serum_protein_level = 5.5  
glucose_level = 85      
folic_acid_level = 9  
muac_value = 12  
bmi = bmi_calc[0]
wasting_level = round(result["wasting"], 3)  
zscore = round(result["stunting"], 3)


