# Inference.py
from Rule import corn_diseases, symptoms, symptoms_name

def detect_disease():
    detected_diseases = set()  # Menggunakan set untuk menghindari duplikasi

    # Tanyakan setiap penyakit
    for disease_name, disease_code in corn_diseases.items():
        symptom_list = symptoms[disease_code]
        disease_detected = True  # Asumsi awal penyakit terdeteksi

        # Tanyakan setiap gejala terkait dengan penyakit
        for symptom in symptom_list:
            symptom_name = symptoms_name[symptom]  # Mengambil nama gejala
            response = input(f"Apakah jagung mengalami {symptom_name}? (ya/tidak): ").strip().lower()
            if response == 'tidak':
                disease_detected = False  # Jika ada gejala yang tidak terdeteksi, set flag ke False
                break  # Hentikan pertanyaan untuk gejala selanjutnya

        # Jika semua gejala terdeteksi (semua "ya"), tambahkan kode penyakit ke dalam set
        if disease_detected:
            detected_diseases.add(disease_code)
            print(f"\nPenyakit yang mungkin terjadi: {disease_name} ({disease_code})")
            break  # Hentikan pertanyaan lebih lanjut setelah penyakit terdeteksi

    # Jika tidak ada penyakit terdeteksi
    if not detected_diseases:
        print("Tidak ada penyakit yang terdeteksi berdasarkan gejala yang diberikan.")
