import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Poonam | FY Performance Review",
    page_icon="👩‍💻",
    layout="wide"
)

# ---------------- STYLES ----------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

@keyframes slideFade {
    from { opacity: 0; transform: translateY(-12px); }
    to { opacity: 1; transform: translateY(0); }
}

.animated-title {
    font-size: 36px;
    font-weight: 800;
    animation: slideFade 1.2s ease;
}

.subtitle {
    font-size: 16px;
    color: #555;
    margin-bottom: 30px;
}

.card {
    background: #ffffff;
    padding: 24px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 24px;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin-bottom: 14px;
}

.metric {
    font-size: 34px;
    font-weight: 700;
    color: #2563eb;
}

.metric-label {
    font-size: 14px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="animated-title">
🚀 Poonam — FY Performance Review & Growth Journey
</div>
<div class="subtitle">
Technical Architect | Leadership | Delivery Impact
</div>
""", unsafe_allow_html=True)

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧭 Role & Scope",
    "🏆 Key Achievements",
    "📊 Metrics",
    "📚 Learning & Certifications",
    "🔮 3-Year Vision",
    "⬆️ Why I Should Be Promoted"
])

# ---------------- TAB 1 ----------------
with tab1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Role & Scope")
        st.markdown("""
        **Technical Architect – Frontend**

        - Led and supported frontend initiatives across the delivery lifecycle  
        - Provided architectural guidance, reviews, and implementation support  
        - Mentored teams to ensure scalable and maintainable solutions  
        - Defined and enforced frontend standards and best practices
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 2 ----------------
with tab2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Key Achievements")
        st.markdown("""
        - Supported projects: **Sightseeing, Experiences, Retail, Student Community, Cabs, GV**
        - Built a **shared component library** for cross-team reuse
        - Conducted sessions on coding standards and architecture
        - Reviewed PRs across teams to maintain code quality
        - Core contributor to performance optimization initiatives
        - Led technical support during **Cabs go-live**
        - Sightseeing (Indigo) became the **first KPMG project to go live**
        - Introduced Atomic Design, TypeScript, and reusable theme wrapper
        - Guided teams on AI-assisted development (Cursor AI)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 3 ----------------
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### Metrics")
            st.markdown("**15+**  \nAvg Daily Bookings (Sightseeing)")
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown("### Coverage")
            st.markdown("**6+**  \nProjects Supported")
            st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 4 ----------------
with tab4:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Learning & Certifications")
        st.markdown("""
        - **PMP Certified**
        - Learning Generative AI & Agentic AI concepts
        - Understanding AI architectures and use cases
        - Applying AI tools to improve productivity and solution quality
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 5 ----------------
with tab5:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 3-Year Vision")
        st.markdown("""
        - Transition into a **Delivery Lead / Delivery Manager** role
        - Use technical depth to identify risks and give realistic estimates
        - Communicate technical challenges effectively to stakeholders
        - Actively participate in **AI presales** and solution shaping
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 6 ----------------
with tab6:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Why I Should Be Promoted")
        st.markdown("""
        - Operating beyond current role expectations
        - Trusted during critical delivery phases
        - Strong mix of technical depth and delivery mindset
        - Created reusable assets benefiting multiple teams
        - Preparing for leadership and AI-driven opportunities
        """)
        st.markdown('</div>', unsafe_allow_html=True)
