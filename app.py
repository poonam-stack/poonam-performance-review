import streamlit as st

# version: v-native-stable

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Poonam | FY Performance Review",
    page_icon="🚀",
    layout="wide"
)

# ---------------- STYLES ----------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #F5F8FF;
}

.header {
    background: linear-gradient(90deg, #1D4ED8, #2563EB);
    padding: 32px;
    border-radius: 18px;
    color: white;
    margin-bottom: 30px;
}

.header h1 {
    font-size: 36px;
    font-weight: 800;
}

.header p {
    font-size: 16px;
    opacity: 0.95;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    color: #1E3A8A;
    margin-bottom: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header">
    <h1>👩‍💻 Poonam — FY Performance Review & Growth Journey</h1>
    <p>Technical Architect | Leadership | Delivery Impact</p>
</div>
""", unsafe_allow_html=True)

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧭 Role & Scope",
    "🏆 Achievements",
    "📊 Delivery Impact",
    "📚 Learning",
    "🔮 3-Year Vision",
    "⬆️ Promotion Readiness"
])

# ---------------- TAB 1 ----------------
with tab1:
    st.markdown("### 🧭 Role & Scope")
    st.markdown("""
    🔹 Technical Architect leading frontend initiatives  
    🔹 Ownership across design, development, and delivery  
    🔹 Mentoring teams on scalable and maintainable architecture  
    🔹 Driving frontend standards and best practices  
    """)

# ---------------- TAB 2 ----------------
with tab2:
    st.markdown("### 🏆 Key Achievements")
    st.markdown("""
    ✅ Supported projects: Sightseeing, Experiences, Retail, Student Community, Cabs, GV  
    ✅ Created shared component library for cross-project reuse  
    ✅ Conducted coding and architecture best-practice sessions  
    ✅ Reviewed PRs across teams to maintain quality  
    ✅ Contributor to performance optimization initiatives  
    ✅ Led technical stabilization during Cabs go-live  
    ✅ First KPMG project live: Sightseeing (Indigo)  
    ✅ Introduced Atomic Design, TypeScript, and theming wrapper  
    ✅ Guided teams on AI-assisted development (Cursor AI)  
    """)

# ---------------- TAB 3 (UNIQUE METRICS) ----------------
with tab3:
    st.markdown("### 📊 Delivery Impact")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Avg Daily Bookings", "15+")

    with col2:
        st.metric("Projects Supported", "6+")

    with col3:
        st.metric("Certifications", "PMP")

    st.info("📌 Metrics reflect direct delivery impact and cross-team contribution.")

# ---------------- TAB 4 ----------------
with tab4:
    st.markdown("### 📚 Learning & Certifications")
    st.markdown("""
    🎓 PMP Certified  
    🤖 Learning Generative AI & Agentic AI  
    🧠 Understanding AI architectures and enterprise use cases  
    ⚙️ Applying AI tools to daily work and delivery efficiency  
    """)

# ---------------- TAB 5 ----------------
with tab5:
    st.markdown("### 🔮 3-Year Vision")
    st.markdown("""
    🚀 Move into a Delivery Lead / Delivery Manager role  
    🚀 Use technical depth to manage risks and estimates  
    🚀 Communicate technical challenges to stakeholders effectively  
    🚀 Participate in AI presales and solution shaping  
    """)

# ---------------- TAB 6 ----------------
with tab6:
    st.markdown("### ⬆️ Why I Should Be Promoted")
    st.markdown("""
    ⭐ Consistently operating beyond current role expectations  
    ⭐ Trusted during critical delivery phases  
    ⭐ Strong blend of technical depth and delivery ownership  
    ⭐ Created reusable assets benefiting multiple teams  
    ⭐ Actively preparing for leadership and AI-driven initiatives  
    """)
