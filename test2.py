# import streamlit as st
# import pandas as pd
# import openai
# from openai.error import RateLimitError
#
# OPENAI_API_KEY = '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'
#
# df_specifics = pd.read_csv('patients_detailed_data_specs.csv')
# column_names = ['patient_id', 'test_id', 'name', 'Age', 'Gender', 'HR', 'O2Sat', 'Temp', 'SBP', 'MAP', 'DBP', 'Resp', 'EtCO2', 'BaseExcess', 'HCO3', 'FiO2', 'PaCO2', 'SaO2', 'AST', 'BUN', 'Alkalinephos', 'Calcium', 'Glucose', 'Bilirubin_total', 'Hgb', 'Platelets', 'SepsisLabel']
# column_details = ['Patient ID', 'Test ID', 'Name', 'Age', 'Gender', 'Heart rate', 'Pulse oximetry', 'Temperature', 'Systolic BP', 'Mean arterial pressure', 'Diastolic BP', 'Respiration rate', 'End tidal carbon dioxide', 'Measure of excess bicarbonate', 'Bicarbonate', 'Fraction of inspired oxygen', 'Partial pressure of carbon dioxide from arterial blood', 'Oxygen saturation from arterial blood', 'Aspartate transaminase', 'Blood urea nitrogen', 'Alkaline phosphatase', 'Calcium', 'Serum glucose', 'Total bilirubin', 'Hematocrit', 'Platelets', 'Does the patient have sepsis?']
# column_units = ['', '', '', '', '', 'bpm', '%', 'Deg C', 'mm Hg', 'mm Hg', 'mm Hg', 'breaths per minute', 'mm Hg', 'mmol/L', 'mmol/L', '%', 'mm Hg', '%', 'IU/L', 'mg/dL', 'IU/L', 'mg/dL', 'mg/dL', 'mg/dL', 'g/dL', 'count*10^3/µL', '']
#
# openai.api_key = OPENAI_API_KEY
#
#
# def generate_medical_report(patient_id, test_id):
#     # patient = df_specifics[df_specifics["patient_id"] == patient_id].iloc[0]
#     patient = df_specifics[(df_specifics["patient_id"] == patient_id) & (df_specifics["test_id"] == test_id)].iloc[0]
#     prompt = ""
#     for column in range(len(column_names)):
#         if not pd.isna(patient[column_names[column]]):
#             prompt += f'{column_details[column]}: {patient[column_names[column]]} {column_units[column]}\n'
#             label_column = f'{column_names[column]}_label'
#             if label_column in patient.index:
#                 prompt += f'{column_details[column]} value indicates: {patient[label_column]}\n'
#     prompt += "Does the patient have any disease?\n" \
#               "Generate a 5-point medical report with a conclusion based on the above information for doctors."
#
#     # try:
#     #     completions = openai.Completion.create(
#     #         engine="text-davinci-003",
#     #         prompt=prompt,
#     #         max_tokens=1024,
#     #         n=1,
#     #         stop=None,
#     #         temperature=0.5,
#     #     )
#     #
#     #     report = completions.choices[0].text.strip()
#     #
#     # except RateLimitError:
#
#     report = f'The patient, {patient["name"]}, is an {patient["Age"]}-year-old {patient["Gender"]} with a heart rate of 97.0 bpm, pulse oximetry of 95.0 %, temperature of 36.11 Deg C, systolic BP of 98.0 mm Hg, and diastolic BP of 43.0 mm Hg. All these values are within the normal range. The respiration rate is 19.0 breaths per minute, end tidal carbon dioxide is 35.0 mm Hg, and the measure of excess bicarbonate is 24.0 mmol/L, which indicates alkalemia. The bicarbonate level is 45.0 mmol/L, indicating a high level. The fraction of inspired oxygen is 0.28%, partial pressure of carbon dioxide from arterial blood is 100.0 mm Hg, indicating hypercapnia, and the oxygen saturation from arterial blood is 88.0%, indicating moderate hypoxia. The patient\'s aspartate transaminase, blood urea nitrogen, alkaline phosphatase, serum glucose, and total bilirubin levels are significantly elevated. The hematocrit is mildly low and the platelets are highly decreased. The patient does not have sepsis. \nBased on the results, it is suggested that the patient should be monitored for any signs of infection and be prescribed medications to reduce elevated levels of aspartate transaminase, blood urea nitrogen, alkaline phosphatase, serum glucose, and total bilirubin. The patient should be given supplements to increase the platelet count and hematocrit levels. Additionally, the patient should be provided with oxygen therapy to improve oxygen saturation and reduce hypercapnia.'
#
#     return report
#
#
# def main():
#     st.title("Medical Report Generator")
#
#     df = pd.read_csv('patients_detailed_data.csv')
#
#     df_specifics = df[column_names]
#
#     st.dataframe(df_specifics)
#
#     patient_ids = df_specifics["patient_id"].unique().tolist()
#     test_ids = []
#     selected_patient_id, selected_test_id = st.columns(2)
#     with selected_patient_id:
#         selected_patient_id = st.selectbox("Select a patient ID", patient_ids)
#
#     if selected_patient_id:
#         test_ids = df_specifics[df_specifics["patient_id"] == selected_patient_id]["test_id"].tolist()
#     with selected_test_id:
#         selected_test_id = st.selectbox("Select a test ID", test_ids)
#
#     if st.button("Generate Report"):
#         medical_report = generate_medical_report(selected_patient_id, selected_test_id)
#         with st.expander("Medical Report", expanded=True):
#             st.write(medical_report)
#
#
# if __name__ == "__main__":
#     main()
