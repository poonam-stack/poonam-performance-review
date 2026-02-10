import streamlit as st

# version: final-promotion-ready

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
    padding: 34px;
    border-radius: 20px;
    color: white;
    margin-bottom: 32px;
}

.header h1 {
    font-size: 36px;
    font-weight: 800;
    margin-bottom: 6px;
}

.header p {
    font-size: 16px;
    opacity: 0.95;
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
    🔹 Ownership across design, development, and delivery stages  
    🔹 Supporting teams with architecture, implementation, and problem-solving  
    🔹 Mentoring developers on scalable, maintainable frontend practices  
    🔹 Driving frontend standards and best practices across projects  
    """)

# ---------------- TAB 2 ----------------
with tab2:
    st.markdown("### 🏆 Key Achievements")
    st.markdown("""
    ✅ Supported multiple projects: **Sightseeing, Experiences, Retail, Student Community, Cabs, GV**  

    ✅ Took initiative to build a **shared component library**, enabling reuse across teams  

    ✅ Conducted team sessions on **coding standards and best practices**  

    ✅ Reviewed PRs across most projects to maintain high code quality  

    ✅ Contributed to the **performance optimization team** by analyzing bottlenecks and guiding implementations  

    ✅ Provided leadership and technical direction during **Cabs go-live**, helping the team overcome critical issues  

    ✅ **Sightseeing (Indigo)** became the first project to go live from KPMG  

    ✅ Introduced **Atomic Design, TypeScript**, and a reusable **theme wrapper**, later shared with other teams  

    ✅ Guided teams in improving **AI-assisted development (Cursor AI)** through reviews and best practices  
    """)

# ---------------- TAB 3 ----------------
with tab3:
    st.markdown("### 📊 Delivery Impact")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Avg Daily Bookings", "15+", help="Sightseeing project")

    with col2:
        st.metric("Projects Supported", "6+")

    with col3:
        st.metric("Certification", "PMP")

    st.info("📌 Metrics reflect hands-on delivery impact and cross-team contribution.")

# ---------------- TAB 4 ----------------
with tab4:
    st.markdown("### 📚 Learning & Certifications")
    st.markdown("""
    🎓 **PMP Certified**  

    🤖 Actively learning **Generative AI and Agentic AI**  

    🧠 Building understanding of AI architecture, differences, and enterprise use cases  

    ⚙️ Leveraging AI tools in daily work to improve productivity, quality, and decision-making  
    """)

# ---------------- TAB 5 ----------------
with tab5:
    st.markdown("### 🔮 3-Year Vision")
    st.markdown("""
    🚀 Transition into a **Delivery Lead / Delivery Manager** role  

    🚀 Use technical depth to identify risks early and provide realistic, challenging estimates  

    🚀 Effectively communicate technical constraints and trade-offs to stakeholders  

    🚀 Actively contribute to **AI presales**, solution shaping, and showcasing AI use cases to clients  
    """)

# ---------------- TAB 6 ----------------
with tab6:
    st.markdown("### ⬆️ Why I Should Be Promoted")
    st.markdown("""
    ⭐ Consistently operating beyond current role expectations and scope  

    ⭐ Trusted during critical delivery phases and high-pressure situations  

    ⭐ **A strong multitasker who thrives in challenging and fast-paced environments while maintaining delivery quality and focus**  

    ⭐ Strong blend of technical depth, delivery ownership, and stakeholder awareness  

    ⭐ Fast learner with a strong belief in **continuous learning and self-upskilling**  

    ⭐ Actively mentoring team members on working smarter, improving productivity, and design thinking  

    ⭐ Proactively encouraging teams to **leverage AI tools** to enhance efficiency and output quality  

    ⭐ Possess sufficient experience, maturity, and judgment to be considered for the **next level role**  

    ⭐ Strong ownership mindset — I take responsibility for outcomes, not just tasks  

    ⭐ Deep belief in **governance and process discipline**  
    ⭐ Independently set up Jira boards, created tasks, and drove structured execution within the Indigo team  

    ⭐ Consistently encourage teams to follow defined processes while staying delivery-focused and agile  

    ⭐ Created reusable assets and practices that continue to benefit teams beyond my immediate scope  

    ⭐ Actively preparing myself for leadership and AI-driven delivery opportunities  
    """)
