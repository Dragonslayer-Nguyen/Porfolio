import streamlit as st


def projects():
    st.title("🚀 Strategic Projects Portfolio")
    st.markdown(
        "<p style='color: #64748b;'>Showcasing specialized expertise in Computer Vision, Quantitative Trading, and AI Automation.</p>",
        unsafe_allow_html=True)
    st.write("---")

    tab1, tab2, tab3 = st.tabs(["👁️ Computer Vision", "📈 Quant & Data", "🤖 AI Automation"])

    with tab1:
        # --- Dự án 1: Lip Reading ---
        st.subheader("🔍 Deep Lip Reading: Vietnamese Visual-to-Text Pipeline")

        col_l1, col_l2 = st.columns([1, 1.2])
        with col_l1:
            # Metric Card làm nổi bật kết quả
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 20px; border-radius: 12px; border-left: 5px solid #16a34a; margin-bottom: 20px;">
                <h4 style="margin:0; color:#166534; font-size: 0.9em; letter-spacing: 1px;">KEY ACHIEVEMENT</h4>
                <p style="color:#16a34a; font-weight:800; font-size:1.2em; margin:5px 0;">Idiomatic Accuracy</p>
                <p style="color:#64748b; font-size:0.85em;">Successful transcription of complex Vietnamese proverbs from silent video.</p>
            </div>
            """, unsafe_allow_html=True)

        with col_l2:
            st.markdown("""
            **Technical Implementation:**
            * **Architecture:** Developed an end-to-end pipeline using **Lip-Net** (Spatiotemporal CNN + Bi-GRU) to map silent video sequences directly to text.
            * **Transfer Learning:** Re-trained and fine-tuned the model on a custom-curated **Vietnamese dataset**, optimizing phoneme recognition for specific tonal nuances.
            * **Feature Extraction:** Utilized **MediaPipe** for high-precision lip-region tracking and spatiotemporal normalization at 25fps.

            **Strategic Impact:**
            * **CTC Loss Optimization:** Optimized the decoding process to achieve seamless alignment between visual sequences and text output.
            * **Accessibility:** Demonstrated the potential for visual-only speech recognition in assistive technologies and noisy environment communication.
            """)
            st.caption("Tech Stack: TensorFlow, MediaPipe, OpenCV, Spatiotemporal Modeling")

        st.divider()

        # --- Project 2: Body Measurement & Virtual Sizing ---
        st.subheader("👗 AI-Powered Virtual Tailor: Contactless Body Measurement")

        col_b1, col_b2 = st.columns([1, 1.2])
        with col_b1:
            # Metric Card nhấn mạnh Giá trị Kinh doanh (Business Value)
            st.markdown("""
                    <div style="background-color: #f5f3ff; padding: 20px; border-radius: 12px; border-left: 5px solid #8b5cf6; margin-bottom: 20px;">
                        <h4 style="margin:0; color:#4c1d95; font-size: 0.9em; letter-spacing: 1px;">BUSINESS IMPACT</h4>
                        <p style="color:#8b5cf6; font-weight:800; font-size:1.2em; margin:5px 0;">Return Rate Reduction</p>
                        <p style="color:#64748b; font-size:0.85em;">Solving the "Sizing Gap" in fashion e-commerce with precise, instant sizing.</p>
                    </div>
                    """, unsafe_allow_html=True)


        with col_b2:
            st.markdown("""
                    **Technical Deep Dive:**
                    Developed a **markerless anthropometric system** capable of extracting precise body measurements from standard 2D camera feeds in real-time.

                    * **Pose Estimation Engine:** Utilized **MediaPipe Pose** high-fidelity topology to track 33 3D landmarks, robust to occlusions and varied body postures.
                    * **Geometric Calibration Challenge:** Overcame the lack of depth sensors by engineering a **reference-based calibration algorithm**. This translates pixel distances into metric units (cm) by analyzing user height input or standard background references.
                    * **Virtual Sizing Logic:** Built an intelligent mapping layer that converts raw body metrics (shoulder width, chest circumference, torso length) into standardized apparel sizes (S/M/L/XL) tailored to specific brand size charts.
                    """)
            st.caption("Tech Stack: MediaPipe Pose, OpenCV, Computational Geometry, Python")

    with tab2:
        # --- Project 1: Quantitative Trading ---
        st.subheader("📈 Systematic Quantitative Trading: VN30F1M Alpha Generation")

        col_q1, col_q2 = st.columns([1, 1.2])
        with col_q1:
            st.markdown("""
            <div style="background-color: #f0f7ff; padding: 20px; border-radius: 12px; border-left: 5px solid #2563eb;">
                <h4 style="margin:0; color:#1e40af; font-size: 0.9em; letter-spacing: 1px;">KEY PERFORMANCE</h4>
                <h2 style="margin:0; color:#2563eb; font-size: 2.2em;">+30% ROI</h2>
                <p style="color:#64748b; font-size:0.85em; margin-top: 5px;">Out-of-Sample Backtesting Results</p>
            </div>
            """, unsafe_allow_html=True)

        with col_q2:
            st.markdown("""
            **Methodology & Implementation:**
            * **Alpha Factor Engineering:** Designed and validated predictive alpha factors based on **Market Microstructure** and **Order Flow** analysis within the Vietnam Derivatives Market (VN30F1M).
            * **Backtesting Engine:** Developed a high-fidelity vectorized backtesting framework incorporating realistic constraints such as **slippage**, transaction costs, and market liquidity.
            * **Risk Management:** Implemented advanced portfolio optimization techniques to maximize the **Sharpe Ratio** while maintaining strict drawdown controls.

            **Business Impact:**
            * Successfully built an automated trading system that consistently outperforms market benchmarks.
            * Demonstrated the viability of **Statistical Arbitrage** strategies in emerging derivatives markets.
            """)
            st.caption("Tech Stack: Python, Pandas, Quantitative Modeling, Vectorized Backtesting")

        st.divider()

        # --- Project 2: Logistics Forecasting ---
        st.subheader("📦 Predictive Logistics: Demand Forecasting & Workforce Optimization")

        col_d1, col_d2 = st.columns([1, 1.2])
        with col_d1:
            st.markdown("""
            <div style="background-color: #f0fdf4; padding: 20px; border-radius: 12px; border-left: 5px solid #16a34a;">
                <h4 style="margin:0; color:#166534; font-size: 0.9em; letter-spacing: 1px;">PRIMARY GOAL</h4>
                <p style="color:#16a34a; font-weight:800; font-size:1.2em; margin:5px 0;">Operational Excellence</p>
                <p style="color:#64748b; font-size:0.85em;">Data-Driven Resource Allocation</p>
            </div>
            """, unsafe_allow_html=True)

        with col_d2:
            st.markdown("""
            **Methodology & Implementation:**
            * **Time-Series Econometrics:** Utilized advanced forecasting models (**Prophet, XGBoost, ARIMA**) to decode complex seasonality and volatility in cargo throughput.
            * **Feature Engineering:** Integrated **exogenous variables** such as flight schedules, macroeconomic indicators, and public holidays to enhance model sensitivity.
            * **Resource Mapping:** Translated volumetric forecasts into actionable **Manpower Planning** models, optimizing staffing levels across peak and off-peak windows.

            **Business Impact:**
            * **Cost Reduction:** Significantly lowered labor overhead and overtime expenses by aligning staff supply with predicted cargo demand.
            * **SLA Compliance:** Ensured optimal resource availability during peak surges, maintaining high service-level agreements and operational throughput.
            """)
            st.caption("Tech Stack: Time-Series Analysis, Scikit-learn, SQL, Power BI")

    with tab3:
        # --- Project 1: Intelligent Voice Assistant ---
        st.subheader("🎙️ Cognitive Voice Interface & Intelligent Retrieval")

        col_v1, col_v2 = st.columns([1, 1.2])
        with col_v1:
            st.markdown("""
            <div style="background-color: #fff7ed; padding: 20px; border-radius: 12px; border-left: 5px solid #f97316;">
                <h4 style="margin:0; color:#9a3412; font-size: 0.9em; letter-spacing: 1px;">TECHNOLOGY</h4>
                <p style="color:#f97316; font-weight:800; font-size:1.2em; margin:5px 0;">GenAI Integration</p>
                <p style="color:#64748b; font-size:0.85em;">Powered by Gemini 3.0 Pro</p>
            </div>
            """, unsafe_allow_html=True)

        with col_v2:
            st.markdown("""
            **Description:** Built an end-to-end cognitive workflow that bridges the gap between vocal commands and structured information retrieval.

            **Technical Implementation:**
            * **Speech-to-Reasoning Pipeline:** Developed a system to capture user vocal input, convert it to high-fidelity text, and use **Gemini AI** for intent recognition and query synthesis.
            * **Prompt Engineering:** Optimized LLM prompts to ensure the assistant returns highly relevant, structured search results tailored to user context.

            **Outcome:**
            * Created a zero-touch interaction model for information retrieval, significantly enhancing user accessibility and search efficiency.
            """)
            st.caption("Tech Stack: Gemini API, Python, NLP, Speech Recognition, Streamlit")

        st.divider()

        # --- Project 2: Logistics Automation (AWB) ---
        st.subheader("📄 Intelligent Document Processing (IDP): Automated Logistics Pipeline")

        col_a1, col_a2 = st.columns([1, 1.2])
        with col_a1:
            st.markdown("""
            <div style="background-color: #f5f3ff; padding: 20px; border-radius: 12px; border-left: 5px solid #8b5cf6;">
                <h4 style="margin:0; color:#4c1d95; font-size: 0.9em; letter-spacing: 1px;">IMPACT</h4>
                <p style="color:#8b5cf6; font-weight:800; font-size:1.2em; margin:5px 0;">Zero-Error Automation</p>
                <p style="color:#64748b; font-size:0.85em;">Automated Data Entry</p>
            </div>
            """, unsafe_allow_html=True)

        with col_a2:
            st.markdown("""
            **Description:** Engineered a high-efficiency automation pipeline to digitize and process **Airwaybills (AWB)** for global logistics operations.

            **Technical Implementation:**
            * **OCR Data Extraction:** Leveraged advanced OCR techniques combined with Gemini's vision capabilities to parse complex document layouts.
            * **Automated Data Mapping:** Built logic to automatically identify and extract critical metadata, including **Consignee details, Cargo Weight, and Port of Origin**.
            * **System Integration:** Developed a seamless workflow to push extracted data directly into corporate databases, bypassing manual entry.

            **Outcome:**
            * **Efficiency:** Achieved a 100% reduction in manual data entry time.
            * **Data Integrity:** Eliminated human transcription errors, ensuring high-fidelity data across the logistics supply chain.
            """)
            st.caption("Tech Stack: Gemini Vision API, OCR, Python Automation, Logistics Workflow")