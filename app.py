import streamlit as st
import hashlib

# ==========================================
# ⚙️ PENGATURAN DEFAULT NAMA BRAND & EMAIL
# ==========================================
DEFAULT_APP_NAME = "Pintar Media Studio"
DEFAULT_EMAIL    = "pintarmedia@gmail.com"
# ==========================================

st.set_page_config(
    page_title="Pintar Media Platform",
    page_icon="🎬",
    layout="wide"
)

# Ambil nama brand dinamis dari link URL (?brand=NamaBrand) jika ada
query_params = st.query_params
domain_brand = query_params.get("brand", DEFAULT_APP_NAME)
brand_name = domain_brand.replace("-", " ").replace("_", " ").title()

# Palet warna dinamis otomatis
PALETTES = [
    {"primary": "#6366f1", "accent": "#818cf8", "bg_grad": "linear-gradient(135deg, #1e1b4b, #0f172a)"},
    {"primary": "#06b6d4", "accent": "#22d3ee", "bg_grad": "linear-gradient(135deg, #083344, #0f172a)"},
    {"primary": "#10b981", "accent": "#34d399", "bg_grad": "linear-gradient(135deg, #064e3b, #0f172a)"},
    {"primary": "#f59e0b", "accent": "#fbbf24", "bg_grad": "linear-gradient(135deg, #451a03, #0f172a)"},
    {"primary": "#8b5cf6", "accent": "#a78bfa", "bg_grad": "linear-gradient(135deg, #2e1065, #0f172a)"},
]
color_idx = int(hashlib.md5(brand_name.encode()).hexdigest(), 16) % len(PALETTES)
theme = PALETTES[color_idx]

st.markdown(f"""
<style>
    .hero-box {{
        background: {theme['bg_grad']};
        padding: 40px 30px;
        border-radius: 16px;
        border: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        margin-bottom: 25px;
    }}
    .hero-title {{
        font-size: 34px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 8px;
    }}
    .hero-sub {{
        font-size: 15px;
        color: #94a3b8;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.5;
    }}
    .badge {{
        background: {theme['primary']};
        color: #ffffff;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
        margin-bottom: 12px;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero-box">
    <div class="badge">🛡️ Verified Platform</div>
    <div class="hero-title">{brand_name}</div>
    <div class="hero-sub">
        Cloud Automation Platform for YouTube Content Scheduling and Digital Workflow Management.
    </div>
</div>
""", unsafe_allow_html=True)

tab_overview, tab_privacy, tab_terms, tab_compliance = st.tabs([
    "🏠 Overview",
    "🔒 Privacy Policy",
    "📄 Terms of Service",
    "🛡️ YouTube API Compliance"
])

with tab_overview:
    st.write(f"Welcome to **{brand_name}**, a dedicated management tool for scheduling and uploading content to authorized YouTube channels.")
    st.info("Our platform strictly adheres to Google Cloud Security Standards and OAuth 2.0 Protocols.")

with tab_privacy:
    st.markdown(f"""
    ### 🔒 Privacy Policy for {brand_name}
    *Last Updated: 2026*

    **1. Data Collection:**  
    Our tool connects to YouTube via Google OAuth 2.0. We only request permissions necessary to manage and upload video content (`youtube.upload`). We do not store or sell your private personal credentials.

    **2. Data Usage:**  
    Data is solely used to verify channel ownership and execute video publication requests requested by the user.

    **3. Revoking Access:**  
    Users can revoke access anytime via [Google Account Security Settings](https://myaccount.google.com/permissions).
    """)

with tab_terms:
    st.markdown(f"""
    ### 📄 Terms of Service
    By accessing **{brand_name}**, you agree to comply with all applicable laws and YouTube Community Guidelines. The service is provided 'as-is' for authorized creators.
    """)

with tab_compliance:
    st.markdown(f"""
    ### 🛡️ Google API Services & YouTube Compliance
    **{brand_name}** complies with the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.
    """)

st.markdown("---")
st.markdown(f"<div style='text-align:center; color:#64748b; font-size:12px;'>© 2026 {brand_name}. Contact: {DEFAULT_EMAIL}</div>", unsafe_allow_html=True)
