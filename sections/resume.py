from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.lib import colors
from reportlab.lib.units import inch
import io


def create_final_cv():
    buffer = io.BytesIO()

    # Lề chuẩn quốc tế (0.5 - 0.75 inch)
    doc = SimpleDocTemplate(
        buffer,
        pagesize=(612, 792),
        rightMargin=45, leftMargin=45, topMargin=40, bottomMargin=40
    )

    styles = getSampleStyleSheet()
    primary_color = colors.HexColor("#1a2a44")

    # --- CUSTOM STYLES ---
    name_style = ParagraphStyle('Name', fontSize=24, fontName='Helvetica-Bold', spaceAfter=2, alignment=TA_CENTER,
                                textColor=primary_color)
    sub_name = ParagraphStyle('SubName', fontSize=12, fontName='Helvetica-Bold', spaceAfter=8, alignment=TA_CENTER,
                              textColor=colors.grey)
    contact_style = ParagraphStyle('Contact', fontSize=9.5, fontName='Helvetica', alignment=TA_CENTER, spaceAfter=12)

    heading_style = ParagraphStyle('Heading', fontSize=12, fontName='Helvetica-Bold', textColor=primary_color,
                                   spaceBefore=12, spaceAfter=4, textTransform='UPPERCASE')
    job_title = ParagraphStyle('JobTitle', fontSize=10.5, fontName='Helvetica-Bold', leading=12)
    date_style = ParagraphStyle('Date', fontSize=9.5, fontName='Helvetica-Oblique', alignment=2)
    body_style = ParagraphStyle('Body', fontSize=10, leading=14, fontName='Helvetica', alignment=TA_JUSTIFY)
    bullet_style = ParagraphStyle('Bullet', parent=body_style, leftIndent=12, firstLineIndent=0, spaceBefore=2)

    content = []

    # --- 1. HEADER (Fix overlap) ---
    content.append(Paragraph("NGUYEN HOANG DUY", name_style))
    content.append(Spacer(1, 20))  # Tạo khoảng trống chống đè chữ
    content.append(Paragraph("AI ARCHITECT | AUTOMATION ENGINEER", sub_name))

    contact_info = (
        "Ho Chi Minh City, VN  •  0923132208  •  "
        "<a href='mailto:220803duy@gmail.com' color='#1a2a44'>220803duy@gmail.com</a><br/>"
    )
    content.append(Paragraph(contact_info, contact_style))

    # --- 2. SUMMARY (Focus on Business AI) ---
    content.append(Paragraph("Professional Summary", heading_style))
    content.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=8))
    content.append(Paragraph(
        "Strategic **Automation Architect** specializing in the integration of AI-driven intelligence into core business processes. "
        "Expert in designing **Agentic Workflows** and **RAG-based systems** that transform unstructured data into actionable assets. "
        "Proven track record in architecting end-to-end autonomous pipelines that replace manual cognitive labor, "
        "significantly increasing ROI through Intelligent Document Processing and Predictive Analytics.",
        body_style
    ))

    # --- 3. TECHNICAL EXPERTISE ---
    content.append(Paragraph("Technical Expertise", heading_style))
    content.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=8))

    skills_data = [
        [Paragraph("• <b>AI/ML:</b> LLMs (Gemini, GPT), RAG, LangChain, PyTorch", body_style),
         Paragraph("• <b>Computer Vision:</b> YOLOv8, MediaPipe, OpenCV", body_style)],
        [Paragraph("• <b>Automation:</b> n8n, Agentic Workflows, Playwright, Scrapy", body_style),
         Paragraph("• <b>Data:</b> SQL, Pandas, NumPy, Vector Databases", body_style)]
    ]
    skills_table = Table(skills_data, colWidths=[3.4 * inch, 3.4 * inch])
    skills_table.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('VALIGN', (0, 0), (-1, -1), 'TOP')]))
    content.append(skills_table)

    # --- 4. EXPERIENCE ---
    content.append(Paragraph("Professional Experience", heading_style))
    content.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=8))

    # Exp 1
    header1 = Table([[Paragraph("<b>AI Automation Architect</b> | Freelance", job_title),
                      Paragraph("Jan 2024 – Present", date_style)]], colWidths=[5 * inch, 2.2 * inch])
    header1.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    content.append(header1)

    bullets1 = [
        "<b>Intelligent Document Processing (IDP):</b> Engineered a multi-stage pipeline using Gemini 1.5 Pro to extract structured data from logistics invoices with 99% accuracy.",
        "<b>Custom AI Agents:</b> Spearheaded the development of autonomous n8n agents for lead generation and CRM synchronization, saving 40+ manual hours per week.",
        "<b>Performance Optimization:</b> Reduced model inference latency by 30% through advanced prompt engineering and context window management."
    ]
    for b in bullets1: content.append(Paragraph(f"• {b}", bullet_style))
    content.append(Spacer(1, 10))

    # Exp 2
    header2 = Table([[Paragraph("<b>Quantitative Developer</b> | FinTech", job_title),
                      Paragraph("Jun 2023 – Dec 2023", date_style)]], colWidths=[5 * inch, 2.2 * inch])
    header2.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0), ('BOTTOMPADDING', (0, 0), (-1, -1), 2)]))
    content.append(header2)

    bullets2 = [
        "<b>Alpha Generation:</b> Architected backtesting engines for VN30F1M index using statistical modeling, delivering +30% annualized ROI.",
        "<b>Predictive Logistics:</b> Optimized workforce allocation using XGBoost, resulting in a 15% reduction in operational overhead."
    ]
    for b in bullets2: content.append(Paragraph(f"• {b}", bullet_style))

    # --- 5. SELECTED PROJECTS ---
    content.append(Paragraph("Selected Projects", heading_style))
    content.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=8))

    projs = [
        ("<b>TrendPulse AI:</b> Multi-agent system for real-time fashion market intelligence.",
         "Gemini Flash, n8n, Selenium"),
        ("<b>Vietnamese Lip Reading:</b> Visual speech recognition using CNN + Bi-GRU and MediaPipe.",
         "Python, TensorFlow, MediaPipe"),
        ("<b>Virtual Tailor:</b> Contactless body measurement system using YOLOv8-pose estimation.",
         "OpenCV, YOLOv8, C++")
    ]
    for title, tech in projs:
        content.append(Paragraph(f"{title} | <i>{tech}</i>", job_title))
        content.append(Spacer(1, 4))

    # --- 6. EDUCATION ---
    content.append(Paragraph("Education", heading_style))
    content.append(HRFlowable(width="100%", thickness=1, color=primary_color, spaceAfter=8))

    edu = Table([[Paragraph("<b>Bachelor of IT (Artificial Intelligence)</b> - FPT University", job_title),
                  Paragraph("Graduated 2024", date_style)]], colWidths=[5.5 * inch, 1.7 * inch])
    edu.setStyle(TableStyle([('LEFTPADDING', (0, 0), (-1, -1), 0)]))
    content.append(edu)
    content.append(Paragraph("• Graduated with High Distinction; GPA: 8.1/10", bullet_style))

    doc.build(content)
    buffer.seek(0)
    return buffer


if __name__ == "__main__":
    pdf = create_final_cv()
    with open("NguyenHoangDuy_Architect_CV.pdf", "wb") as f:
        f.write(pdf.getbuffer())
    print("✅ CV đã được tối ưu chuẩn quốc tế!")