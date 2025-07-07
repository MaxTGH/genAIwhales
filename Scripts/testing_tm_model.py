from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os
import zipfile
import re
import shutil


zip_path = "c:/Users/mn316/Downloads/converted_keras.zip"
extract_to = "c:/Users/mn316/Downloads/converted_keras"

if zipfile.is_zipfile(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")
else:
    print(f"{zip_path} is not a valid ZIP file.")

# --- Settings ---
model_path = "c:/Users/mn316/Downloads/converted_keras/keras_Model.h5"
labels_path = "c:/Users/mn316/Downloads/converted_keras/labels.txt"
image_folder = r"R:\MarineUAS\Projects\Student Projects\Max\SmartWhalesCont\TeachableMachine\TestV2"
image_size = (224, 224)

# --- Load model and labels ---
model = load_model(model_path, compile=False)
with open(labels_path, "r") as f:
    class_names = [line.strip().split(" ", 1)[-1].lower() for line in f.readlines()]

# --- Natural sort key for filenames ---
def natural_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", s)]

# --- Collect and sort image files ---
image_files = sorted(
    [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".jpeg", ".png"))],
    key=natural_key
)

# --- Preprocess all images ---
data = np.ndarray(shape=(len(image_files), 224, 224, 3), dtype=np.float32)

for i, filename in enumerate(image_files):
    img_path = os.path.join(image_folder, filename)
    image = Image.open(img_path).convert("RGB")
    image = ImageOps.fit(image, image_size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image).astype(np.float32)
    normalized = (image_array / 127.5) - 1
    data[i] = normalized

# --- Predict batch ---
predictions = model.predict(data)

# --- Print estimated Whales confidence for all images ---
for i, prediction in enumerate(predictions):
    index = np.argmax(prediction)
    label = class_names[index]
    confidence = prediction[index]

    if label == "whales":
        whales_confidence = confidence
    else:
        whales_confidence = 1.0 - confidence  # Assuming binary classification

    print(f"{image_files[i]} -> Estimated Whales Confidence: {whales_confidence:.4f}")

try:
    shutil.rmtree(extract_to)
    os.remove(zip_path)
    print(f"Deleted extracted folder: {extract_to}")
    print(f"Deleted ZIP file: {zip_path}")
except Exception as e:
    print(f"Cleanup failed: {e}")