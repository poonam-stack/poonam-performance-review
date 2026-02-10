import streamlit as st

# version: v-blue-professional

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Poonam | FY Performance Review",
    page_icon="🚀",
    layout="wide"
)

# ---------------- GLOBAL STYLES ----------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #F8FAFF;
    color: #0F172A;
}

@keyframes fadeDown {
    from { opacity:0; transform:translateY(-14px); }
    to { opacity:1; transform:translateY(0); }
}

.header-box {
    background: linear-gradient(90deg, #2563EB, #1E40AF);
    padding: 28px 30px;
    border-radius: 18px;
    margin-bottom: 35px;
    color: white;
    animation: fadeDown 1.2s ease;
}

.header-title {
    font-size: 34px;
    font-weight: 800;
}

.header-subtitle {
    font-size: 16px;
    opacity: 0.95;
    margin-top: 6px;
}

.card {
    background: white;
    padding: 26px;
    border-radius: 16px;
    box-shadow: 0 8px 22px rgba(30,64,175,0.12);
    margin-bottom: 26px;
}

.card h3 {
    color: #1E40AF;
    font-weight: 700;
    margin-bottom: 14px;
}

.metric {
    font-size: 36px;
    font-weight: 800;
    color: #2563EB;
}

.metric-label {
    font-size: 14px;
    color: #475569;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-box">
    <div class="header-title">👩‍💻 Poonam — FY Performance Review & Growth Journey</div>
    <div class="header-subtitle">Technical Architect | Leadership | Delivery Impact</div>
</div>
""", unsafe_allow_html=True)

# ---------------- HELPER: CARD ----------------
def card(content):
    st.markdown(
        f"""
        <div class="card">
            {content}
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧭 Role & Scope",
    "🏆 Key Achievements",
    "📊 Metrics",
    "📚 Learning",
    "🔮 3-Year Vision",
    "⬆️ Promotion Readiness"
])

# ---------------- TAB 1 ----------------
with tab1:
    card("""
    <h3>Role & Scope</h3>
    ▸ <b>Technical Architect – Frontend</b><br><br>
    ▸ Led frontend initiatives across the delivery lifecycle<br>
    ▸ Provided architectural guidance and implementation support<br>
    ▸ Mentored teams on scalable, maintainable solutions<br>
    ▸ Defined and enforced frontend best practices
    """)

# ---------------- TAB 2 ----------------
with tab2:
    card("""
    <h3>Key Achievements</h3>
    ✔ Supported projects: <b>Sightseeing, Experiences, Retail, Student Community, Cabs, GV</b><br><br>
    ✔ Built a shared component library enabling cross-team reuse<br>
    ✔ Conducted coding best-practice and architecture sessions<br>
    ✔ Reviewed PRs across teams to ensure code quality<br><br>
    ✔ Core contributor to performance optimization initiatives<br>
    ✔ Led technical support during <b>Cabs go-live</b><br>
    ✔ Sightseeing (Indigo) became the first KPMG project to go live<br>
    ✔ Introduced Atomic Design, TypeScript, and reusable theme wrappers<br>
    ✔ Guided teams on AI-assisted development (Cursor AI)
    """)

# ---------------- TAB 3 ----------------
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        card("""
        <div class="metric">15+</div>
        <div class="metric-label">Avg Daily Bookings (Sightseeing)</div>
        """)

    with col2:
        card("""
        <div class="metric">6+</div>
        <div class="metric-label">Projects Supported</div>
        """)

# ---------------- TAB 4 ----------------
with tab4:
    card("""
    <h3>Learning & Certifications</h3>
    ▸ <b>PMP Certified</b><br><br>
    ▸ Actively learning Generative AI & Agentic AI<br>
    ▸ Understanding AI architectures and real-world use cases<br>
    ▸ Leveraging AI tools to improve productivity and solution quality
    """)

# ---------------- TAB 5 ----------------
with tab5:
    card("""
    <h3>3-Year Vision</h3>
    ➤ Transition into a <b>Delivery Lead / Delivery Manager</b> role<br><br>
    ➤ Leverage technical depth to identify risks and provide realistic estimates<br>
    ➤ Communicate technical challenges effectively to stakeholders<br>
    ➤ Actively contribute to <b>AI presales</b> and solution shaping
    """)

# ---------------- TAB 6 ----------------
with tab6:
    card("""
    <h3>Why I Should Be Promoted</h3>
    ▸ Already operating beyond current role expectations<br>
    ▸ Trusted during critical delivery phases<br>
    ▸ Strong mix of technical depth and delivery mindset<br>
    ▸ Created reusable assets benefiting multiple teams<br>
    ▸ Preparing for leadership and AI-driven opportunities
    """)
