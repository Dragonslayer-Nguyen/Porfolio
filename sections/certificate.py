import streamlit as st
import base64


def show_pdf(file_path):
    """Hiển thị PDF Full width, tự động co giãn và nét"""
    try:
        with open(file_path, "rb") as f:
            pdf_data = f.read()
            pdf64 = base64.b64encode(pdf_data).decode("utf-8")

        pdf_viewer_html = f"""
        <div id="pdf-viewer-container" style="width:100%; height:850px; overflow-y: auto; background-color: #525659; border-radius: 12px; padding: 10px 0;">
            <div id="canvas-wrapper" style="display: flex; flex-direction: column; align-items: center; gap: 15px; width: 100%;"></div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.9.179/pdf.min.js"></script>
        <script>
            const pdfData = atob("{pdf64}");
            const pdfjsLib = window['pdfjs-dist/build/pdf'];
            pdfjsLib.GlobalWorkerOptions.workerSrc = 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.9.179/pdf.worker.min.js';

            const loadingTask = pdfjsLib.getDocument({{data: pdfData}});
            loadingTask.promise.then(function(pdf) {{
                const wrapper = document.getElementById('canvas-wrapper');
                const container = document.getElementById('pdf-viewer-container');

                for(let pageNum = 1; pageNum <= pdf.numPages; pageNum++) {{
                    pdf.getPage(pageNum).then(function(page) {{
                        // Lấy chiều rộng container để tính toán scale tự động
                        const containerWidth = container.clientWidth - 40; // trừ padding
                        const unscaledViewport = page.getViewport({{scale: 1}});
                        const scale = containerWidth / unscaledViewport.width;

                        const viewport = page.getViewport({{scale: scale}});
                        const canvas = document.createElement('canvas');

                        // Style cho canvas để trông giống tờ giấy
                        canvas.style.boxShadow = "0 8px 24px rgba(0,0,0,0.4)";
                        canvas.style.backgroundColor = "white";
                        canvas.style.maxWidth = "95%"; 
                        canvas.style.height = "auto";

                        const context = canvas.getContext('2d');
                        canvas.height = viewport.height;
                        canvas.width = viewport.width;
                        wrapper.appendChild(canvas);

                        page.render({{
                            canvasContext: context,
                            viewport: viewport
                        }});
                    }});
                }}
            }});
        </script>
        <style>
            #pdf-viewer-container::-webkit-scrollbar {{ width: 10px; }}
            #pdf-viewer-container::-webkit-scrollbar-track {{ background: #333; }}
            #pdf-viewer-container::-webkit-scrollbar-thumb {{ background: #888; border-radius: 5px; border: 2px solid #333; }}
        </style>
        """
        # Tăng height lên 900 để chứa được toàn bộ container và lề
        st.components.v1.html(pdf_viewer_html, height=880)

    except FileNotFoundError:
        st.error(f"⚠️ Không tìm thấy file tại: {file_path}")


