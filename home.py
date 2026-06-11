import streamlit as st
from streamlit_option_menu import option_menu

from pages.informasi_penyakit import show as show_info
from pages.deteksi_penyakit import show as show_deteksi

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="ORYLIS",
    page_icon="🌾",
    layout="wide"
)

# selected = option_menu(
#     menu_title=None,
#     options=[
#         "Home",
#         "Informasi Penyakit",
#         "Klasifikasi Penyakit"
#     ],
#     icons=[
#         "house",
#         "book",
#         "search"
#     ],
#     orientation="horizontal"
# )

# =========================
# SESSION STATE
# =========================
if "selected_menu" not in st.session_state:
    st.session_state.selected_menu = "Home"

selected = option_menu(
    menu_title=None,
    options=[
        "Home",
        "Informasi Penyakit",
        "Klasifikasi Penyakit"
    ],
    icons=[
        "house",
        "book",
        "search"
    ],
    orientation="horizontal",

    default_index=[
        "Home",
        "Informasi Penyakit",
        "Klasifikasi Penyakit"
    ].index(st.session_state.selected_menu),

    styles={
        "container": {
            "padding": "10px",
            "background-color": "#FFFFFF",
            "border-radius": "0px",
            "box-shadow": "0px 4px 15px rgba(0,0,0,0.08)",
            "border": "1px solid #E2E8F0",
        },

        "icon": {
            "color": "#16A34A",
            "font-size": "18px"
        },

        "nav-link": {
            "font-size": "16px",
            "font-weight": "600",
            "text-align": "center",
            "margin": "0px 6px",
            "padding": "12px",
            "border-radius": "12px",
            "color": "#475569",
            "--hover-color": "#DCFCE7",
        },

        "nav-link-selected": {
            "background": "linear-gradient(135deg,#16A34A,#22C55E)",
            "color": "white",
            "font-weight": "700",
        },
    }
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

/* =========================
   HIDE STREAMLIT DEFAULT
========================= */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* =========================
   GLOBAL
========================= */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    background-color:#F5F7FA;
    color:#ffffff;
}

/* Main background */
.stApp{
    background: linear-gradient(to bottom, #F8FAFC, #EEF2F7);
}

/* =========================
   NAVBAR
========================= */
.nav-link {
    font-size:16px !important;
}
            


/* =========================
   HERO
========================= */
.hero-title{
    font-size:64px;
    font-weight:800;
    color:#16A34A;
    margin-bottom:0px;
}

.hero-subtitle{
    font-size:20px;
    color:#475569;
    margin-top:10px;
    line-height:1.8;
}

/* =========================
   SECTION TITLE
========================= */
.section-title{
    text-align:center;
    font-size:42px;
    font-weight:800;
    color:#16A34A;
    margin-top:40px;
    margin-bottom:25px;
}

/* =========================
   CARD
========================= */
.card{
    background: linear-gradient(135deg, #052E16, #166534);
    padding:30px;
    border-radius:22px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.08);
    border:1px solid #E2E8F0;
    transition:0.3s;
    height:240px;
}

.card-tentang{
    background:white;
    padding:30px;
    border-radius:22px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.08);
    border:1px solid #E2E8F0;
    transition:0.3s;
    height:500px;
}

.card-text{
    padding:30px;
    border:1px solid #E2E8F0;
    transition:0.3s;
}            

.card:hover{
    transform:translateY(-5px);
}

.card-title{
    font-size:24px;
    font-weight:700;
    color:#22C55E;
}

.card p{
    font-size:20px;
    color:white;
    margin-top:10px;
    text-align:justify;
    line-height:1.8;
}

/* =========================
   ABOUT TEXT
========================= */
.text-tentang{
    color:#000000;
    text-align:center;
    font-size:22px;
    line-height:1.9;
    margin-left:50px;
    margin-right:50px;
}

