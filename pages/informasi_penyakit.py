import streamlit as st

def show():

    st.markdown("""
    <style>
    
    .text-tentang{
        color:#000000;
        text-align:center;
        font-size:22px;
        line-height:1.9;
        margin-left:50px;
        margin-right:50px;
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
                
    .disease-card{
        box-shadow:0px 4px 15px rgba(0,0,0,0.06);
        background:white
        border:1px solid #E5E7EB;
        border-radius:20px;
        padding:25px;
        margin-bottom:20px;
    }

    .disease-title{
        font-size:32px;
        font-weight:700;
        color:#22c55e;
    }

    .disease-desc{
        font-size:21px;
        line-height:1.9;
        text-align:justify;
        color:#374151;
    }

    .disease-img img{
        border-radius:15px;
    }

    </style>
    """, unsafe_allow_html=True)
    # =========================
    # HEADER
    # =========================
    st.markdown("""
    <div class="card-tentang">
    <div class="section-title">
        Informasi Penyakit Daun Padi
    </div>
    <div class="text-tentang">
    Sebelum melakukan proses deteksi penyakit, pengguna sangat disarankan
    untuk memahami terlebih dahulu karakteristik setiap jenis kondisi daun
    padi yang dapat dikenali oleh sistem ORYLIS. Pemahaman ini penting agar
    hasil prediksi yang diberikan sistem dapat diinterpretasikan dengan lebih
    baik serta membantu pengguna dalam melakukan pengamatan awal terhadap
    kondisi tanaman di lapangan. Sistem ORYLIS dirancang untuk mengklasifikasikan citra daun padi ke dalam
    empat kategori, yaitu <b>Healthy</b>, <b>Brown Spot</b>,
    <b>Hispa</b>, dan <b>Leaf Blast</b>. Masing-masing kategori memiliki
    karakteristik visual yang berbeda sehingga dapat digunakan sebagai
    indikator awal kondisi kesehatan tanaman padi.
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # =========================
    # HEALTHY
    # =========================
    with st.container(border=True):

        st.markdown("""
        <div class="disease-card">
            <div class="disease-title">
                🌱 Healthy
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                "assets/images/healthy.jpg",
                use_container_width=True
            )

        with col2:
            st.markdown("""
            <div class="disease-desc">

            <b>Healthy</b> menunjukkan kondisi daun padi yang sehat dan tidak
            terinfeksi penyakit. Daun umumnya berwarna hijau merata,
            memiliki permukaan yang bersih, serta tidak menunjukkan adanya
            bercak, luka, ataupun perubahan warna yang tidak normal.
            <br>
            <b>Ciri-ciri:</b>
            <ul>
                <li>Hijau merata</li>
                <li>Tidak terdapat bercak</li>
                <li>Tidak terdapat luka</li>
                <li>Pertumbuhan normal</li>
            </ul>

            </div>
            """, unsafe_allow_html=True)
    st.markdown("""
    <hr style="
        border:1px solid #E5E7EB;
        margin-top:30px;
        margin-bottom:30px;
    ">
    """, unsafe_allow_html=True)
    # =========================
    # BROWN SPOT
    # =========================
    with st.container():
        st.markdown("""
        <div class="disease-card">
            <div class="disease-title">
                🟤 Brown Spot
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                "assets/images/brown_spot.jpg",
                use_container_width=True
            )

        with col2:
            st.markdown("""
            <div class="disease-desc">

            <b>Brown Spot</b> merupakan penyakit pada tanaman padi yang disebabkan
            oleh jamur <i>Bipolaris oryzae</i>. Penyakit ini ditandai dengan munculnya
            bercak-bercak berwarna cokelat pada permukaan daun yang umumnya berbentuk
            oval hingga bulat dengan bagian tengah berwarna lebih terang dan tepi yang
            lebih gelap.
            <br>
            <b>Ciri-ciri:</b>
            <ul>
                <li>Muncul bercak berwarna cokelat pada daun</li>
                <li>Bercak berbentuk oval atau bulat</li>
                <li>Bagian tengah bercak berwarna lebih terang</li>
                <li>Tepi bercak berwarna cokelat tua hingga kehitaman</li>
                <li>Pada infeksi berat, bercak dapat menyatu dan memperluas kerusakan daun</li>
            </ul>

            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <hr style="
        border:1px solid #E5E7EB;
        margin-top:30px;
        margin-bottom:30px;
    ">
    """, unsafe_allow_html=True)
    # =========================
    # HISPA
    # =========================
    with st.container():
        st.markdown("""
            <div class="disease-card">
                <div class="disease-title">
                    🐞 Hispa
                </div>
            </div>
            """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                "assets/images/hispa.jpg",
                use_container_width=True
            )

        with col2:
            st.markdown("""
            <div class="disease-desc">

            <b>Hispa</b> merupakan kerusakan daun padi yang disebabkan oleh serangan
            hama <i>Rice Hispa</i> (<i>Dicladispa armigera</i>). Hama ini menyerang
            jaringan daun dengan cara mengikis permukaan daun sehingga menimbulkan
            kerusakan yang khas berupa garis-garis atau bercak memanjang berwarna
            putih keabu-abuan pada helaian daun.
            <br>
            <b>Ciri-ciri:</b>
            <ul>
                <li>Muncul garis-garis putih atau keabu-abuan pada daun</li>
                <li>Terdapat bekas kikisan pada permukaan daun</li>
                <li>Daun tampak transparan atau berwarna pucat pada area tertentu</li>
                <li>Kerusakan umumnya memanjang mengikuti arah tulang daun</li>
                <li>Pada serangan berat, daun dapat mengering dan mengalami penurunan fungsi fotosintesis</li>
            </ul>

            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("""
    <hr style="
        border:1px solid #E5E7EB;
        margin-top:30px;
        margin-bottom:30px;
    ">
    """, unsafe_allow_html=True)
    # =========================
    # LEAF BLAST
    # =========================
    with st.container():
        st.markdown("""
                <div class="disease-card">
                    <div class="disease-title">
                    🔥 Leaf Blast
                    </div>
                </div>
                """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(
                "assets/images/leaf_blast.jpg",
                use_container_width=True
            )

        with col2:
            st.markdown("""
            <div class="disease-desc">

            <b>Leaf Blast</b> merupakan salah satu penyakit utama pada tanaman padi
            yang disebabkan oleh jamur <i>Magnaporthe oryzae</i>. Penyakit ini
            menyerang jaringan daun dan menjadi salah satu faktor yang dapat
            menyebabkan penurunan hasil panen apabila tidak ditangani dengan baik.
            <b>Ciri-ciri:</b>
            <ul>
                <li>Muncul bercak berbentuk belah ketupat atau lonjong</li>
                <li>Bagian tengah bercak berwarna abu-abu atau putih keabu-abuan</li>
                <li>Tepi bercak berwarna cokelat tua hingga kehitaman</li>
                <li>Jumlah bercak dapat bertambah dan menyebar ke seluruh permukaan daun</li>
                <li>Pada serangan berat, daun mengering dan produktivitas tanaman menurun</li>
            </ul>

            </div>
            """, unsafe_allow_html=True)

    st.info(
        "📌 Informasi di atas bertujuan sebagai referensi awal. "
        "Untuk mengetahui kategori penyakit secara otomatis, "
        "silakan gunakan menu Deteksi Penyakit pada sistem ORYLIS."
    )

    st.markdown(
        """
        <center style="text-align: left; color:#64748B; background-color:#F1F5F9; padding:20px; border:1px solid #ddd; border-radius:15px; margin-top:50px; margin-bottom:0px">
            <h4>ORYLIS</h4>
            Oryza Leaf Intelligence System<br>
            Sistem Klasifikasi Penyakit Daun Padi Berbasis Deep Learning
            <br><br>
            © 2026 ORYLIS Team. <br>
            Kontak: rachmatullahrizaldy4@gmail.com
        </center>
        """,
        unsafe_allow_html=True
    )