def certificate():
    # --- CSS TUỲ CHỈNH ---
    st.markdown("""
        <style>
        .main-title { font-size: 40px; font-weight: bold; color: #1E3A8A; margin-bottom: 10px; }
        .sub-title { font-size: 18px; color: #6B7280; margin-bottom: 30px; }
        .cert-card { padding: 20px; border-radius: 10px; background-color: #f8fafc; border-left: 5px solid #1E3A8A; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="main-title">🎓 Credentials & Recognitions</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">A comprehensive record of my academic journey and professional milestones.</p>',
                unsafe_allow_html=True)

    # --- PHẦN METRICS (Tạo điểm nhấn ngay từ đầu) ---
    col_m1, col_m2, col_m3 = st.columns(3)
    col_m1.metric("Formal Education", "Bachelor's", "AI Specialization")
    col_m2.metric("Certifications", "12+", "Professional")
    col_m3.metric("Key Awards", "08", "Top Honors")
    st.write("---")

    tab1, tab2, tab3 = st.tabs([
        "📜 Academic Degrees",
        "🛠️ Professional Specializations",
        "🏆 Technical Honors"
    ])

    # --- TAB 1: ACADEMIC DEGREES ---
    with tab1:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.markdown("""
                <div class="cert-card">
                    <h4>Bachelor of Science</h4>
                    <p><b>Major:</b> Artificial Intelligence</p>
                    <p><b>Institution:</b> FPT University</p>
                    <p><b>Period:</b> 2018 - 2022</p>
                </div>
            """, unsafe_allow_html=True)
        with c2:
            show_pdf("assets/FPT_University_Degree.pdf")

    # --- TAB 2: PROFESSIONAL CERTIFICATIONS ---
    with tab2:
        st.subheader("Industry-Standard Certifications")
        # Chia cột để chọn loại chứng chỉ
        cat_col, view_col = st.columns([1, 2])

        cert_groups = {
            "🤖 AI & Machine Learning": ["assets//cousera//Deep_Learning.pdf", "assets//cousera//Natural_Language_Processing.pdf",
                                        "assets//cousera//IBM_Introduction_To_Machine_Learning.pdf", "assets//cousera//IBM_Applied_AI.pdf",
                                        "assets//cousera//IBM_AI_Developer.pdf"],
            "📊 Data Science & Big Data": ["assets//cousera//IBM_Data_Science.pdf", "assets//cousera//Applied_Data_Science.pdf",
                                          "assets//cousera//Big_Data.pdf"],
            "💻 Software Development": ["assets//cousera//IBM_Full_Stack_Software_Developer.pdf",
                                       "assets//cousera//Software_Development_Lifecycle.pdf"],
            "📚 Academic & Management": ["assets//cousera//Academic_English_Writing.pdf",
                                        "assets//cousera//Project_Management_Principles_and_Practices.pdf"]
        }

        with cat_col:
            category = st.radio("Choose Category", list(cert_groups.keys()))
            files = cert_groups[category]
            display_names = {f: f.replace("assets/cousera/", "").replace(".pdf", "").replace("_", " ") for f in files}
            selected_path = st.selectbox("Select Certificate", options=files, format_func=lambda x: display_names[x])

        with view_col:
            show_pdf(selected_path)

    # --- TAB 3: AWARDS & ACHIEVEMENTS ---
    with tab3:
        # Danh sách giải thưởng dựa trên dữ liệu thật của bạn
        awards_data = [
            {"title": "First Prize - 'Apps4Vsmart' Competition", "org": "VinUniversity",
             "file": "assets/award/Vin UIN-2020-Giai nhat.pdf", "year": "2020"},

            {"title": "First Prize - Robocon South Vietnam", "org": "Robocon South of Vietnam",
             "file": "assets/award/Giai Nhat-ROBOTOCONS-2020.pdf", "year": "2020-2021"},

            {"title": "City Merit - Excellent Student", "org": "HCMC Dept. of Education",
             "file": "assets/award/Giay chung nhan Hoc sinh Gioi Giai Cap Thanh Pho.pdf", "year": "2020-2021"},

            {"title": "Second Prize - City Science & Tech", "org": "HCMC Dept. of Education",
             "file": "assets/award/11CL-NCKH-Giai nhì- TPHCM.pdf", "year": "2020"},

            {"title": "First Prize - Scientific Research 2020-2021", "org": "School Level",
             "file": "assets/award/12CL-NCKH2020-Giai nhat-Truong.pdf", "year": "2020-2021"},

            {"title": "First Prize - Scientific Research 2019-2020", "org": "School Level",
             "file": "assets/award/11CL-NCKH2019-Giai nhat-Truong.pdf", "year": "2019-2020"},

            {"title": "April Olympic Competition Participant", "org": "South of Vietnam",
             "file": "assets/award/Olimpic thang 4-2018.pdf", "year": "2018-2019"},

            {"title": "FPT Research Festival Participant", "org": "FPT University",
             "file": "assets/award/FPT_RESFES.pdf", "year": "2022"},
        ]

        st.info("💡 Select an achievement from the sidebar or the dropdown to view proof.")

        # Sử dụng selectbox với mô tả chi tiết
        selected_award_title = st.selectbox(
            "View Achievement Evidence:",
            options=[a["title"] for a in awards_data]
        )

        selected_award = next(a for a in awards_data if a["title"] == selected_award_title)

        # Hiển thị thông tin tóm tắt bằng card trước khi hiện PDF
        st.markdown(f"""
            <div style="background-color: #e0f2fe; padding: 15px; border-radius: 10px; margin-bottom: 20px;">
                <h3 style="margin:0; color:#0369a1;">{selected_award['title']}</h3>
                <p style="margin:0;"><b>Organized by:</b> {selected_award['org']} | <b>Year:</b> {selected_award['year']}</p>
            </div>
        """, unsafe_allow_html=True)

        show_pdf(selected_award['file'])