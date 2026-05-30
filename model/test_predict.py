# import tensorflow as tf
# import numpy as np
# from PIL import Image

# from triplet_attention import TripletAttention

# # Load model
# model = tf.keras.models.load_model(
#     "efnb2_triplet_final_20251126-175144.keras",
#     custom_objects={
#         "TripletAttention": TripletAttention
#     },
#     compile=False
# )

# print(model.output_shape)

# # Ganti sesuai urutan class training
# CLASS_NAMES = [
#     "Brown Spot",
#     "Healthy",
#     "Hispa",
#     "Leaf Blast"
# ]

# # Buka gambar contoh
# img = Image.open("../assets/images/healthy.jpg").convert("RGB")

# # Resize (sementara)
# img = img.resize((260,260))

# img = np.array(img)

# img = img / 255.0

# img = np.expand_dims(img, axis=0)

# pred = model.predict(img)

# print(pred)

# print("Prediksi :", CLASS_NAMES[np.argmax(pred)])

# print("Confidence :", np.max(pred) * 100)

# print("Jumlah output:", model.output_shape[-1])

import tensorflow as tf
import numpy as np
from PIL import Image

from triplet_attention import TripletAttention

# =========================
# LOAD MODEL
# =========================
model = tf.keras.models.load_model(
    "efnb2_triplet_final_20251126-175144.keras",
    custom_objects={
        "TripletAttention": TripletAttention
    },
    compile=False
)

# =========================
# CLASS NAMES
# =========================
classes = [
    "Brown Spot",
    "Hispa",
    "Leaf Blast"
]

# =========================
# LOAD IMAGE
# =========================
img = Image.open("../assets/images/brown_spot.jpg").convert("RGB")

# ukuran harus sama seperti training
IMG_SIZE = 260

img = img.resize((IMG_SIZE, IMG_SIZE))

# =========================
# PREPROCESS
# =========================
img_array = np.array(img)

img_array = img_array / 255.0

img_array = np.expand_dims(img_array, axis=0)

# =========================
# PREDICT
# =========================
pred = model.predict(img_array)[0]

print("RAW OUTPUT :", pred)

confidence = float(np.max(pred))
class_idx = int(np.argmax(pred))

THRESHOLD = 0.85

if confidence < THRESHOLD:
    label = "Healthy"
else:
    label = classes[class_idx]

# =========================
# RESULT
# =========================
print("Prediksi :", label)
print("Confidence :", round(confidence * 100, 2), "%")