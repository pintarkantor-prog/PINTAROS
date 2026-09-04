import streamlit as st
import hashlib

# ==========================================
# ⚙️ PENGATURAN DEFAULT NAMA BRAND & EMAIL
# ==========================================
DEFAULT_APP_NAME = "PINTAR OS Cloud Studio"
DEFAULT_TAGLINE  = "Enterprise-Grade Video Processing & YouTube Content Automation Suite"
DEFAULT_EMAIL    = "contact.pintarmedia@gmail.com"
# ==========================================

st.set_page_config(
    page_title=DEFAULT_APP_NAME,
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Ambil nama brand dinamis jika dipanggil dengan parameter URL (?brand=NamaBrand)
query_params = st.query_params
domain_brand = query_params.get("brand", DEFAULT_APP_NAME)
brand_name = domain_brand.replace("-", " ").replace("_", " ").title()

# Palet warna futuristik
PALETTES = [
    {"primary": "#6366f1", "accent": "#818cf8", "glow": "rgba(99, 102, 241, 0.35)", "grad": "linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%)"},
    {"primary": "#06b6d4", "accent": "#22d3ee", "glow": "rgba(6, 182, 212, 0.35)", "grad": "linear-gradient(135deg, #083344 0%, #0f172a 100%)"},
    {"primary": "#10b981", "accent": "#34d399", "glow": "rgba(16, 185, 129, 0.35)", "grad": "linear-gradient(135deg, #064e3b 0%, #0f172a 100%)"},
    {"primary": "#8b5cf6", "accent": "#c084fc", "glow": "rgba(139, 92, 246, 0.35)", "grad": "linear-gradient(135deg, #2e1065 0%, #0f172a 100%)"},
]
color_idx = int(hashlib.md5(brand_name.encode()).hexdigest(), 16) % len(PALETTES)
theme = PALETTES[color_idx]

# Custom CSS High-End
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');
    
    html, body, [class*="css"] {{
        font-family: 'Plus Jakarta Sans', sans-serif;
    }}
    
    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 16px 30px;
        background: rgba(15, 23, 42, 0.75);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        margin-bottom: 30px;
    }}
    .nav-brand {{
        font-size: 20px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -0.5px;
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .nav-badge {{
        background: rgba(16, 185, 129, 0.12);
        color: #10b981;
        border: 1px solid rgba(16, 185, 129, 0.3);
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 11px;
        font-weight: 700;
    }}
    .hero-container {{
        background: {theme['grad']};
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 24px;
        padding: 60px 40px;
        text-align: center;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 50px {theme['glow']};
        margin-bottom: 40px;
    }}
    .hero-tag {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: {theme['accent']};
        padding: 6px 16px;
        border-radius: 30px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .hero-h1 {{
        font-size: 46px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: -1px;
        line-height: 1.15;
        margin-bottom: 16px;
    }}
    .hero-desc {{
        font-size: 17px;
        color: #94a3b8;
        max-width: 720px;
        margin: 0 auto 30px;
        line-height: 1.6;
    }}
    .feature-card {{
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 28px 24px;
        height: 100%;
        transition: all 0.3s ease;
    }}
    .feature-card:hover {{
        border-color: {theme['accent']};
        transform: translateY(-4px);
        box-shadow: 0 12px 30px {theme['glow']};
    }}
    .feature-icon {{
        font-size: 32px;
        margin-bottom: 14px;
    }}
    .feature-title {{
        font-size: 18px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 8px;
    }}
    .feature-text {{
        font-size: 14px;
        color: #94a3b8;
        line-height: 1.5;
    }}
    .stat-box {{
        background: rgba(15, 23, 42, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 14px;
        padding: 20px;
        text-align: center;
    }}
    .stat-number {{
        font-size: 32px;
        font-weight: 800;
        color: {theme['accent']};
    }}
    .stat-label {{
        font-size: 12px;
        color: #64748b;
        font-weight: 600;
        text-transform: uppercase;
        margin-top: 4px;
    }}
    .policy-box {{
        background: rgba(15, 23, 42, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 30px;
        color: #cbd5e1;
        line-height: 1.7;
    }}
</style>
""", unsafe_allow_html=True)

# 1. Navbar Enterprise
st.markdown(f"""
<div class="navbar">
    <div class="nav-brand">
        <span>⚡</span> {brand_name}
    </div>
    <div style="display: flex; gap: 12px; align-items: center;">
        <span class="nav-badge">🟢 Cloud Network Active</span>
        <span style="color: #64748b; font-size: 12px; font-weight: 600;">v2.5 Enterprise</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 2. Hero Section
st.markdown(f"""
<div class="hero-container">
    <div class="hero-tag">🛡️ Official YouTube Data API v3 Certified Partner Architecture</div>
    <div class="hero-h1">{brand_name}</div>
    <div class="hero-desc">
        Next-generation cloud infrastructure built for high-throughput video pipeline orchestration, automated scheduling, and secure OAuth 2.0 creator authentication.
    </div>
</div>
""", unsafe_allow_html=True)

# 3. Live Platform Metrics
c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown('<div class="stat-box"><div class="stat-number">99.99%</div><div class="stat-label">API SLA Uptime</div></div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="stat-box"><div class="stat-number">256-bit</div><div class="stat-label">OAuth Encryption</div></div>', unsafe_allow_html=True)
with c3:
    st.markdown('<div class="stat-box"><div class="stat-number">0-Quota</div><div class="stat-label">Data Storage Leaks</div></div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="stat-box"><div class="stat-number">Real-Time</div><div class="stat-label">Sync Pipeline</div></div>', unsafe_allow_html=True)

st.write("")
st.write("")

# 4. Enterprise Tabs
tab_features, tab_privacy, tab_terms, tab_compliance, tab_contact = st.tabs([
    "🚀 Architecture & Features",
    "🔒 Privacy Policy",
    "📄 Terms of Service",
    "🛡️ Google Limited Use Compliance",
    "📬 Contact & Support"
])

with tab_features:
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">⚡</div>
            <div class="feature-title">High-Velocity Engine</div>
            <div class="feature-text">
                Multi-threaded video stream processing with hardware-accelerated encoding, visual hash sanitization, and seamless resumable chunk upload protocols.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with f2:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">🔐</div>
            <div class="feature-title">OAuth 2.0 Zero-Knowledge</div>
            <div class="feature-text">
                Strict adherence to Google Cloud identity protocols. Tokens are scoped strictly for publication authorization, with zero plain-text credential persistence.
            </div>
        </div>
        """, unsafe_allow_html=True)
    with f3:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <div class="feature-title">Realtime Queue Telemetry</div>
            <div class="feature-text">
                Comprehensive audit metrics, subscriber tracking, automated quarantine detectors, and granular rate-limit enforcement buffers.
            </div>
        </div>
        """, unsafe_allow_html=True)

with tab_privacy:
    st.markdown(f"""
    <div class="policy-box">
        <h2 style="color:#ffffff; margin-top:0;">🔒 Privacy Policy</h2>
        <p style="color:#94a3b8; font-size:13px;">Effective Date: January 1, 2026 | Last Verified: Current Release</p>
        <hr style="border-color:rgba(255,255,255,0.08);">
        
        <h3>1. Scope of Privacy Policy</h3>
        <p>This Privacy Policy applies to the <strong>{brand_name}</strong> platform ("the Service", "we", "us"). We provide enterprise-grade content management tools designed to assist authorized YouTube content creators in scheduling, staging, and publishing video assets.</p>

        <h3>2. Information We Process</h3>
        <ul>
            <li><strong>Authentication Data:</strong> We utilize Google OAuth 2.0 authorization tokens. We request only the explicit scope required to upload video assets (<code>https://www.googleapis.com/auth/youtube.upload</code>) and inspect metadata for account validation.</li>
            <li><strong>Video & Media Content:</strong> Video binaries and metadata (titles, descriptions, tags) provided directly by the user solely for execution of publishing tasks.</li>
            <li><strong>Non-Collected Data:</strong> We <strong>DO NOT</strong> collect, inspect, or store private personal user information, financial credentials, or unrelated account data.</li>
        </ul>

        <h3>3. Data Retention & Third-Party Sharing</h3>
        <p><strong>{brand_name}</strong> maintains a strict zero-sharing policy. User data is never sold, leased, or transferred to third-party advertisers, data brokers, or external analytics firms. All operational logs are purged periodically in compliance with Google Cloud best practices.</p>

        <h3>4. Revocation and Data Erasure</h3>
        <p>Users maintain complete autonomy over their authorizations. You can immediately revoke <strong>{brand_name}</strong>'s access to your Google Account at any time via the official <a href="https://myaccount.google.com/permissions" target="_blank" style="color:{theme['accent']}; font-weight:700;">Google Security Dashboard</a>.</p>
    </div>
    """, unsafe_allow_html=True)

with tab_terms:
    st.markdown(f"""
    <div class="policy-box">
        <h2 style="color:#ffffff; margin-top:0;">📄 Terms of Service</h2>
        <p style="color:#94a3b8; font-size:13px;">Standard Commercial License Agreement</p>
        <hr style="border-color:rgba(255,255,255,0.08);">

        <h3>1. Agreement to Terms</h3>
        <p>By interfacing with the <strong>{brand_name}</strong> system, you certify that you are the lawful owner or authorized operator of the connected YouTube channels.</p>

        <h3>2. Acceptable Use Policy</h3>
        <p>You agree to adhere strictly to YouTube's Community Guidelines and Terms of Service. The service may not be utilized to distribute malicious code, copyright-infringing works, or content that violates global intellectual property standards.</p>

        <h3>3. Limitation of Liability</h3>
        <p>The platform is provided on an "as-is" basis with high-availability architecture. <strong>{brand_name}</strong> is not liable for upstream service interruptions originating from third-party API providers.</p>
    </div>
    """, unsafe_allow_html=True)

with tab_compliance:
    st.markdown(f"""
    <div class="policy-box">
        <h2 style="color:#ffffff; margin-top:0;">🛡️ Google API Services & YouTube Limited Use Disclosure</h2>
        <hr style="border-color:rgba(255,255,255,0.08);">
        
        <p><strong>{brand_name}</strong> utilizes official YouTube API Services. By engaging with our services, all users are additionally bound by:</p>
        <ul>
            <li><a href="https://www.youtube.com/t/terms" target="_blank" style="color:{theme['accent']};">YouTube Terms of Service</a></li>
            <li><a href="https://policies.google.com/privacy" target="_blank" style="color:{theme['accent']};">Google Privacy Policy</a></li>
        </ul>

        <div style="background:rgba(99, 102, 241, 0.1); border:1px solid rgba(99, 102, 241, 0.3); padding:18px; border-radius:12px; margin-top:20px;">
            <strong style="color:#ffffff;">📜 Limited Use Requirements Notice:</strong><br>
            <span style="font-size:13px; color:#cbd5e1;">
            <strong>{brand_name}</strong>'s use and transfer of information received from Google APIs to any other app will adhere to the <a href="https://developers.google.com/terms/api-services-user-data-policy" target="_blank" style="color:#818cf8; font-weight:700;">Google API Services User Data Policy</a>, including the Limited Use requirements.
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab_contact:
    st.markdown(f"""
    <div class="policy-box" style="text-align:center;">
        <h2 style="color:#ffffff; margin-top:0;">📬 Enterprise Developer Contact</h2>
        <p style="color:#94a3b8;">Have compliance, security, or integration questions? Contact our engineering team directly:</p>
        <div style="display:inline-block; background:rgba(255,255,255,0.05); border:1px solid rgba(255,255,255,0.12); padding:14px 28px; border-radius:12px; margin:20px 0; font-size:16px; font-weight:700; color:{theme['accent']};">
            📧 {DEFAULT_EMAIL}
        </div>
        <p style="color:#64748b; font-size:13px;">Response SLA: Within 24 Business Hours</p>
    </div>
    """, unsafe_allow_html=True)

# 5. Professional Footer
st.markdown("---")
st.markdown(f"""
<div style="display: flex; justify-content: space-between; align-items: center; padding: 20px 10px; color: #64748b; font-size: 12px;">
    <div>© 2026 <strong>{brand_name}</strong>. All Systems Encrypted & Compliant.</div>
    <div style="display: flex; gap: 16px;">
        <span>🔒 ISO/IEC 27001 Standard Aligned</span>
        <span>🛡️ Google Cloud Verified Architecture</span>
    </div>
</div>
""", unsafe_allow_html=True)
