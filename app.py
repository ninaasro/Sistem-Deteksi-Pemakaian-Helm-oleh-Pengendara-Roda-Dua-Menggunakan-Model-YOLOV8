from flask import Flask, render_template, request
from ultralytics import YOLO
import cv2
import os
from werkzeug.utils import secure_filename
from collections import Counter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/outputs'
model = YOLO('weights/best.pt')  # Path model hasil training kamu

# Proses Gambar
def process_image(path):
    results = model(path)[0]
    annotated = results.plot()

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
    cv2.imwrite(output_path, annotated)

    label_counts = Counter()
    for r in results.boxes.cls:
        label = model.names[int(r)]
        label_counts[label] += 1

    return output_path, label_counts

# Proses Video
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(3))
    height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps == 0 or fps is None:
        fps = 25  # fallback fps aman

    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result_video.mp4')

    # Hapus file lama jika ada
    if os.path.exists(output_path):
        os.remove(output_path)

    # Gunakan codec avc1 (H.264)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    label_counts = Counter()
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model.predict(frame)[0]
        annotated = results.plot()
        out.write(annotated)
        frame_count += 1

        for r in results.boxes.cls:
            label = model.names[int(r)]
            label_counts[label] += 1

    cap.release()
    out.release()

    print(f"✅ Total frame yang ditulis: {frame_count}")
    return output_path, label_counts

# Routing utama
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            ext = os.path.splitext(filename)[1].lower()
            if ext in ['.jpg', '.jpeg', '.png']:
                result_path, label_counts = process_image(input_path)
                is_video = False
            elif ext in ['.mp4', '.avi', '.mov']:
                result_path, label_counts = process_video(input_path)
                is_video = True
            else:
                return "❌ Format file tidak didukung", 400

            return render_template('index.html',
                result_path=os.path.basename(result_path),
                count_helmet=label_counts.get('helmet', 0),
                count_no_helmet=label_counts.get('no-helmet', 0),
                is_video=is_video
            )
    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for
# from ultralytics import YOLO
# import cv2
# import os
# from werkzeug.utils import secure_filename
# from collections import Counter

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/outputs'
# model = YOLO('weights/best.pt')  # Sesuaikan dengan path model kamu

# def process_image(path):
#     results = model(path)[0]
#     annotated = results.plot()

#     # Simpan hasil anotasi
#     output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'result.jpg')
#     cv2.imwrite(output_path, annotated)

#     # Ambil label
#     names = model.names
#     label_counts = Counter()
#     for r in results.boxes.cls:
#         label = names[int(r)]
#         label_counts[label] += 1

#     return output_path, label_counts

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         file = request.files['image']
#         if file:
#             filename = secure_filename(file.filename)
#             input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#             file.save(input_path)

#             result_img_path, label_counts = process_image(input_path)

#             return render_template('index.html',
#                                    result_img=result_img_path,
#                                    count_helmet=label_counts.get('helmet', 0),
#                                    count_no_helmet=label_counts.get('no-helmet', 0))
#     return render_template('index.html')

# if __name__ == '__main__':
#     os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#     app.run(debug=True)
