"""
This script is to generate fake healthcare data for testing other applications.
This data si generated using Faker python package
"""

# Imports
import pprint
import json
import random
from faker import Faker
from faker.providers import BaseProvider


# Define a custom provider for generating insurance policy numbers
class InsuranceProvider(BaseProvider):
    """
    Insurance Provider class to generate policy number
    """

    def insurance_policy_number(self):
        """
        Generate standard policy number for US member
        """
        prefix = "POL"
        number1 = self.bothify(text="####")
        number2 = self.bothify(text="####")
        number3 = self.bothify(text="####")
        return f"{prefix}-{number1}-{number2}-{number3}"


# Helper functions
# Function to generate clinical notes
def generate_clinical_notes(diagnosis, medications):
    """
    Generate clinical notes for testing text processing
    """
    symptoms = random.choice(
        [
            "Patient reports feeling shortness of breath and chest pain.",
            "Patient experiences frequent headaches and dizziness.",
            "Patient complains of chronic joint pain and stiffness.",
            "Patient has been feeling anxious and unable to sleep well.",
            "Patient reports frequent coughing and difficulty breathing.",
        ]
    )

    treatment_plan = f"Continue with {medications} as prescribed. Follow up in 4 weeks to reassess the condition."

    follow_up = "Patient is advised to maintain a low-sodium diet and exercise regularly. Blood pressure to be monitored at home."

    return f"Chief Complaint: {symptoms}\nDiagnosis: {diagnosis}\nTreatment Plan: {treatment_plan}\nFollow-Up Instructions: {follow_up}"


# Function to generate a single medical record
def generate_medical_record(faker_object):
    """
    Generate entire medical record cintaing details
    """
    recent_diagnosis = random.choice(
        [
            "Hypertension",
            "Diabetes",
            "Asthma",
            "COPD",
            "Hyperlipidemia",
            "Arthritis",
            "Anxiety",
            "Depression",
            "Obesity",
            "Heart Disease",
        ]
    )

    medications = random.choice(
        [
            "Lisinopril",
            "Metformin",
            "Albuterol",
            "Simvastatin",
            "Amlodipine",
            "Gabapentin",
            "Hydrochlorothiazide",
            "Omeprazole",
            "Atorvastatin",
            "Levothyroxine",
        ]
    )

    record = {
        "Patient_ID": faker_object.uuid4(),
        "First_Name": faker_object.first_name(),
        "Last_Name": faker_object.last_name(),
        "SSN": faker_object.ssn(),
        "DOB": faker_object.date_of_birth(minimum_age=18, maximum_age=90).strftime(
            "%Y-%m-%d"
        ),
        "Address": faker_object.address(),
        "Phone_Number": faker_object.phone_number(),
        "Email": faker_object.email(),
        "Recent_Diagnosis": recent_diagnosis,
        "Medications": medications,
        "Primary_Physician": faker_object.name(),
        "Insurance_Provider": random.choice(
            [
                "Blue Cross Blue Shield",
                "Aetna",
                "Cigna",
                "United Healthcare",
                "Humana",
                "Kaiser Permanente",
            ]
        ),
        "Insurance_Policy_Number": faker_object.insurance_policy_number(),
        "Date_of_Visit": faker_object.date_this_year().strftime("%Y-%m-%d"),
        "Next_Appointment": faker_object.future_date(end_date="+60d").strftime(
            "%Y-%m-%d"
        ),
        "Clinical_Notes": generate_clinical_notes(recent_diagnosis, medications),
    }
    return record


if __name__ == "__main__":
    # Initialize Faker
    fake = Faker()
    fake.add_provider(InsuranceProvider)

    # Generate 100 medical records
    medical_records = [generate_medical_record(fake) for _ in range(100)]

    pprint.pprint(medical_records[0])

    # Save data to json
    with open(
        "fake_medical_records_with_clinical_notes.json", "w", encoding="utf-8"
    ) as f:
        json.dump(medical_records, f, indent=4)
