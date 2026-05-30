import tensorflow as tf
from triplet_attention import TripletAttention

model = tf.keras.models.load_model(
    "efnb2_triplet_final_20251126-175144 (1).keras",
    custom_objects={
        "TripletAttention": TripletAttention
    },
    compile=False
)

print("MODEL BERHASIL DIMUAT")