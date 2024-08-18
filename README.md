
# Medical Records Generation and De-identification

## Overview

This repository contains two Python scripts:

1. **`src/generate_fake_medical_records.py`**: Generates fake medical records with clinical notes containing HIPAA-compliant attributes and PHI/PII.
2. **`src/deidentify_medical_records.py`**: De-identifies the generated medical records using Microsoft Presidio, replacing PHI/PII with realistic-looking fake values.

## Prerequisites

Before running these scripts, make sure you have Python installed along with the required libraries. You can install the necessary dependencies using pip:

```bash
pip install faker presidio-analyzer presidio-anonymizer
```

## Scripts

### 1. `generate_fake_medical_records.py`

This script generates 100 fake medical records, each containing:

- **Patient Information**: Name, SSN, DOB, Address, Phone Number, Email
- **Medical Data**: Recent Diagnosis, Medications, Primary Physician, Insurance Provider, Insurance Policy Number, Date of Visit, Next Appointment
- **Clinical Notes**: Detailed notes on symptoms, diagnosis, treatment plan, and follow-up instructions

The output is saved as `fake_medical_records_with_clinical_notes.json`.

#### Usage

1. Run the script:

    ```bash
    python generate_fake_medical_records.py
    ```

2. This will create a JSON file named `fake_medical_records_with_clinical_notes.json` in the current directory.

### 2. `deidentify_medical_records.py`

This script takes the generated fake medical records as input and de-identifies the sensitive PHI/PII fields using Microsoft Presidio. Instead of standard tags, it replaces the detected sensitive information with realistic-looking fake data.

- **Fields Analyzed and De-identified**:
  - First Name, Last Name
  - SSN
  - Date of Birth
  - Address
  - Phone Number
  - Email Address
  - Insurance Policy Number
  - Clinical Notes

The output is saved as `deidentified_medical_records_with_fake_values.json`.

#### Usage

1. Ensure that the `fake_medical_records_with_clinical_notes.json` file is present in the current directory.
   
2. Run the script:

    ```bash
    python deidentify_medical_records.py
    ```

3. This will create a JSON file named `deidentified_medical_records_with_fake_values.json` in the current directory, where all PHI/PII fields have been replaced with fake values.

## Example

After running both scripts, you will have two JSON files:

- **`fake_medical_records_with_clinical_notes.json`**: Contains the original fake medical records with PHI/PII.
- **`deidentified_medical_records_with_fake_values.json`**: Contains the de-identified records with PHI/PII replaced by fake values.

These files can be used for testing, development, or demonstrating compliance with privacy standards in handling medical records.
