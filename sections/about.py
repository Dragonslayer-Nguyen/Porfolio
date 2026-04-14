import streamlit as st
from sections.resume import create_final_cv
def about():
    col1, col2 = st.columns([1.1, 2], gap="large")

    with col1:
        st.image("assets/avatar.jpg", use_container_width=True)
        st.markdown("""
            <div style="text-align: center; color: #6b7280; font-size: 0.9em; margin-top: -10px;">
                📍 Ho Chi Minh City, Vietnam<br>
                📧 220803duy@gmail.com
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.title("Nguyễn Hoàng Duy")
        st.write("#### *Architecting Automated Data Pipelines & AI-Driven Intelligence*")
        st.divider()

        # Section: Education
        st.markdown("##### 🎓 Academic Excellence")
        st.markdown("**Bachelor of IT in Artificial Intelligence** | FPT University")
        st.caption("Graduated with High Distinction • Focus on Deep Learning & Predictive Analytics")

        # THAY THẾ TECH STACK THÀNH AI BUSINESS FOCUS
        st.markdown("##### 🚀 AI Business Focus")
        st.markdown("""
        <style>
            .focus-tag {
                display: inline-block;
                background-color: #eff6ff; /* Màu xanh nhẹ doanh nghiệp */
                border-radius: 6px;
                padding: 4px 12px;
                margin: 3px;
                font-family: 'Inter', sans-serif;
                font-size: 0.85em;
                font-weight: 600;
                color: #1e40af;
                border: 1px solid #bfdbfe;
                box-shadow: 1px 1px 2px rgba(0,0,0,0.05);
            }
        </style>
        <div>
            <span class="focus-tag">Cost Efficiency via Automation</span>
            <span class="focus-tag">Competitive Market Intelligence</span>
            <span class="focus-tag">Scalable Data Pipelines</span>
            <span class="focus-tag">LLM-Powered Decision Support</span>
            <span class="focus-tag">Actionable BI Insights</span>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # Section: Core Competencies (Giữ nguyên cấu trúc đã tối ưu cho Automation)
        st.markdown("##### 🧠 Core Competencies")
        c1, c2, c3 = st.columns(3)

        with c1:
            st.info("""
            **Scraping & Automation**
            - **End-to-End Crawling:** Automated data harvesting.
            - **Market Intelligence:** Tracking trends & competitors.
            - **n8n Workflows:** Dynamic business logic.
            """)

        with c2:
            st.success("""
            **AI & LLM Solutions**
            - **Agentic Workflows:** Multi-step AI agents.
            - **RAG Architect:** Smart document processing.
            - **Precision Extraction:** Data from unstructured sources.
            """)

        with c3:
            st.warning("""
            **Business Intelligence**
            - **Data Pipelines:** Clean & ready-to-use data.
            - **Strategic Analytics:** Predictive modeling.
            - **Real-time BI:** Streamlit & Power BI dashboards.
            """)

        st.write("---")

        try:
            pdf_data = create_final_cv()

            st.download_button(
                label="📥 DOWNLOAD MY CV (Generated PDF)",
                data=pdf_data,  # Dữ liệu lấy trực tiếp từ hàm trong resume.py
                file_name="NguyenHoangDuy_CV.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        except Exception as e:
            st.error(f"Could not generate PDF: {e}")