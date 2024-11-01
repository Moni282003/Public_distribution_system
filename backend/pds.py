import pandas as pd
def categorize_z_score(z_score):
    if z_score is None:
        return None
    elif z_score < -2.0 and z_score > -3.5:
        return "Mild"
    elif z_score > 2.0 and z_score < 3.5:
        return "Mild"
    elif -2.0 <= z_score <= 2.0:
        return "Normal"
    elif z_score >= 3.5:
        return "Severe"
    elif z_score <= -3.5:
        return "Severe"
    

def categorize_muac(muac, gender):
    if gender == "M":
        return "Malnourished" if muac < 12.5 else "Normal"
    elif gender == "F":
        return "Malnourished" if muac < 12.0 else "Normal"
    return None

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Categorization functions for various metrics
def categorize_hemoglobin_level(hemoglobin):
    if hemoglobin < 7:
        return "Severe Anemia"
    elif 7 <= hemoglobin < 10:
        return "Moderate Anemia"
    elif 10 <= hemoglobin < 12:
        return "Mild Anemia"
    elif 12 <= hemoglobin <= 15:
        return "Normal"
    else:
        return "High"

from User_input import personal_details

from User_input import bmi_calc,hemoglobin_level,vitamin_a_level,muac_value,vitamin_d_level,zinc_level,folic_acid_level,iodine_level,glucose_level,serum_protein_level,sodium_level,potassium_level,calcium_level,cholesterol_level,height,weight,wasting_level,zscore,bmi

def categorize_vitamin_a_level(vitamin_a):
    if vitamin_a < 0.2:
        return "Severe Deficiency"
    elif 0.2 <= vitamin_a < 0.7:
        return "Moderate Deficiency"
    elif 0.7 <= vitamin_a < 1.1:
        return "Mild Deficiency"
    elif vitamin_a >= 1.1:
        return "Normal"

def categorize_vitamin_d_level(vitamin_d):
    if vitamin_d < 10:
        return "Severe Deficiency"
    elif 10 <= vitamin_d < 20:
        return "Moderate Deficiency"
    elif 20 <= vitamin_d < 30:
        return "Mild Deficiency"
    elif 30 <= vitamin_d <= 50:
        return "Normal"
    else:
        return "High"

def categorize_zinc_level(zinc):
    if zinc < 50:
        return "Severe Deficiency"
    elif 50 <= zinc < 70:
        return "Moderate Deficiency"
    elif 70 <= zinc < 90:
        return "Mild Deficiency"
    elif 90 <= zinc <= 110:
        return "Normal"
    else:
        return "Elevated"

def categorize_folic_acid_level(folic_acid):
    if folic_acid < 4:
        return "Severe Deficiency"
    elif 4 <= folic_acid < 10:
        return "Moderate Deficiency"
    elif 10 <= folic_acid < 15:
        return "Mild Deficiency"
    elif 15 <= folic_acid <= 20:
        return "Normal"
    else:
        return "Elevated"

def categorize_iodine_level(iodine):
    if iodine < 20:
        return "Severe Deficiency"
    elif 20 <= iodine < 50:
        return "Moderate Deficiency"
    elif 50 <= iodine < 100:
        return "Mild Deficiency"
    elif 100 <= iodine <= 199:
        return "Normal"
    else:
        return "Excess"

def categorize_blood_glucose_level(glucose):
    if glucose < 70:
        return "Hypoglycemia"
    elif 70 <= glucose < 100:
        return "Normal"
    elif 100 <= glucose < 126:
        return "Prediabetes"
    else:
        return "Diabetes"

def categorize_serum_protein_level(protein):
    if protein < 6.0:
        return "Low"
    elif 6.0 <= protein <= 8.0:
        return "Normal"
    else:
        return "High"

def categorize_sodium_level(sodium):
    if sodium < 135:
        return "Low"
    elif 135 <= sodium <= 145:
        return "Normal"
    else:
        return "High"

def categorize_potassium_level(potassium):
    if potassium < 3.5:
        return "Low"
    elif 3.5 <= potassium <= 5.0:
        return "Normal"
    else:
        return "High"

def categorize_calcium_level(calcium):
    if calcium < 8.5:
        return "Low"
    elif 8.5 <= calcium <= 10.2:
        return "Normal"
    else:
        return "High"

def categorize_cholesterol_level(cholesterol):
    if cholesterol < 200:
        return "Low"
    elif 200 <= cholesterol < 240:
        return "Normal"
    else:
        return "High"


