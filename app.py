import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Heena | FY Performance Review",
    layout="wide"
)

# ================= CUSTOM CSS =================
st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(to right, #f8f9fc, #eef2f7);
}

/* Animations */
@keyframes fadeSlide {
    0% {opacity: 0; transform: translateY(-20px);}
    100% {opacity: 1; transform: translateY(0);}
}

/* Title */
.main-title {
    font-size: 48px;
    font-weight: 800;
    background: linear-gradient(90deg, #4f46e5, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeSlide 1.2s ease-in-out;
}

/* Subtitle */
.sub-title {
    font-size: 20px;
    color: #475569;
    margin-bottom: 30px;
    animation: fadeSlide 1.6s ease-in-out;
}

/* Card */
.card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
    animation: fadeSlide 0.8s ease-in-out;
}

/* Section title */
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 15px;
    color: #1e293b;
}

/* Metric card */
.metric-card {
    background: linear-gradient(135deg, #6366f1, #22d3ee);
    color: white;
    padding: 22px;
    border-radius: 16px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown('<div class="main-title">Heena – FY Performance Review</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Technical Architect | Leadership | Delivery Impact</div>', unsafe_allow_html=True)

# ================= TABS =================
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "🧭 Role & Scope",
        "🚀 Achievements",
        "📈 Impact",
        "🎓 Learning",
        "🔮 3-Year Vision",
        "⬆️ Promotion Readiness"
    ]
)

# ================= TAB 1 =================
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Role & Scope</div>', unsafe_allow_html=True)
    st.write("""
    **Technical Architect – Frontend**

    - Led and supported multiple frontend projects end-to-end  
    - Provided technical guidance across all stages of delivery  
    - Mentored teams to ensure scalability, performance, and code quality  
    - Defined and enforced architectural standards and best practices across teams
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 2 =================
with tab2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Key Achievements</div>', unsafe_allow_html=True)
    st.write("""
    - Supported and contributed to multiple projects:
      **Sightseeing, Experience, Retails, Student Community, Cabs, GV**
    - Designed and built a **common component library** to enable reuse across projects
    - Conducted sessions on **best coding practices** and architecture
    - Regularly reviewed PRs across most projects to ensure quality
    - Core member of the **Performance Team**:
        - Analysed performance bottlenecks  
        - Defined optimization approaches  
        - Guided teams through implementation
    - Demonstrated delivery leadership during critical phases:
        - Supported **Cabs** during go-live issue resolution  
        - Helped stabilize **Expedia release process**
    - First KPMG project to go live: **Sightseeing with Indigo**
    - Introduced strong architectural foundations:
        - Atomic Design pattern  
        - TypeScript standardization  
        - Theme wrapper supporting multiple themes (reused across projects)
    - Reviewed and improved **Cursor AI–generated code**, guiding teams on better patterns
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 3 =================
with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.write("📊 Avg Daily Bookings")
        st.write("15+")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Business Impact</div>', unsafe_allow_html=True)
        st.write("""
        - Stable production performance post go-live  
        - Smooth release execution and reduced delivery risk  
        - Strong architectural foundation for future scaling
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 4 =================
with tab4:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Learning & Certifications</div>', unsafe_allow_html=True)
    st.write("""
    ✅ **PMP Certification – Cleared**

    **AI Upskilling**
    - Agentic AI vs Generative AI  
    - AI architecture patterns  
    - Practical AI use cases

    **Hands-on Application**
    - Leveraging AI tools to improve daily productivity  
    - Enhancing solution design and technical decision-making
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 5 =================
with tab5:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">3-Year Vision</div>', unsafe_allow_html=True)
    st.write("""
    - Grow into a **Delivery Lead / Delivery Manager**
    - Use technical depth to:
        - Identify risks early  
        - Provide realistic and challenging estimates  
        - Communicate technical issues effectively to stakeholders
    - Actively contribute to **AI pre-sales**
    - Showcase AI-driven architectures and use cases to potential clients
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ================= TAB 6 =================
with tab6:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Why I Am Ready for Promotion</div>', unsafe_allow_html=True)
    st.write("""
    **Operating Beyond Role Expectations**

    - Consistently supported multiple projects and teams beyond my assigned scope  
    - Took ownership during critical delivery phases to reduce risk and ensure stability  
    - Proactively identified and addressed architectural and performance gaps at an organizational level  

    **Leadership & Delivery Impact**

    - Trusted to step in during high-pressure situations such as **Cabs go-live** and **Expedia release process**  
    - Acted as a technical anchor during delivery uncertainty  
    - Balanced delivery timelines with long-term architectural quality  

    **Scaling Impact Across Teams**

    - Built shared component libraries and theme wrappers used across multiple projects  
    - Established best practices including **Atomic Design, TypeScript, and performance standards**  
    - Enabled faster development, reduced rework, and consistent quality  

    **Strong Foundation for Delivery Leadership**

    - PMP certified with strong grounding in delivery, planning, and risk management  
    - Able to translate technical complexity into clear and actionable communication for stakeholders  

    **Future-Ready & Business Aligned**

    - Actively building expertise in **Agentic and Generative AI**  
    - Exploring AI-led use cases for pre-sales and client engagement  

    **Summary**

    I am already operating as a technical leader with delivery ownership and organizational impact, and I am ready to take on a formal role that reflects this responsibility and value.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