/* =========================
   BUTTON
========================= */
.stButton>button{
    background:linear-gradient(135deg,#16A34A,#22C55E);
    color:white;
    border:none;
    padding:12px 25px;
    border-radius:14px;
    font-size:16px;
    font-weight:600;
    transition:0.3s;
    width:100%;
}

.stButton>button:hover{
    transform:translateY(-2px);
    box-shadow:0px 6px 20px rgba(34,197,94,0.3);
}

/* =========================
   INFO BOX
========================= */
[data-testid="stInfo"]{
    background:#FFFFFF;
    border:1px solid #D1FAE5;
    border-radius:18px;
    padding:10px;
}

/* =========================
   FOOTER
========================= */
.footer{
    text-align:center;
    color:#64748B;
    margin-top:50px;
    padding-top:20px;
    padding-bottom:20px;
    border-top:1px solid #CBD5E1;
    line-height:1.8;
}

</style>
""", unsafe_allow_html=True)

if selected == "Home":

    # =========================
    # HERO SECTION
    # =========================
    col1, col2 = st.columns([1.3, 1])

    with col1:

        st.markdown(
            """
            <div class="hero-title">
                ORYLIS
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="hero-subtitle">
            <b>Oryza Leaf Intelligence System</b><br><br>

            Sistem klasifikasi penyakit daun padi berbasis Deep Learning
            yang dirancang untuk membantu identifikasi kondisi daun padi
            secara otomatis melalui analisis citra digital.
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        col_btn1, col_btn2, col_empty = st.columns([1,1,1.5])

        with col_btn1:
            if st.button("🌾 Mulai Klasifikasi"):

                st.session_state.selected_menu = "Klasifikasi Penyakit"
                st.rerun()

        with col_btn2:
            if st.button("📚 Pelajari Penyakit"):

                st.session_state.selected_menu = "Informasi Penyakit"
                st.rerun()

    with col2:

        st.image(
            "assets/WhatsApp Image 2026-05-24 at 21.44.02.jpeg",
            use_container_width=True
        )

    st.divider()

    # =========================
    # ABOUT SECTION
    # =========================
    st.markdown(
        """
        <div class="card-tentang">
        <div class="section-title">
            Tentang ORYLIS
        </div>
        <div  class="text-tentang">
        ORYLIS (Oryza Leaf Intelligence System) merupakan sistem klasifikasi
        penyakit daun padi yang memanfaatkan teknologi Deep Learning untuk
        membantu proses identifikasi kondisi daun padi secara otomatis.

        Sistem menerima citra daun padi sebagai masukan dan melakukan proses
        klasifikasi untuk menentukan kategori penyakit yang terdeteksi.
        Dengan pendekatan kecerdasan buatan, pengguna dapat memperoleh
        informasi awal mengenai kondisi tanaman secara cepat dan mudah.
        </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()



    # =========================
    # TECHNOLOGY SECTION
    # =========================
    st.markdown(
        """
        <div class="section-title">
            Teknologi yang Digunakan
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card">
            <div class="card-title">
                EfficientNet-B2
            </div>
            <p>
            Model Convolutional Neural Network yang digunakan sebagai backbone
            klasifikasi citra karena memiliki keseimbangan yang baik antara
            akurasi dan efisiensi komputasi
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="card">
            <div class="card-title">
                TensorFlow & Keras
            </div>
            <p>
            Framework Deep Learning yang digunakan untuk proses pelatihan,
            evaluasi, dan inferensi model klasifikasi penyakit daun padi.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">
            <div class="card-title">
                Triplet Attention
            </div>
            <p>
            Mekanisme perhatian yang ditambahkan pada model untuk membantu
            proses ekstraksi fitur dan meningkatkan fokus model terhadap
            informasi penting pada citra daun padi.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        st.markdown("""
        <div class="card">
            <div class="card-title">
                Streamlit
            </div>
            <p>
            Framework Python yang digunakan untuk membangun aplikasi web
            interaktif sehingga sistem dapat digunakan secara mudah dan
            responsif oleh pengguna.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # =========================
    # ADVANTAGES SECTION
    # =========================
    st.markdown(
        """
        <div class="section-title">
            Keunggulan Sistem
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("⚡ Deteksi Cepat\n\nProses klasifikasi dilakukan dalam hitungan detik.")

    with col2:
        st.info("🌱 Mudah Digunakan\n\nCukup unggah gambar daun padi, sistem akan memberikan hasil klasifikasi.")

    with col3:
        st.info("🧠 Berbasis Deep Learning\n\nMenggunakan model AI modern.")

    with col4:
        st.info("📊 Confidence Score\n\nMenampilkan tingkat keyakinan prediksi.")

    st.divider()

    # =========================
    # FOOTER
    # =========================
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

elif selected == "Informasi Penyakit":

    show_info()

elif selected == "Klasifikasi Penyakit":

    show_deteksi()