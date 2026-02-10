import streamlit as st

# version: v-bullets-fixed

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
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-box">
    <div class="header-title">👩‍💻 Poonam — FY Performance Review & Growth Journey</div>
    <div class="header-subtitle">Technical Architect | Leadership | Delivery Impact</div>
</div>
""", unsafe_allow_html=True)

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
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Role & Scope")
    st.markdown("""
    🔹 **Technical Architect – Frontend**  
    🔹 Led frontend initiatives across the delivery lifecycle  
    🔹 Provided architectural guidance and implementation support  
    🔹 Mentored teams on scalable, maintainable solutions  
    🔹 Defined and enforced frontend best practices
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 2 ----------------
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Key Achievements")
    st.markdown("""
    ✅ Supported projects: **Sightseeing, Experiences, Retail, Student Community, Cabs, GV**  
    ✅ Built a shared component library enabling cross-team reuse  
    ✅ Conducted coding best-practice and architecture sessions  
    ✅ Reviewed PRs across teams to ensure code quality  

    ✅ Core contributor to performance optimization initiatives  
    ✅ Led technical support during **Cabs go-live**  
    ✅ Sightseeing (Indigo) was the first KPMG project to go live  
    ✅ Introduced Atomic Design, TypeScript, and reusable theme wrappers  
    ✅ Guided teams on AI-assisted development (Cursor AI)
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 3 ----------------
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Metrics")
        st.markdown("🚀 **15+**  \nAvg daily bookings (Sightseeing)")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Coverage")
        st.markdown("📦 **6+**  \nProjects supported")
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 4 ----------------
with tab4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Learning & Certifications")
    st.markdown("""
    🎓 **PMP Certified**  
    📘 Learning Generative AI & Agentic AI  
    🧠 Understanding AI architectures & real-world use cases  
    ⚙️ Using AI tools to improve productivity and solution quality
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 5 ----------------
with tab5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 3-Year Vision")
    st.markdown("""
    ➤ Move into a **Delivery Lead / Delivery Manager** role  
    ➤ Use technical depth to identify risks and provide realistic estimates  
    ➤ Communicate technical challenges clearly to stakeholders  
    ➤ Participate in **AI presales** and solution shaping
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 6 ----------------
with tab6:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Why I Should Be Promoted")
    st.markdown("""
    ⭐ Operating beyond current role expectations  
    ⭐ Trusted during critical delivery phases  
    ⭐ Strong mix of technical depth and delivery mindset  
    ⭐ Created reusable assets benefiting multiple teams  
    ⭐ Preparing for leadership and AI-driven opportunities
    """)
    st.markdown('</div>', unsafe_allow_html=True)
