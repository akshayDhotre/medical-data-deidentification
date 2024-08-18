"""
This script is to deidentify data using Microsoft presedio SDK.
"""

# Imports
import json
from faker import Faker
from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine


# Custom fields recognizer (for insurance policy number)
class InsurancePolicyRecognizer(PatternRecognizer):
    def __init__(self):
        # Define a pattern that matches the insurance policy format
        patterns = [
            Pattern(
                name="Insurance Policy Number",
                regex=r"POL-\d{4}-\d{4}-\d{4}",
                score=0.8,
            )
        ]
        super().__init__(supported_entity="INSURANCE_POLICY", patterns=patterns)


# Helper functions
# Function to generate fake data for anonymization
def generate_fake_value(faker_object, entity_type):
    if entity_type == "PERSON":
        return faker_object.name()
    elif entity_type == "US_SSN":
        return faker_object.ssn()
    elif entity_type == "PHONE_NUMBER":
        return faker_object.phone_number()
    elif entity_type == "EMAIL_ADDRESS":
        return faker_object.email()
    elif entity_type == "DATE_TIME":
        return faker_object.date_of_birth(minimum_age=18, maximum_age=90).strftime(
            "%Y-%m-%d"
        )
    elif entity_type == "INSURANCE_POLICY":
        return f"POL-{faker_object.bothify(text='####')}-{faker_object.bothify(text='####')}-{faker_object.bothify(text='####')}"
    elif entity_type == "ADDRESS":
        return faker_object.address()
    else:
        return "<REDACTED>"


# De-identify the PHI and PII fields in each record with fake values
def deidentify_record_with_fakes(faker_object, analyzer, record):
    fields_to_analyze = [
        "First_Name",
        "Last_Name",
        "SSN",
        "DOB",
        "Address",
        "Phone_Number",
        "Email",
        "Insurance_Policy_Number",
        "Clinical_Notes",
    ]

    for field in fields_to_analyze:
        if field in record:
            text = record[field]
            if isinstance(text, str):
                # Analyze the text to find sensitive entities
                results = analyzer.analyze(
                    text=text,
                    entities=[
                        "PERSON",
                        "US_SSN",
                        "PHONE_NUMBER",
                        "EMAIL_ADDRESS",
                        "DATE_TIME",
                        "INSURANCE_POLICY",
                        "LOCATION",
                    ],
                    language="en",
                )

                # Replace detected entities with fake values
                for result in results:
                    fake_value = generate_fake_value(faker_object, result.entity_type)
                    text = text[: result.start] + fake_value + text[result.end :]

                record[field] = text
    return record


if __name__ == "__name__":
    # Initialize the Analyzer and Anonymizer
    analyzer = AnalyzerEngine()
    anonymizer = AnonymizerEngine()
    fake = Faker()

    # Load the JSON file with the generated fake medical records
    with open(
        "fake_medical_records_with_clinical_notes.json", "r", encoding="utf-8"
    ) as f:
        medical_records = json.load(f)

    # Apply de-identification with fake values to all records
    deidentified_records = [
        deidentify_record_with_fakes(fake, analyzer, record)
        for record in medical_records
    ]

    # Save the de-identified records to a new JSON file
    with open(
        "deidentified_medical_records_with_fake_values.json", "w", encoding="utf-8"
    ) as f:
        json.dump(deidentified_records, f, indent=4)

    print(
        "De-identification with fake values complete. Output saved to 'deidentified_medical_records_with_fake_values.json'."
    )
