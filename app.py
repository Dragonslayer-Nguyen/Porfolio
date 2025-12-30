import streamlit as st
from sections.about import about
from sections.projects import projects
from sections.skills import skills
from sections.contact import contact

# Cấu hình trang với tiêu đề tiếng Anh chuyên nghiệp
st.set_page_config(
    page_title="Nguyen Hoang Duy | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
st.sidebar.markdown("---") # Đường kẻ phân cách cho sạch sẽ

page = st.sidebar.radio(
    "Go to:",
    ["About Me", "Featured Projects", "Technical Skills", "Contact & Network"]
)

# Logic điều hướng
if page == "About Me":
    about()
elif page == "Featured Projects":
    projects()
elif page == "Technical Skills":
    skills()
else:
    contact()
