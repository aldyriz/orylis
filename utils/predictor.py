import tensorflow as tf
import numpy as np
from PIL import Image

from triplet_attention import TripletAttention

# Load model
model = tf.keras.models.load_model(
    "efnb2_triplet_final_20251126-175144.keras",
    custom_objects={
        "TripletAttention": TripletAttention
    },
    compile=False
)

# Nama kelas
CLASS_NAMES = [
    "Brown Spot",
    "Healthy",
    "Hispa",
    "Leaf Blast"
]

# Buka gambar
img = Image.open("sample.jpg").convert("RGB")

# Resize sesuai training
img = img.resize((260,260))

# Konversi ke array
img = np.array(img) / 255.0

# Tambah batch dimension
img = np.expand_dims(img, axis=0)

# Prediksi
pred = model.predict(img)

print(pred)

print("Label :", CLASS_NAMES[np.argmax(pred)])
print("Confidence :", np.max(pred) * 100)