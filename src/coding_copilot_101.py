"""

"""
from presidio_analyzer import EntityRecognizer

# Load the pre-trained HIPAA and PII entity recognizer

recognizer = EntityRecognizer.load("en")

# Define the text to be deidentified
text = "John Doe, 123 Main Street, Redwood City, CA 94063, (650) 555-1234, 123-45-6789"

# Recognize HIPAA and PII entities in the text
results = recognizer.recognize(text)

# Print the recognized entities
for result in results:
    if result.entity_type in ["PERSON_NAME", "ADDRESS", "PHONE_NUMBER", "SOCIAL_SECURITY_NUMBER"]:
        print(f"Entity type: {result.entity_type}, Text: {result.text}")

# Deidentify the recognized entities
deidentified_text = text
for result in results:
    if result.entity_type in ["PERSON_NAME", "ADDRESS", "PHONE_NUMBER", "SOCIAL_SECURITY_NUMBER"]:
        deidentified_text = deidentified_text.replace(result.text, "REDACTED")

# Print the deidentified text
print(f"\nDeidentified text: {deidentified_text}")
