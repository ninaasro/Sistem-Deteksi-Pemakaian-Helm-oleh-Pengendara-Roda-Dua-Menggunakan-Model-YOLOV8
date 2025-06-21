# Sistem-Deteksi-Pemakaian-Helm-oleh-Pengendara-Roda-Dua-Menggunakan-Model-YOLOV8

Proyek ini bertujuan untuk mendeteksi apakah pengendara roda dua menggunakan helm atau tidak, menggunakan model deteksi objek YOLOv8 dan ditampilkan melalui antarmuka web Flask yang mendukung gambar dan video input.

🚀 Fitur Utama
✅ Deteksi objek real-time (gambar atau video)
✅ Dua label: helmet dan no-helmet
✅ Visualisasi hasil dengan bounding box
✅ Hitung jumlah helm dan tidak pakai helm

🧪 Dataset
Dataset yang digunakan adalah hasil labeling sendiri menggunakan Roboflow, dengan 4 class awal:
1. helmet
2. no-helmet
3. driver
4. bicyclist
Namun, proyek ini difokuskan hanya pada 2 label: helmet dan no-helmet, dengan filter pada tahap training/inferensi.

📈 Akurasi Model
mAP@0.5: ± 90%
Precision: ± 91%
Recall: ± 80%

🖼️ Antarmuka Web
Upload gambar (.jpg/.png) atau video (.mp4/.avi/.mov)
Tampilkan hasil deteksi lengkap dengan jumlah objek terdeteksi
