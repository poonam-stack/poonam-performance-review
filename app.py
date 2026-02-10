import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Poonam | FY Performance Review",
    page_icon="🚀",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap" rel="stylesheet">

<style>
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.section-title {
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 15px;
    animation: fadeInUp 1s ease;
}

.card {
    background: #ffffff;
    padding: 25px;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.metric {
    font-size: 34px;
    font-weight: 700;
    color: #2E86C1;
}

.metric-label {
    font-size: 14px;
    color: #555;
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(12px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.stTabs [role="tab"] {
    font-size: 15px;
    font-weight: 600;
    padding: 10px 18px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="section-title">
🚀 Poonam — FY Performance Review & Growth Journey
</div>
""", unsafe_allow_html=True)

st.markdown(
    "A concise, impact-focused overview of my contributions, growth, and future readiness."
)

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🧭 Role & Scope",
    "🏆 Key Achievements",
    "📊 Metrics",
    "📚 Learning & Certifications",
    "🌱 Improvements",
    "🚀 Promotion Readiness"
])

# ---------------- TAB 1 ----------------
with tab1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Role & Scope</div>

        <b>Technical Architect – Frontend</b><br><br>

        • Led and supported multiple frontend initiatives across delivery lifecycle<br>
        • Provided architectural guidance, design reviews, and implementation support<br>
        • Acted as a technical mentor for teams during development and release phases<br>
        • Ensured alignment to scalability, performance, and maintainability standards
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 2 ----------------
with tab2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Key Achievements</div>

        • Contributed across multiple projects: <b>Sightseeing, Experiences, Retail, Student Community, Cabs, GV</b><br><br>

        • Took initiative to design and build a <b>common component library</b>, enabling faster development and consistency across projects<br><br>

        • Established and conducted sessions on <b>best coding practices</b> and frontend standards<br><br>

        • Actively reviewed PRs across most projects, ensuring high code quality and maintainability<br><br>

        • Core member of the <b>performance optimization initiative</b>, contributing to analysis, improvement strategies, and guiding teams on implementation<br><br>

        • Played a key leadership role during <b>Cabs go-live</b>, helping resolve critical issues and stabilizing delivery under pressure<br><br>

        • Sightseeing (Indigo partnership) was the <b>first project to go live from KPMG</b>, setting the foundation for future deliveries<br><br>

        • Defined architectural best practices such as <b>Atomic Design</b> and <b>TypeScript adoption</b> in new projects like GV<br><br>

        • Designed a <b>theme wrapper</b> to support multiple branding needs, later shared and reused across teams<br><br>

        • Reviewed and guided teams on <b>AI-assisted development (Cursor AI)</b>, improving code quality and efficiency
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 3 ----------------
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="metric">15+</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Average Daily Bookings (Sightseeing)</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown('<div class="metric">6+</div>', unsafe_allow_html=True)
            st.markdown('<div class="metric-label">Projects Supported</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 4 ----------------
with tab4:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Learning & Certifications</div>

        • <b>PMP Certification</b> – Strengthened delivery, risk management, and stakeholder communication skills<br><br>

        • Actively building expertise in <b>AI and modern architectures</b>, including:
          – Generative AI vs Agentic AI<br>
          – AI system architecture and real-world use cases<br><br>

        • Leveraging multiple AI tools in daily work to improve productivity, learning, and solution quality
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 5 ----------------
with tab5:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Improvements & Growth</div>

        • Transitioned from individual contributor mindset to <b>team and delivery ownership</b><br><br>

        • Improved ability to guide teams during ambiguity and high-pressure delivery phases<br><br>

        • Strengthened cross-team collaboration and architectural decision-making<br><br>

        • Proactively introduced structure, standards, and reusable assets to improve long-term efficiency
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TAB 6 ----------------
with tab6:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-title">Why I Am Ready for Promotion</div>

        <b>Leadership & Delivery Ownership</b><br>
        • Trusted to step in during critical delivery phases such as <b>Cabs go-live</b><br>
        • Acted as a technical anchor ensuring stability and clarity under pressure<br><br>

        <b>Technical Depth with Business Mindset</b><br>
        • Strong frontend architectural expertise combined with delivery awareness<br>
        • Ability to assess risks, provide realistic estimates, and communicate trade-offs clearly<br><br>

        <b>Organizational Impact</b><br>
        • Created reusable libraries, standards, and frameworks benefiting multiple teams<br>
        • Elevated overall engineering quality beyond individual projects<br><br>

        <b>Future Readiness</b><br>
        • Actively preparing for <b>Delivery Lead / Delivery Manager</b> responsibilities<br>
        • Keen to contribute to <b>AI-focused presales</b>, showcasing practical AI use cases to clients
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
