import pandas as pd

# Update with your actual path
file_path = r"C:\Users\kyleh\Desktop\CGM_Project\CGM Analytics.xlsx"
sheet_name = "CGM"

# Load the CGM sheet
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Calculate patient responsibility
df['Calculated Patient Responsibility'] = df['Invoice Detail Allow'] - df['Invoice Detail Payments']

# Select key columns
df_output = df[[
    'Patient First Name',
    'Patient Last Name',
    'Invoice Detail Allow',
    'Invoice Detail Payments',
    'Calculated Patient Responsibility'
]]

# Save result
output_file = r"C:\Users\kyleh\Desktop\CGM_Project\CGM_Patient_Responsibility_Output.xlsx"
df_output.to_excel(output_file, index=False)

print("Calculation complete. Output saved at:")
print(output_file)
