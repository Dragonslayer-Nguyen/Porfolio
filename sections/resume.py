from fpdf import FPDF, XPos, YPos


class ExecutiveTechCV(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        # Bảng màu chuyên nghiệp: Deep Navy & Electric Blue
        self.color_navy = (13, 27, 62)
        self.color_accent = (26, 35, 126)
        self.color_text = (30, 39, 46)
        self.color_subtext = (70, 80, 90)
        self.set_margins(12, 12, 12)

    def header_section(self, name, contact_info, portfolio_url):
        # Header Background
        self.set_fill_color(*self.color_navy)
        self.rect(0, 0, 210, 48, 'F')

        # Name (Tăng size cực đại để tạo dấu ấn)
        self.set_y(15)
        self.set_font('helvetica', 'B', 32)
        self.set_text_color(255, 255, 255)
        self.cell(0, 15, name.upper(), align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Contact Info
        self.set_font('helvetica', '', 11)
        self.set_text_color(220, 220, 220)
        full_contact = f"{contact_info}  |  "
        text_width = self.get_string_width(full_contact + "Portfolio Website")
        self.set_x((210 - text_width) / 2)
        self.write(10, full_contact)

        # Portfolio Link
        self.set_font('helvetica', 'B', 11)
        self.set_text_color(100, 210, 255)
        self.write(10, "Portfolio Website", portfolio_url)
        self.ln(22)

    def draw_section_title(self, title):
        self.ln(5)
        self.set_font('helvetica', 'B', 16)
        self.set_text_color(*self.color_navy)
        self.cell(0, 10, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Thanh ngăn cách thiết kế hiện đại
        curr_y = self.get_y() - 2
        self.set_draw_color(*self.color_accent)
        self.set_line_width(1.2)
        self.line(self.l_margin, curr_y, self.l_margin + 30, curr_y)
        self.set_draw_color(200, 205, 210)
        self.set_line_width(0.3)
        self.line(self.l_margin + 30, curr_y, 210 - self.r_margin, curr_y)
        self.ln(5)

    def draw_subsection_header(self, title):
        """Tiêu đề phụ có nền xám để phân khối nội dung Trang 2 cực kỳ rõ ràng"""
        self.set_fill_color(242, 244, 247)
        self.set_font('helvetica', 'B', 12)
        self.set_text_color(*self.color_navy)
        self.cell(0, 9, f"  {title.upper()}", fill=True, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(3)

    def add_entry(self, title, subtitle, date, description_list):
        # Tiêu đề & Ngày tháng (Căn lề Grid)
        self.set_font('helvetica', 'B', 13)
        self.set_text_color(*self.color_text)
        self.cell(145, 7, title, new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('helvetica', 'B', 10.5)
        self.set_text_color(*self.color_subtext)
        self.cell(41, 7, date, align='R', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Vai trò/Công ty
        self.set_font('helvetica', 'I', 11.5)
        self.set_text_color(*self.color_accent)
        self.cell(0, 7, subtitle, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Mô tả dự án
        self.set_font('helvetica', '', 11)
        self.set_text_color(*self.color_text)
        for item in description_list:
            self.set_x(self.l_margin + 5)
            self.multi_cell(181, 6, f"- {item}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)

    def add_skill_row(self, label, skills):
        self.set_font('helvetica', 'B', 11.5)
        self.set_text_color(*self.color_navy)
        self.cell(42, 8, f"{label}:", new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('helvetica', '', 11.5)
        self.set_text_color(*self.color_text)
        self.multi_cell(0, 8, skills, new_x=XPos.LMARGIN, new_y=YPos.NEXT)


# --- KHỞI TẠO VÀ XUẤT FILE ---
cv = ExecutiveTechCV()
cv.set_auto_page_break(auto=True, margin=15)
MY_LINK = "https://duy-nguyen-portfolio.streamlit.app/"

# --- TRANG 1: PROFILE & CORE SKILLS ---
cv.add_page()
cv.header_section("NGUYEN HOANG DUY", "Ho Chi Minh City  |  (+84) 923 132 208  |  220803duy@gmail.com", MY_LINK)

cv.draw_section_title("Education")
cv.add_entry("Bachelor of Science in Artificial Intelligence", "FPT University", "2022 - 2026",
             ["GPA: 3.3/4.0 | Focus: Deep Learning, Computer Vision & Quantitative Research.",
              "Specialized Research: Vietnamese Lip-Reading models and Market Intelligence automation."])

cv.draw_section_title("Technical Expertise")
cv.add_skill_row("AI & Deep Learning", "Python (PyTorch, TensorFlow), OpenCV, MediaPipe, Langchain")
cv.add_skill_row("Data Engineering", "SQL, Pandas, NumPy, Tableau, Technical Indicators, Time-series")
cv.add_skill_row("Intelligent Systems", "LLM Orchestration (API AGENT), Multi-Agent Search, Automation")

cv.draw_section_title("Domain & Soft Skills")
cv.add_skill_row("Finance & Assets", "Quantitative Trading, Stock Market Analysis, Real Estate Planning")
cv.add_skill_row("Professional", "Technical Reporting, Data Visualization, Market Research, Problem Solving")

cv.draw_section_title("Awards & Honors")
cv.add_entry("First Prize - Robocon Southern Vietnam", "Regional Championship", "2021",
             ["Led technical architecture for the championship-winning autonomous robotics team."])
cv.add_entry("First Prize - Apps4Vsmart", "VinUniversity STEME DAY", "2020",
             ["Designed a high-impact mobile application awarded by VinUniversity leadership."])
cv.add_entry("Second Prize - City Science & Technology Contest", "HCMC Dept. of Education and Training", "2020-2021",
             ["Won Second Prize in the City-level Scientific Research Competition for High School Students.",
              "Recognized for excellence in technical innovation and scientific methodology."])

# --- TRANG 2: PROFESSIONAL PROJECTS ---
cv.add_page()
cv.set_y(15)
cv.draw_section_title("EXPERIENCE")

# I. AI Engineering
cv.draw_subsection_header("I. AI Engineering & Computer Vision")
cv.add_entry(
    "Vietnamese Lip-Reading System", "Project Lead & Architect", "2025 - 2026",
    ["Developed a LipNet-based Deep Learning model for Vietnamese viseme recognition.",
     "Integrated 3D-CNN and Bi-GRU layers with CTC Loss for temporal video processing.",
     "Deployed real-time inference pipeline using Streamlit with 65% accuracy rate."]
)
cv.add_entry(
    "AI Body Measurement Application", "CV Developer", "2024 - 2025",
    ["Orchestrated a pose-estimation pipeline using MediaPipe for contactless body measurement.",
     "Achieved 80% precision in image-to-metric transformation for fitness apparel industry.",
     "Automated data workflows to replace manual measurement processes."]
)

# II. Data Intelligence
cv.ln(2)
cv.draw_subsection_header("II. Data Science & Quantitative Intelligence")
cv.add_entry(
    "Quantitative Alpha Generation Bot", "Algorithm Developer", "2025 - 2026",
    ["Engineered a VN30F1M trading bot utilizing ML-based predictive signal generation.",
     "Backtested Alpha strategies on 5+ years of market data.",
     "Optimized execution latency and integrated real-time risk management protocols."]
)
cv.add_entry(
    "Multivariate Production Forecasting", "Lead Data Analyst", "2025",
    ["Architected time-series models to forecast commodity production cycles and supply chain trends.",
     "Optimized model accuracy by analyzing complex feature dependencies in multivariate datasets."]
)

# III. Automation
cv.ln(2)
cv.draw_subsection_header("III. Intelligent Automation & LLMs")
cv.add_entry(
    "Fitwear Market Intelligence Engine", "System Architect", "2026",
    ["Built a multi-agent system to automate competitor tracking for SK & VN fitness markets.",
     "Utilized Gemini API for large-scale sentiment analysis and brand ranking (Xexymix, Andar)."]
)
cv.add_entry(
    "Automated Document Processing (IDP)", "Automation Lead", "2025 - 2026",
    ["Pioneered an AWB extraction pipeline using Gemini API, reducing manual entry by 70%.",
     "Designed robust JSON parsing workflows for seamless integration with core business systems."]
)

cv.output("D:\Porfolio\\assets\\CV_NguyenHoangDuy.pdf")
