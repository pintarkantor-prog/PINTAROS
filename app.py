import streamlit as st
import hashlib

# ==========================================
# ⚙️ PENGATURAN NAMA & IDENTITAS BRAND
# ==========================================
DEFAULT_APP_NAME = "PINTAR OS Cloud Studio"
DEFAULT_EMAIL    = "contact.pintarmedia@gmail.com"
# ==========================================

st.set_page_config(
    page_title="PINTAR OS - Automation Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ambil nama brand dinamis jika dipanggil dengan parameter URL (?brand=NamaBrand)
query_params = st.query_params
domain_brand = query_params.get("brand", DEFAULT_APP_NAME)
brand_name = domain_brand.replace("-", " ").replace("_", " ").title()

# Custom CSS — MURNI DESIGN SYSTEM PINTAR OS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');
    
    html, body, [class*="css"], .stApp {
        background-color: #090d16 !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #c8cdd5 !important;
    }
    
    /* Header Title */
    .pintar-header {
        margin-bottom: 20px;
    }
    .pintar-title {
        font-size: 26px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .pintar-subtitle {
        font-size: 13px;
        color: #7e89ac;
        margin-top: 4px;
    }
    
    /* Status Panel Bar (Mirip persis PINTAR OS) */
    .status-panel {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background: #0e1630;
        border: 1px solid rgba(129, 140, 248, 0.12);
        border-radius: 12px;
        padding: 16px 24px;
        margin-bottom: 24px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
    }
    .status-group {
        display: flex;
        align-items: center;
        gap: 28px;
    }
    .status-item {
        display: flex;
        flex-direction: column;
        gap: 3px;
    }
    .status-label {
        font-size: 10px;
        font-weight: 700;
        text-transform: uppercase;
        color: #7e89ac;
        letter-spacing: 0.8px;
    }
    .status-val {
        font-size: 13px;
        font-weight: 700;
        color: #c8cdd5;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    
    .badge-live-connected {
        background: rgba(16, 185, 129, 0.12);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.25);
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 700;
    }
    
    /* Card Container */
    .pintar-card {
        background: #0e1630;
        border: 1px solid rgba(129, 140, 248, 0.12);
        border-radius: 14px;
        padding: 24px;
        margin-bottom: 20px;
    }
    .pintar-card h3 {
        color: #818cf8;
        font-size: 16px;
        font-weight: 700;
        margin-top: 0;
        margin-bottom: 12px;
    }
    .pintar-card p, .pintar-card li {
        font-size: 13px;
        color: #9ca3af;
        line-height: 1.6;
    }
    
    /* Policy Box */
    .policy-container {
        background: #0b1021;
        border: 1px solid rgba(129, 140, 248, 0.15);
        border-radius: 12px;
        padding: 28px;
        margin-top: 10px;
    }
    .policy-container h2 {
        color: #ffffff;
        font-size: 18px;
        font-weight: 700;
        margin-top: 0;
    }
    .policy-container h3 {
        color: #818cf8;
        font-size: 14px;
        font-weight: 700;
        margin-top: 18px;
        margin-bottom: 8px;
    }
    .policy-container p, .policy-container li {
        font-size: 13px;
        color: #cbd5e1;
        line-height: 1.7;
    }
    
    /* Tab Navigation Style */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 8px;
        color: #7e89ac;
        padding: 8px 16px;
        font-weight: 700;
        font-size: 12px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #6c72ff !important;
        color: #ffffff !important;
        border-color: #6c72ff !important;
    }
</style>
""", unsafe_allow_html=True)

# 1. Header Utama PINTAR OS
st.markdown(f"""
<div class="pintar-header">
    <div class="pintar-title">
        <span>⚡</span> {brand_name.upper()}
    </div>
    <div class="pintar-subtitle">
        Sistem otomasi manajemen konten video, integrasi cloud scheduler, dan sinkronisasi resmi Google YouTube Data API v3.
    </div>
</div>
""", unsafe_allow_html=True)

# 2. Status Panel (Mirip Toolbar PINTAR OS)
st.markdown("""
<div class="status-panel">
    <div class="status-group">
        <div class="status-item">
            <span class="status-label">WORKER CLUSTER</span>
            <span class="status-val" style="color:#818cf8;">PINTAR-CLOUD (NODE_1)</span>
        </div>
        <div class="status-item">
            <span class="status-label">OAUTH 2.0 PROTOCOL</span>
            <span class="status-val"><span class="badge-live-connected">● AKTIF & TERENKRIPSI</span></span>
        </div>
        <div class="status-item">
            <span class="status-label">API GATEWAY</span>
            <span class="status-val" style="color:#10b981;">Google YouTube v3 (Verified Architecture)</span>
        </div>
        <div class="status-item">
            <span class="status-label">SYSTEM STATUS</span>
            <span class="status-val" style="color:#6c72ff;">Ready / Operational</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 3. Tab Navigasi PINTAR OS
tab_app, tab_privacy, tab_terms, tab_compliance = st.tabs([
    "🚀 Arsitektur Sistem",
    "🔒 Kebijakan Privasi (Privacy Policy)",
    "📄 Syarat Layanan (Terms of Service)",
    "🛡️ Kepatuhan YouTube API"
])

with tab_app:
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="pintar-card">
            <h3>⚡ High-Throughput Engine</h3>
            <p>
                Didukung oleh pipeline render video otomatis, pemindaian folder multi-antrean, serta sistem upload berbasis chunk aman berkecepatan tinggi.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="pintar-card">
            <h3>🔐 Keamanan Zero-Credential</h3>
            <p>
                Menggunakan standar resmi Google OAuth 2.0. Sistem tidak menyimpan password akun Google secara plain-text, serta akses dapat dicabut kapan saja.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="pintar-card">
            <h3>📊 Audit & Monitoring Realtime</h3>
            <p>
                Telemetri kuota API Google harian terproteksi, monitoring status kesehatan channel, dan pencegahan error duplikasi secara cerdas.
            </p>
        </div>
        """, unsafe_allow_html=True)

with tab_privacy:
    st.markdown(f"""
    <div class="policy-container">
        <h2>🔒 Kebijakan Privasi ({brand_name})</h2>
        <p style="color:#7e89ac; font-size:12px;">Terakhir diperbarui: 2026 | Dokumen Kepatuhan Pengembang Resmi</p>
        <hr style="border-color:rgba(255,255,255,0.08);">

        <h3>1. Pendahuluan</h3>
        <p>
            <strong>{brand_name}</strong> ("kami") menghormati privasi pengguna dan berkomitmen untuk melindungi data akun yang terhubung ke platform otomasi kami. Dokumen ini menjelaskan bagaimana data diakses, digunakan, dan dilindungi.
        </p>

        <h3>2. Data yang Diakses & Digunakan</h3>
        <p>
            Aplikasi kami menggunakan protokol resmi Google OAuth 2.0 untuk meminta izin akses terbatas (scope: <code>https://www.googleapis.com/auth/youtube.upload</code> dan <code>youtube.readonly</code>). 
        </p>
        <ul>
            <li><strong>Penggunaan Izin:</strong> Hanya digunakan untuk memvalidasi channel milik pengguna dan mengunggah video yang dijadwalkan secara sah oleh pemilik akun.</li>
            <li><strong>Data yang TIDAK Diambil:</strong> Kami <strong>TIDAK PERNAH</strong> mengambil, menyimpan, atau memperjualbelikan password pribadi, data finansial, atau data kontak pengguna kepada pihak ketiga mana pun.</li>
        </ul>

        <h3>3. Penyimpanan & Keamanan Data</h3>
        <p>
            Seluruh token otentikasi disimpan dengan enkripsi standar industri (AES-256) dan hanya digunakan selama proses eksekusi tugas pengunggahan video berlangsung.
        </p>

        <h3>4. Pencabutan Izin (Revoke Access)</h3>
        <p>
            Pengguna memiliki kontrol penuh dan dapat mencabut izin akses aplikasi ini kapan saja melalui <a href="https://myaccount.google.com/permissions" target="_blank" style="color:#818cf8; font-weight:700;">Pengaturan Keamanan Akun Google</a>.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab_terms:
    st.markdown(f"""
    <div class="policy-container">
        <h2>📄 Syarat & Ketentuan Layanan</h2>
        <p style="color:#7e89ac; font-size:12px;">Ketentuan Penggunaan Platform Otomasi</p>
        <hr style="border-color:rgba(255,255,255,0.08);">

        <h3>1. Persetujuan Pengguna</h3>
        <p>
            Dengan menggunakan layanan <strong>{brand_name}</strong>, Anda menyatakan bahwa Anda adalah pemilik sah atau pihak yang memiliki wewenang penuh atas channel YouTube yang dikaitkan.
        </p>

        <h3>2. Kepatuhan Pedoman Komunitas</h3>
        <p>
            Pengguna wajib mematuhi seluruh Pedoman Komunitas YouTube serta hukum hak cipta yang berlaku. Dilarang menggunakan sistem ini untuk menyebarkan konten berbahaya atau melanggar hak cipta.
        </p>
    </div>
    """, unsafe_allow_html=True)

with tab_compliance:
    st.markdown(f"""
    <div class="policy-container">
        <h2>🛡️ Pernyataan Kepatuhan Google API & YouTube</h2>
        <hr style="border-color:rgba(255,255,255,0.08);">

        <p>
            Aplikasi <strong>{brand_name}</strong> menggunakan Layanan YouTube API. Dengan menggunakan platform ini, pengguna juga terikat oleh:
        </p>
        <ul>
            <li><a href="https://www.youtube.com/t/terms" target="_blank" style="color:#818cf8;">Persyaratan Layanan YouTube (YouTube Terms of Service)</a></li>
            <li><a href="https://policies.google.com/privacy" target="_blank" style="color:#818cf8;">Kebijakan Privasi Google (Google Privacy Policy)</a></li>
        </ul>

        <div style="background:rgba(108, 114, 255, 0.08); border:1px solid rgba(108, 114, 255, 0.25); padding:16px; border-radius:10px; margin-top:16px;">
            <strong style="color:#ffffff;">Pemberitahuan Persyaratan Penggunaan Terbatas (Limited Use):</strong><br>
            <span style="font-size:12px; color:#cbd5e1;">
            Penggunaan dan transfer informasi yang diterima <strong>{brand_name}</strong> dari Google API ke aplikasi lain akan mematuhi <a href="https://developers.google.com/terms/api-services-user-data-policy" target="_blank" style="color:#818cf8; font-weight:700;">Kebijakan Data Pengguna Layanan Google API</a>, termasuk persyaratan Penggunaan Terbatas.
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer PINTAR OS
st.markdown("---")
st.markdown(f"""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 0; color: #7e89ac; font-size: 11px;">
    <div>© 2026 <strong>{brand_name}</strong>. Powered by PINTAR OS Architecture.</div>
    <div>Kontak Pengembang: <span style="color:#818cf8; font-weight:700;">{DEFAULT_EMAIL}</span></div>
</div>
""", unsafe_allow_html=True)
