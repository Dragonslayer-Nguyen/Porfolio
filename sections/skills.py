import streamlit as st

def skills():
    st.title("⚒️ Technical Expertise")
    st.markdown("<p style='color: #64748b;'>A comprehensive overview of my technical proficiency and specialized toolkits.</p>", unsafe_allow_html=True)
    st.write("---")

    # CSS tinh chỉnh cho hệ thống Skill Tags
    st.markdown("""
        <style>
        .skill-category-card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        .skill-category-card:hover {
            border-color: #3b82f6;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }
        .category-title {
            color: #1e293b;
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .skill-tag {
            display: inline-block;
            background-color: #f1f5f9;
            color: #475569;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            margin: 4px;
            border: 1px solid #e2e8f0;
        }
        .skill-tag:hover {
            background-color: #3b82f6;
            color: #ffffff;
            border-color: #3b82f6;
        }
        </style>
    """, unsafe_allow_html=True)

    # Chia cột để tối ưu không gian
    col1, col2 = st.columns(2, gap="large")

    with col1:
        # Nhóm 1: Core Programming
        st.markdown("""
            <div class="skill-category-card">
                <div class="category-title">💻 Programming Languages</div>
                <span class="skill-tag">Python (Expert)</span>
                <span class="skill-tag">C++</span>
                <span class="skill-tag">SQL (PostgreSQL)</span>
            </div>
        """, unsafe_allow_html=True)

        # Nhóm 2: AI & Computer Vision
        st.markdown("""
            <div class="skill-category-card">
                <div class="category-title">🤖 AI & Deep Learning</div>
                <span class="skill-tag">TensorFlow</span>
                <span class="skill-tag">PyTorch</span>
                <span class="skill-tag">OpenCV</span>
                <span class="skill-tag">MediaPipe</span>
                <span class="skill-tag">YOLO v8/v10</span>
                <span class="skill-tag">Gemini API</span>
                <span class="skill-tag">LangChain</span>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        # Nhóm 3: Data Engineering & BI
        st.markdown("""
            <div class="skill-category-card">
                <div class="category-title">📊 Data & Business Intelligence</div>
                <span class="skill-tag">Power BI (DAX)</span>
                <span class="skill-tag">Power Query</span>
                <span class="skill-tag">Pandas/NumPy</span>
                <span class="skill-tag">Matplotlib/Seaborn</span>
                <span class="skill-tag">ETL Processes</span>
            </div>
        """, unsafe_allow_html=True)

        # Nhóm 4: DevOps & Deployment
        st.markdown("""
            <div class="skill-category-card">
                <div class="category-title">🚀 Deployment & Tools</div>
                <span class="skill-tag">Streamlit</span>
                <span class="skill-tag">Azure Cloud</span>
                <span class="skill-tag">Git/GitHub</span>
                <span class="skill-tag">Docker (Basic)</span>
                <span class="skill-tag">Automation Systems</span>
            </div>
        """, unsafe_allow_html=True)

    # Phần ghi chú thêm về ngôn ngữ (tùy chọn)
    st.write("")
    # Thêm phần này vào cuối hàm skills() trong file skills.py

    st.write("---")
    st.markdown("##### 🌐 Language Proficiency")

    # Sử dụng cột để phân bổ ngôn ngữ chuyên nghiệp
    lang_col1, lang_col2 = st.columns(2)

    with lang_col1:
        st.markdown("""
                <div style="background-color: #f8fafc; padding: 15px; border-radius: 10px; border-left: 5px solid #3b82f6;">
                    <span style="font-weight: 700; color: #1e293b;">Vietnamese</span>
                    <span style="color: #64748b; font-size: 0.85rem; margin-left: 10px;">Native Speaker</span>
                    <div style="background-color: #e2e8f0; height: 6px; border-radius: 3px; margin-top: 10px;">
                        <div style="background-color: #3b82f6; width: 100%; height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    with lang_col2:
        st.markdown("""
                <div style="background-color: #f8fafc; padding: 15px; border-radius: 10px; border-left: 5px solid #10b981;">
                    <span style="font-weight: 700; color: #1e293b;">English</span>
                    <span style="color: #64748b; font-size: 0.85rem; margin-left: 10px;">Professional Working Proficiency</span>
                    <div style="background-color: #e2e8f0; height: 6px; border-radius: 3px; margin-top: 10px;">
                        <div style="background-color: #10b981; width: 85%; height: 6px; border-radius: 3px;"></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)