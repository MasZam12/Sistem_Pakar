# Inference.py
from Rule import corn_diseases, symptoms, symptoms_name

def detect_disease():
    detected_diseases = set()

    for disease_name, disease_code in corn_diseases.items():
        symptom_list = symptoms[disease_code]
        disease_detected = True

        for symptom in symptom_list:
            symptom_name = symptoms_name[symptom]
            response = input(f"Apakah jagung mengalami gejala {symptom_name} atau {symptom}? (ya/tidak): ").strip().lower()
            if response == 'tidak':
                disease_detected = False
                break

        if disease_detected:
            detected_diseases.add(disease_code)
            print(f"\nPenyakit yang mungkin terjadi: {disease_name} ({disease_code})")
            break

    if not detected_diseases:
        print("Tidak ada penyakit yang terdeteksi berdasarkan gejala yang diberikan.")
