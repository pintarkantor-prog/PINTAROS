import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="PINTAR OS - Cloud Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Sembunyikan header dan footer bawaan Streamlit
st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    iframe {border: none !important;}
</style>
""", unsafe_allow_html=True)

# Ambil parameter URL dinamis (?brand=NamaBrand) jika ada
query_params = st.query_params
brand_param = query_params.get("brand", "PINTAR OS Cloud Studio")
brand_name = brand_param.replace("-", " ").replace("_", " ").title()

# HTML & CSS Utuh Berdesain PINTAR OS Asli
html_code = f"""
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{brand_name}</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Plus Jakarta Sans', sans-serif;
        }}
        body {{
            background-color: #090d16;
            color: #c8cdd5;
            padding: 30px 40px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1140px;
            margin: 0 auto;
        }}
        
        /* Header */
        .header {{
            margin-bottom: 24px;
        }}
        .title {{
            font-size: 26px;
            font-weight: 800;
            color: #ffffff;
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .subtitle {{
            font-size: 13px;
            color: #7e89ac;
            margin-top: 6px;
            line-height: 1.5;
        }}
        
        /* Status Bar PINTAR OS */
        .status-panel {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #0e1630;
            border: 1px solid rgba(129, 140, 248, 0.15);
            border-radius: 12px;
            padding: 16px 24px;
            margin-bottom: 24px;
            box-shadow: 0 8px 30px rgba(0,0,0,0.4);
        }}
        .status-group {{
            display: flex;
            align-items: center;
            gap: 32px;
            flex-wrap: wrap;
        }}
        .status-item {{
            display: flex;
            flex-direction: column;
            gap: 3px;
        }}
        .status-label {{
            font-size: 10px;
            font-weight: 700;
            text-transform: uppercase;
            color: #7e89ac;
            letter-spacing: 0.8px;
        }}
        .status-val {{
            font-size: 13px;
            font-weight: 700;
            color: #c8cdd5;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .badge-live {{
            background: rgba(16, 185, 129, 0.12);
            color: #10b981;
            border: 1px solid rgba(16, 185, 129, 0.25);
            padding: 3px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
        }}
        
        /* Tab Navigation Bar */
        .tabs-nav {{
            display: flex;
            gap: 10px;
            margin-bottom: 24px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            padding-bottom: 12px;
            flex-wrap: wrap;
        }}
        .tab-btn {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            color: #7e89ac;
            padding: 10px 18px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .tab-btn:hover {{
            background: rgba(108, 114, 255, 0.1);
            color: #c8cdd5;
            border-color: rgba(108, 114, 255, 0.3);
        }}
        .tab-btn.active {{
            background: #6c72ff;
            color: #ffffff;
            border-color: #6c72ff;
            box-shadow: 0 4px 16px rgba(108, 114, 255, 0.35);
        }}
        
        /* Tab Contents */
        .tab-pane {{
            display: none;
            animation: fadeIn 0.25s ease;
        }}
        .tab-pane.active {{
            display: block;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(4px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        /* Grid Feature Cards */
        .grid-3 {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 24px;
        }}
        .card {{
            background: #0e1630;
            border: 1px solid rgba(129, 140, 248, 0.12);
            border-radius: 14px;
            padding: 24px;
            transition: all 0.2s ease;
        }}
        .card:hover {{
            border-color: rgba(129, 140, 248, 0.35);
            transform: translateY(-2px);
        }}
        .card-icon {{
            font-size: 24px;
            margin-bottom: 12px;
        }}
        .card-title {{
            font-size: 15px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 8px;
        }}
        .card-desc {{
            font-size: 13px;
            color: #7e89ac;
            line-height: 1.6;
        }}
        
        /* Legal Document Box */
        .doc-box {{
            background: #0e1630;
            border: 1px solid rgba(129, 140, 248, 0.15);
            border-radius: 14px;
            padding: 32px;
            line-height: 1.7;
        }}
        .doc-box h2 {{
            font-size: 18px;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 6px;
        }}
        .doc-meta {{
            font-size: 12px;
            color: #7e89ac;
            margin-bottom: 20px;
            padding-bottom: 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        }}
        .doc-box h3 {{
            font-size: 14px;
            font-weight: 700;
            color: #818cf8;
            margin-top: 20px;
            margin-bottom: 8px;
        }}
        .doc-box p, .doc-box li {{
            font-size: 13px;
            color: #cbd5e1;
            margin-bottom: 10px;
        }}
        .doc-box ul {{
            padding-left: 20px;
            margin-bottom: 14px;
        }}
        .doc-box a {{
            color: #818cf8;
            text-decoration: none;
            font-weight: 600;
        }}
        .doc-box a:hover {{
            text-decoration: underline;
        }}
        .callout-box {{
            background: rgba(108, 114, 255, 0.08);
            border: 1px solid rgba(108, 114, 255, 0.25);
            padding: 16px 20px;
            border-radius: 10px;
            margin-top: 18px;
            font-size: 12px;
            color: #cbd5e1;
        }}
        
        /* Footer */
        .footer {{
            margin-top: 36px;
            padding-top: 20px;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 12px;
            color: #7e89ac;
            flex-wrap: wrap;
            gap: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <div class="title">
                <span>⚡</span> {brand_name.upper()}
            </div>
            <div class="subtitle">
                Sistem otomasi manajemen konten video, integrasi cloud scheduler, dan sinkronisasi resmi Google YouTube Data API v3.
            </div>
        </div>

        <!-- Status Panel -->
        <div class="status-panel">
            <div class="status-group">
                <div class="status-item">
                    <span class="status-label">CLUSTER NODE</span>
                    <span class="status-val" style="color:#818cf8;">PINTAR-CLOUD (PRODUCTION)</span>
                </div>
                <div class="status-item">
                    <span class="status-label">OAUTH PROTOCOL</span>
                    <span class="status-val"><span class="badge-live">● AKTIF & TERENKRIPSI</span></span>
                </div>
                <div class="status-item">
                    <span class="status-label">API GATEWAY</span>
                    <span class="status-val" style="color:#10b981;">Google YouTube API v3 Certified</span>
                </div>
                <div class="status-item">
                    <span class="status-label">SYSTEM HEALTH</span>
                    <span class="status-val" style="color:#6c72ff;">99.99% Operational</span>
                </div>
            </div>
        </div>

        <!-- Tab Buttons -->
        <div class="tabs-nav">
            <button class="tab-btn active" onclick="openTab(event, 'tab-overview')">🚀 Arsitektur Sistem</button>
            <button class="tab-btn" onclick="openTab(event, 'tab-privacy')">🔒 Kebijakan Privasi (Privacy Policy)</button>
            <button class="tab-btn" onclick="openTab(event, 'tab-terms')">📄 Syarat Layanan (Terms of Service)</button>
            <button class="tab-btn" onclick="openTab(event, 'tab-compliance')">🛡️ Kepatuhan Google & YouTube</button>
        </div>

        <!-- Tab 1: Overview -->
        <div id="tab-overview" class="tab-pane active">
            <div class="grid-3">
                <div class="card">
                    <div class="card-icon">⚡</div>
                    <div class="card-title">High-Velocity Engine</div>
                    <div class="card-desc">
                        Pipeline render video otomatis terintegrasi dengan pemindaian folder multi-antrean dan sistem upload berbasis resumable chunk aman berkecepatan tinggi.
                    </div>
                </div>
                <div class="card">
                    <div class="card-icon">🔐</div>
                    <div class="card-title">Keamanan Zero-Knowledge</div>
                    <div class="card-desc">
                        Otentikasi menggunakan standar resmi Google OAuth 2.0. Sistem tidak menyimpan password akun Google Anda secara plain-text. Akses dapat dicabut kapan saja.
                    </div>
                </div>
                <div class="card">
                    <div class="card-icon">📊</div>
                    <div class="card-title">Audit & Telemetri Realtime</div>
                    <div class="card-desc">
                        Proteksi kuota API Google harian, monitoring kesehatan channel otomatis, dan pencegahan error duplikasi konten secara cerdas.
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab 2: Privacy Policy -->
        <div id="tab-privacy" class="tab-pane">
            <div class="doc-box">
                <h2>🔒 Kebijakan Privasi ({brand_name})</h2>
                <div class="doc-meta">Terakhir diperbarui: 2026 | Dokumen Kepatuhan Pengembang Resmi Google Cloud</div>

                <h3>1. Pendahuluan</h3>
                <p>
                    <strong>{brand_name}</strong> ("kami", "aplikasi") menghormati privasi pengguna dan berkomitmen melindungi seluruh data akun yang terhubung ke platform otomasi kami. Dokumen ini menjelaskan bagaimana data diakses, digunakan, dan diamankan.
                </p>

                <h3>2. Data yang Diakses & Digunakan</h3>
                <p>
                    Aplikasi kami menggunakan protokol resmi Google OAuth 2.0 untuk meminta izin akses terbatas (scope: <code>https://www.googleapis.com/auth/youtube.upload</code> dan <code>youtube.readonly</code>).
                </p>
                <ul>
                    <li><strong>Penggunaan Izin:</strong> Hanya digunakan untuk memverifikasi kepemilikan channel pengguna dan mempublikasikan video yang dijadwalkan secara sah oleh pemilik akun.</li>
                    <li><strong>Data yang TIDAK Diambil:</strong> Kami <strong>TIDAK PERNAH</strong> mengambil, menyimpan, atau memperjualbelikan password pribadi, data keuangan, atau data kontak pengguna kepada pihak ketiga mana pun.</li>
                </ul>

                <h3>3. Penyimpanan & Keamanan Data</h3>
                <p>
                    Seluruh token otentikasi disimpan dengan enkripsi standar industri (AES-256) dan hanya digunakan selama proses eksekusi tugas pengunggahan video berlangsung.
                </p>

                <h3>4. Pencabutan Izin (Revoke Access)</h3>
                <p>
                    Pengguna memiliki kendali penuh dan dapat mencabut izin akses aplikasi ini kapan saja melalui <a href="https://myaccount.google.com/permissions" target="_blank">Pengaturan Keamanan Akun Google</a>.
                </p>
            </div>
        </div>

        <!-- Tab 3: Terms of Service -->
        <div id="tab-terms" class="tab-pane">
            <div class="doc-box">
                <h2>📄 Syarat & Ketentuan Layanan</h2>
                <div class="doc-meta">Ketentuan Penggunaan Resmi Platform Otomasi</div>

                <h3>1. Persetujuan Pengguna</h3>
                <p>
                    Dengan menggunakan layanan <strong>{brand_name}</strong>, Anda menyatakan bahwa Anda adalah pemilik sah atau pihak yang memiliki wewenang penuh atas channel YouTube yang dikaitkan.
                </p>

                <h3>2. Kepatuhan Pedoman Komunitas YouTube</h3>
                <p>
                    Pengguna wajib mematuhi seluruh Pedoman Komunitas YouTube serta hukum hak cipta yang berlaku. Dilarang menggunakan sistem ini untuk mendistribusikan konten berbahaya, spam, atau materi yang melanggar hak kekayaan intelektual.
                </p>

                <h3>3. Batasan Tanggung Jawab</h3>
                <p>
                    Layanan ini disediakan atas dasar ketersediaan tinggi ("as-is"). Kami tidak bertanggung jawab atas tindakan penalti channel yang disebabkan oleh pelanggaran Pedoman Komunitas YouTube oleh pihak pengguna.
                </p>
            </div>
        </div>

        <!-- Tab 4: Compliance -->
        <div id="tab-compliance" class="tab-pane">
            <div class="doc-box">
                <h2>🛡️ Pernyataan Kepatuhan Google API & YouTube</h2>
                <div class="doc-meta">Standar Kepatuhan Google API Services User Data Policy</div>

                <p>
                    Platform <strong>{brand_name}</strong> menggunakan Layanan Resmi YouTube API Services. Dengan menggunakan aplikasi ini, pengguna juga terikat oleh:
                </p>
                <ul>
                    <li><a href="https://www.youtube.com/t/terms" target="_blank">Persyaratan Layanan YouTube (YouTube Terms of Service)</a></li>
                    <li><a href="https://policies.google.com/privacy" target="_blank">Kebijakan Privasi Google (Google Privacy Policy)</a></li>
                </ul>

                <div class="callout-box">
                    <strong style="color:#ffffff;">Pemberitahuan Persyaratan Penggunaan Terbatas (Limited Use):</strong><br>
                    Penggunaan dan transfer informasi yang diterima <strong>{brand_name}</strong> dari Google API ke aplikasi lain akan mematuhi <a href="https://developers.google.com/terms/api-services-user-data-policy" target="_blank">Kebijakan Data Pengguna Layanan Google API</a>, termasuk persyaratan Penggunaan Terbatas.
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <div>© 2026 <strong>{brand_name}</strong>. Powered by PINTAR OS Architecture.</div>
            <div>Kontak Pengembang: <span style="color:#818cf8; font-weight:700;">contact.pintarmedia@gmail.com</span></div>
        </div>
    </div>

    <!-- Script Tab Switcher Super Smooth -->
    <script>
        function openTab(evt, tabId) {{
            const panes = document.querySelectorAll('.tab-pane');
            panes.forEach(p => p.classList.remove('active'));
            
            const btns = document.querySelectorAll('.tab-btn');
            btns.forEach(b => b.classList.remove('active'));
            
            document.getElementById(tabId).classList.add('active');
            evt.currentTarget.classList.add('active');
        }}
    </script>
</body>
</html>
"""

# Render langsung tanpa bug Streamlit
components.html(html_code, height=920, scrolling=True)
