import streamlit as st
import tensorflow as tf
import numpy as np
import time

from PIL import Image

from model.triplet_attention import TripletAttention

# =========================
# LOAD MODEL
# =========================
@st.cache_resource
def load_model():

    model = tf.keras.models.load_model(
        "model/efnb2_triplet_final_20251126-175144.keras",
        custom_objects={
            "TripletAttention": TripletAttention
        },
        compile=False
    )

    return model

model = load_model()

# =========================
# SHOW PAGE
# =========================
def show():

    # =========================
    # CUSTOM CSS
    # =========================
    st.markdown("""
    <style>

    button[data-baseweb="tab"] {
    font-size:16px;
    font-weight:600;
    color:#475569;
    }

                
    
    /* Warna teks spinner */
    .stSpinner > div {
        color: #16A34A !important;
        font-weight: 600;
    }

    /* Warna animasi spinner */
    .stSpinner svg {
        stroke: #16A34A !important;
    }
            
    /* Text upload */
    [data-testid="stFileUploader"] label {
        color: #22C55E;
        font-size: 20px;
        font-weight: 700;
    }

    /* Kotak upload */
    [data-testid="stFileUploader"] section {
        background: white;
        border: 2px dashed #22C55E;
        border-radius: 15px;
        padding: 20px;
    }

    /* Tulisan kecil di dalam box */
    [data-testid="stFileUploader"] small {
        color: #6B7280;
    }
                
    /* Button upload */
    [data-testid="stFileUploader"] button {
        background-color: #22C55E;
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: 600;
    }

    /* Hover button upload */
    [data-testid="stFileUploader"] button:hover {
        background-color: white;
        color: #22C55E !important;
        border: 1px solid #22C55E;
    }

    /* Icon upload */
    [data-testid="stFileUploader"] button svg {
        fill: currentColor !important;
    }
        
    .detect-title{
        text-align:center;
        font-size:42px;
        font-weight:800;
        color:#16A34A;
        margin-bottom:10px;
    }

    .detect-subtitle{
        text-align:center;
        font-size:20px;
        color:white;
        margin-bottom:40px;
        line-height:1.7;
        color:black;
    }

    .result-card{
        background:white;
        padding:30px;
        border-radius:20px;
        box-shadow:0px 4px 20px rgba(0,0,0,0.1);
        margin-top:30px;
    }

    .result-title{
        font-size:32px;
        font-weight:700;
        color:#2E7D32;
        margin-bottom:10px;
    }

    .result-confidence{
        font-size:20px;
        color:#444;
        margin-bottom:20px;
    }

    .disease-desc{
        font-size:18px;
        line-height:1.8;
        text-align:justify;
        color:#333;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================
    # HEADER
    # =========================
    st.markdown("""
    <div class="detect-title">
        Klasifikasi Penyakit Daun Padi
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="detect-subtitle">
        Unggah gambar daun padi untuk melakukan proses klasifikasi
        penyakit menggunakan model Deep Learning ORYLIS.
    </div>
    """, unsafe_allow_html=True)

    # =========================
    # UPLOAD IMAGE
    # =========================
    tab1, tab2 = st.tabs([
    "📁 Unggah Gambar",
    "📷 Ambil dari Kamera"
    ])

    uploaded_file = None
    camera_image = None

    # =========================
    # TAB UPLOAD
    # =========================
    with tab1:

        uploaded_file = st.file_uploader(
            "Pilih gambar daun tanaman (JPG/PNG)",
            type=["jpg", "jpeg", "png"]
        )

    # =========================
    # TAB CAMERA
    # =========================
    with tab2:

        if "camera_on" not in st.session_state:
            st.session_state.camera_on = False

        col1, col2, col3 = st.columns([1, 1, 4])

        with col1:
            if st.button("📷 Hidupkan Kamera"):
                st.session_state.camera_on = True

        with col2:
            if st.button("❌ Matikan Kamera"):
                st.session_state.camera_on = False

        if st.session_state.camera_on:
            camera_image = st.camera_input(
                "Ambil foto daun padi"
            )

    # =========================
    # SELECT IMAGE
    # =========================
    image_file = None

    if uploaded_file is not None:
        image_file = uploaded_file

    elif camera_image is not None:
        image_file = camera_image    

    # =========================
    # IF IMAGE UPLOADED
    # =========================
    # =========================
    # IF IMAGE UPLOADED
    # =========================
    if image_file is not None:

        image = Image.open(image_file).convert("RGB")

        # =========================
        # BUTTON
        # =========================
        detect = st.button("🔍 Start Scanning")

        if detect:
            
            with st.spinner("Sedang mendeteksi penyakit..."):

                # progress = st.progress(0)

                # for i in range(100):
                #     time.sleep(0.01)
                #     progress.progress(i + 1)


                # =========================
                # PREPROCESS
                # =========================
                IMG_SIZE = 260

                img = image.resize((IMG_SIZE, IMG_SIZE))

                img_array = np.array(img)

                img_array = img_array / 255.0

                img_array = np.expand_dims(img_array, axis=0)

                # =========================
                # PREDICT
                # =========================
                pred = model.predict(img_array)[0]

                classes = [
                    "Brown Spot",
                    "Hispa",
                    "Leaf Blast"
                ]

                confidence = float(np.max(pred))

                class_idx = int(np.argmax(pred))

                # THRESHOLD = 0.85

                # if confidence < THRESHOLD:
                #     label = "Healthy"
                # else:
                label = classes[class_idx]

                # =========================
                # DESCRIPTION
                # =========================
                descriptions = {

                    "Healthy":
                    "Daun padi berada dalam kondisi sehat dengan warna hijau merata dan tidak menunjukkan gejala penyakit.",

                    "Brown Spot":
                    "Brown Spot merupakan penyakit akibat infeksi jamur Bipolaris oryzae yang ditandai bercak cokelat pada daun.",

                    "Hispa":
                    "Hispa disebabkan oleh serangan hama yang menimbulkan garis putih memanjang pada permukaan daun.",

                    "Leaf Blast":
                    "Leaf Blast merupakan penyakit akibat jamur Magnaporthe oryzae yang ditandai bercak berbentuk belah ketupat."

                }

                # =========================
                # INLINE LAYOUT
                # =========================
                col1, col2 = st.columns([1, 1.2])

                # =========================
                # LEFT SIDE IMAGE
                # =========================
                with col1:

                    # st.markdown("""
                    # <div style="
                    #     background:#0F172A;
                    #     padding:20px;
                    #     border-radius:20px;
                    #     border:1px solid rgba(255,255,255,0.08);
                    # ">
                    # """, unsafe_allow_html=True)

                    st.image(
                        image,
                        use_container_width=True
                    )

                    st.markdown("""
                    <center style="
                        color:#aaaaaa;
                        margin-top:10px;
                        font-size:15px;
                    ">
                        Gambar yang Diunggah
                    </center>
                    """, unsafe_allow_html=True)

                    st.markdown("</div>", unsafe_allow_html=True)

                # =========================
                # RIGHT SIDE RESULT
                # =========================
                with col2:

                    st.markdown(f"""
                    <div style="
                        background:linear-gradient(135deg,#ffffff,#F1F5F9);
                        padding:35px;
                        border-radius:25px;
                        box-shadow:0px 10px 30px rgba(0,0,0,0.15);
                        height:100%;
                    ">

                    <div style="
                        font-size:40px;
                        font-weight:700;
                        color:#16A34A;
                        letter-spacing:1px;
                        margin-bottom:15px;
                        ">
                        KLASIFIKASI GAMBAR BERHASIL!
                    </div>
                    
                    <div style="
                        font-size:32px;
                        font-weight:800;
                        color:#111827;
                        margin-bottom:5px;
                    ">
                        Nama Penyakit:
                    </div>
                    
                    <div style="
                        font-size:42px;
                        font-weight:800;
                        color:#111827;
                        margin-bottom:5px;
                    ">
                        {label}
                    </div>

                    <div style="
                        font-size:22px;
                        font-weight:600;
                        color:#16A34A;
                        margin-bottom:30px;
                    ">
                        Confidence Score: {confidence*100:.2f}%
                    </div>

                    <div style="
                        background:#ECFDF5;
                        padding:25px;
                        border-radius:18px;
                        border-left:6px solid #16A34A;
                    ">

                    <div style="
                        font-size:22px;
                        font-weight:700;
                        color:#111827;
                        margin-bottom:15px;
                    ">
                        Penjelasan
                    </div>

                    <div style="
                        font-size:18px;
                        line-height:1.9;
                        color:#374151;
                        text-align:justify;
                    ">
                        {descriptions[label]}
                    </div>

                        
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown(
        """
        <center style="text-align: left; color:#64748B; background-color:#F1F5F9; padding:20px; border:1px solid #ddd; border-radius:15px; margin-top:50px; margin-bottom:0px">
            <h4>ORYLIS</h4>
            Oryza Leaf Intelligence System<br>
            Sistem Klasifikasi Penyakit Daun Padi Berbasis Deep Learning
            <br><br>
            © 2026 ORYLIS Team. <br>
            Oleh: Prof. Dr. Rima Tri Wahyuningrum, ST., MT.<br>
            Rachmatullah Rizaldy<br>
            Prodi: Teknik Informatika dan S2 PSDA<br>
            Universitas Trunojoyo Madura
        </center>
        """,
        unsafe_allow_html=True
    )