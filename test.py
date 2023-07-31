import openai
import pandas as pd
from conf import OPENAI_API_KEY

df_specifics = pd.read_csv('patients_detailed_data_specs.csv')

patient_id = input('Patient ID: ')

patient = df_specifics[df_specifics["patient_id"] == patient_id].iloc[0]

column_names = ['patient_id', 'test_id', 'name',  'Age', 'Gender', 'HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2', 'BaseExcess', 'HCO3', 'FiO2', 'PaCO2', 'SaO2', 'AST', 'BUN', 'Alkalinephos', 'Calcium', 'Glucose', 'Bilirubin_total', 'Hgb', 'Platelets', 'SepsisLabel']

column_details = ['Patient ID', 'Test ID', 'Name', 'Age', 'Gender', 'Heart rate', 'Pulse oximetry', 'Temperature', 'Systolic BP', 'Mean arterial pressure', 'Diastolic BP', 'Respiration rate', 'End tidal carbon dioxide', 'Measure of excess bicarbonate', 'Bicarbonate', 'Fraction of inspired oxygen', 'Partial pressure of carbon dioxide from arterial blood', 'Oxygen saturation from arterial blood', 'Aspartate transaminase', 'Blood urea nitrogen', 'Alkaline phosphatase', 'Calcium', 'Serum glucose', 'Total bilirubin', 'Hematocrit', 'Platelets', 'Does the patient have sepsis?']

column_units = ['', '', '', '', '', 'bpm', '%', 'Deg C', 'mm Hg', 'mm Hg', 'mm Hg', 'breaths per minute', 'mm Hg', 'mmol/L', 'mmol/L', '%', 'mm Hg', '%', 'IU/L', 'mg/dL', 'IU/L', 'mg/dL', 'mg/dL', 'mg/dL', 'g/dL', 'count*10^3/µL', '']

prompt = f''

for column in range(len(column_names)):
    if not pd.isna(patient[column_names[column]]):
        prompt += f'{column_details[column]}: {patient[column_names[column]]} {column_units[column]}\n'

        label_column = f'{column_names[column]}_label'

        if label_column in patient.index:
            prompt += f'{column_details[column]} value indicates: {patient[label_column]}\n'

prompt += f"Does the patient have any disease?\n" \
      f"Generate a 5-point medical report with a conclusion based on the above information for doctors. "


def report_generation_openai(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    report = completions.choices[0].text.strip()
    return report

medical_report = report_generation_openai(prompt)
print(medical_report)
