# UI.py
from Rule import corn_diseases, symptoms

def display_diseases_and_symptoms():
    print("Penyakit Jagung dan Kode Penyakit:")
    for disease, code in corn_diseases.items():
        print(f"{disease}: {code}")

    print("\nGejala terkait dengan penyakit:")
    for code, symptom_list in symptoms.items():
        disease_name = list(corn_diseases.keys())[list(corn_diseases.values()).index(code)]
        print(f"{disease_name} ({code}): {', '.join(symptom_list)}")
