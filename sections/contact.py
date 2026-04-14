import streamlit as st

def contact():
    # Căn giữa tiêu đề
    st.markdown("<h1 style='text-align: center;'>🤝 Get In Touch</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; color: #64748b;'>Open for professional networking and AI-driven opportunities.</p>",
        unsafe_allow_html=True)

    st.write("")
    st.write("")

    # CSS tinh chỉnh
    st.markdown("""
        <style>
        .contact-card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            padding: 25px 20px;
            border-radius: 15px;
            text-align: center;
            transition: all 0.3s ease;
            width: 100%;
            min-height: 160px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        .contact-card:hover {
            transform: translateY(-5px);
            border-color: #2563eb;
            box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.1);
        }
        .contact-icon {
            font-size: 30px;
            margin-bottom: 12px;
        }
        .contact-label {
            color: #94a3b8;
            font-size: 0.75em;
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-bottom: 8px;
        }
        .contact-link {
            color: #1e293b;
            font-weight: 700;
            text-decoration: none;
            font-size: 1rem;
            word-break: break-all;
        }
        .location-section {
            text-align: center;
            margin-top: 60px;
            padding: 20px;
            border-top: 1px solid #f1f5f9;
        }
        .location-text {
            font-size: 1.5rem;
            font-weight: 800;
            color: #1e293b;
            letter-spacing: -0.02em;
        }
        .location-subtext {
            color: #3b82f6;
            font-weight: 600;
            font-size: 1rem;
            margin-top: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Bố cục 3 cột cân đối
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
            <div class="contact-card">
                <div class="contact-icon">✉️</div>
                <div class="contact-label">Official Email</div>
                <a class="contact-link" href="mailto:220803duy@gmail.com">220803duy@gmail.com</a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="contact-card">
                <div class="contact-icon">💼</div>
                <div class="contact-label">LinkedIn</div>
                <a class="contact-link" href="https://www.linkedin.com/in/duy-nguyen-497298343/" target="_blank">DUYNGUYEN-LINKEDIN</a>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="contact-card">
                <div class="contact-icon">📞</div>
                <div class="contact-label">Phone Number</div>
                <a class="contact-link" href="tel:0923132208">0923.132.208</a>
            </div>
        """, unsafe_allow_html=True)

    # Phần Vị trí
    st.markdown("""
        <div class="location-section">
            <div style="font-size: 2rem; margin-bottom: 10px;">📍</div>
            <div class="location-text">Ho Chi Minh City, Vietnam</div>
            <div class="location-subtext">Available for Global Collaboration</div>
        </div>
    """, unsafe_allow_html=True)