def nutritional_data(report, citizen):
    import pandas as pd
    from datetime import datetime
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

    normal_ranges = {
        "STUNTING": ("-2", "2 units"),
        "WASTING": ("-2", "2 units"),
        "BMI": ("18", "25 kg/m²"),
        "MUAC": ("11", "13 cm"),
        "Hemoglobin": ("12", "15 g/dL"),
        "Vitamin A": ("0.7", "1.1 mg/L"),
        "Vitamin D": ("30", "50 ng/mL"),
        "Zinc": ("90", "110 mcg/dL"),
        "Folic Acid": ("15", "20 ng/mL"),
        "Iodine": ("100", "199 mcg/L"),
        "Blood Glucose": ("70", "100 mg/dL"),
        "Serum Protein": ("6.0", "8.0 g/dL"),
        "Sodium": ("135", "145 mEq/L"),
        "Potassium": ("3.5", "5.0 mEq/L"),
        "Calcium": ("8.5", "10.2 mg/dL"),
        "Cholesterol": ("200", "239 mg/dL")
    }

    units = {
        "STUNTING": "units",
        "WASTING": "units",
        "BMI": "kg/m²",
        "MUAC": "cm",
        "Hemoglobin": "g/dL",
        "Vitamin A": "mg/L",
        "Vitamin D": "ng/mL",
        "Zinc": "mcg/dL",
        "Folic Acid": "ng/mL",
        "Iodine": "mcg/L",
        "Blood Glucose": "mg/dL",
        "Serum Protein": "g/dL",
        "Sodium": "mEq/L",
        "Potassium": "mEq/L",
        "Calcium": "mg/dL",
        "Cholesterol": "mg/dL"
    }

    # Categorize metrics
    metric_categories = {
        "Growth Metrics": ["STUNTING", "WASTING", "BMI", "MUAC"],
        "Biochemical Metrics": ["Hemoglobin", "Vitamin A", "Vitamin D", "Zinc", "Folic Acid", "Iodine"],
        "Metabolic Metrics": ["Blood Glucose", "Serum Protein", "Sodium", "Potassium", "Calcium", "Cholesterol"]
    }
    
    gender = citizen['sex']
    dob = citizen['dob']
    
    if isinstance(dob, str):
        dob = datetime.strptime(dob, '%Y-%m-%d')

    # Calculate age
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    personal_details = {
        "First Name": citizen['name'],
        "Sex": citizen['sex'],
        "Age": age,
        "Date of Birth": str(dob).replace(" 00:00:00", ""),
        "Address": citizen['address'] + ", " + str(citizen['location_pin']),
        "Contact Number": citizen['contact_number'],
        "Report Date": report['report_date'],
        "Report ID": report['report_id']
    }

    results = {
        "STUNTING": (report['stunting'], categorize_z_score(report['stunting'])),
        "WASTING": (report['wasting'], categorize_z_score(report['wasting'])),
        "BMI": (report['bmi'], str(categorize_bmi(24))),
        "MUAC": (report['muac'], categorize_muac(report['muac'], gender)),
        "Hemoglobin": (report["iron_level"], categorize_hemoglobin_level(report["iron_level"])),
        "Vitamin A": (report["vitamin_a"], categorize_vitamin_a_level(report["vitamin_a"])),
        "Vitamin D": (report["vitamin_d"], categorize_vitamin_d_level(report["vitamin_d"])),
        "Zinc": (report["zinc"], categorize_zinc_level(report["zinc"])),
        "Folic Acid": (report["folic_acid"], categorize_folic_acid_level(report["folic_acid"])),
        "Iodine": (report["iodine"], categorize_iodine_level(report["iodine"])),
        "Blood Glucose": (report["blood_glucose"], categorize_blood_glucose_level(report["blood_glucose"])),
        "Serum Protein": (report["serum_protein"], categorize_serum_protein_level(report["serum_protein"])),
        "Sodium": (report["sodium"], categorize_sodium_level(report["sodium"])),
        "Potassium": (report["potassium"], categorize_potassium_level(report["potassium"])),
        "Calcium": (report["calcium"], categorize_calcium_level(report["calcium"])),
        "Cholesterol": (report["lipid_profile"], categorize_cholesterol_level(report["lipid_profile"]))
    }

    # Create a DataFrame for the results
    results_df = pd.DataFrame(results).T
    results_df.columns = ["Result", "Result Condition"]

    # Add Normal Range and Units to the DataFrame
    results_df["Reference Range"] = [f"{normal_ranges[nutrient][0]} to {normal_ranges[nutrient][1]}" 
                                      for nutrient in results_df.index]
    results_df["Result"] = [f"{results_df.loc[nutrient, 'Result']} {units[nutrient]}" for nutrient in results_df.index]

    # Reset the index to include it as a column
    results_df.reset_index(inplace=True)
    results_df.rename(columns={"index": "Nutritional Metric"}, inplace=True)

    # Create separate DataFrames based on categories
    category_dfs = {}
    for category, metrics in metric_categories.items():
        category_dfs[category] = results_df[results_df['Nutritional Metric'].isin(metrics)]

    # Save as Excel
    excel_file_path = "nutritional_results_with_units.xlsx"
    with pd.ExcelWriter(excel_file_path) as writer:
        for category, df in category_dfs.items():
            df.to_excel(writer, sheet_name=category, index=False)

    # Create PDF
    pdf_file_path = "nutritional_results_with_units.pdf"
    doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)

    # Build PDF content
    elements = []
    styles = getSampleStyleSheet()

    # Increase font sizes
    styles['Title'].fontSize = 18
    styles['Normal'].fontSize = 12

    header1 = Paragraph("Nutrition Report", styles['Title'])
    header2 = Paragraph("Govt of India", styles['Title'])
    elements.append(header1)
    elements.append(header2)
    elements.append(Spacer(1, 24))  

    for key, value in personal_details.items():
        detail = Paragraph(f"<b>{key}:</b> {value}", styles['Normal'])
        elements.append(detail)

    elements.append(Spacer(1, 12))  

    for category, df in category_dfs.items():
        # Add title for the table
        title = Paragraph(category + " Results", styles['Title'])
        elements.append(title)
        
        data = [df.columns.tolist()] + df.values.tolist()  # Add header to data
        table = Table(data, colWidths=[doc.width / len(df.columns)] * len(df.columns))  # Set fixed column width

        # Add styling to the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.white),
        ])
        table.setStyle(style)

        elements.append(table)
        elements.append(Spacer(1, 12))  

    elements.append(Spacer(1, 24))  
    signature = Paragraph("Center ID: " + str(citizen['diagnostic_center_id']), styles['Normal'])
    elements.append(signature)

    ration_id = Paragraph("Ration ID: " + str(citizen['ration_shop_id']), styles['Normal'])
    elements.append(ration_id)

    # Build the PDF
    doc.build(elements)

    print(f"Results saved to {pdf_file_path}")
