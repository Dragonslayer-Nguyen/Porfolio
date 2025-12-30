import streamlit as st


def about():
    col1, col2 = st.columns([1.1, 2], gap="large")

    with col1:
        st.image("assets/avatar.jpg", use_container_width=True)
        # Location & Contact tinh tế
        st.markdown("""
            <div style="text-align: center; color: #6b7280; font-size: 0.9em; margin-top: -10px;">
                📍 Ho Chi Minh City, Vietnam<br>
                📧 220803duy@gmail.com
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.title("Nguyễn Hoàng Duy")
        st.write("#### *Bridging the gap between AI Research and Business Intelligence*")
        st.divider()

        # Section: Education
        st.markdown("##### 🎓 Academic Excellence")
        st.markdown("**Bachelor of IT in Artificial Intelligence** | FPT University")
        st.caption("Graduated with High Distinction • Focus on Deep Learning & Predictive Analytics")

        # Section: Technical Stack
        st.markdown("##### 🛠 Technical Stack")
        st.markdown("""
        <style>
            .stack-tag {
                display: inline-block;
                background-color: #f8fafc;
                border-radius: 6px;
                padding: 4px 12px;
                margin: 3px;
                font-family: 'Source Code Pro', monospace;
                font-size: 0.85em;
                font-weight: 600;
                color: #1e293b;
                border: 1px solid #e2e8f0;
                box-shadow: 1px 1px 2px rgba(0,0,0,0.05);
            }
        </style>
        <div>
            <span class="stack-tag">Python (Expert)</span> <span class="stack-tag">Gemini API</span>
            <span class="stack-tag">LangChain</span> <span class="stack-tag">TensorFlow</span>
            <span class="stack-tag">PyTorch</span> <span class="stack-tag">SQL</span>
            <span class="stack-tag">Streamlit</span> <span class="stack-tag">Power BI</span>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # Section: Core Competencies (Tái cấu trúc để Pro hơn)
        st.markdown("##### 🧠 Core Competencies")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.info("""
            **AI & Computer Vision**
            - **Object Detection:** YOLOv8+
            - **Biometrics:** Lip-Net, Mediapipe
            - **Processing:** OpenCV Advanced
            """)

        with c2:
            st.success("""
            **Data Engineering**
            - **Analysis:** Statistical Modeling
            - **Finance:** Predictive Valuation
            - **BI:** Power Query & DAX
            """)

        with c3:
            st.warning("""
            **Agents & Automation**
            - **Virtual Assistant:** Gemini API
            - **RAG System:** PDF Data Extraction
            - **Workflow:** Automated Profiling
            """)

        st.write("---")

        # Download Button
        with open("assets/CV.pdf", "rb") as pdf_file:
            st.download_button(
                label="📥 DOWNLOAD MY CV",
                data=pdf_file,
                file_name="NguyenHoangDuy_CV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )