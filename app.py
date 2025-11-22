import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded",
)

import base64
import os

# --- LOAD CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Create assets folder and style.css if they don't exist yet to avoid errors
local_css("assets/style.css") 

# --- HERO SECTION ---
col1, col2 = st.columns([2, 1], gap="small")
with col1:
    st.title("Hi, I'm Sandip (DEBUG MODE 🔴)")
    st.subheader("Aspiring Data Analyst & Data Scientist")
    st.write(
        """
        I am an Electrical Engineer transitioning into the world of Data Science. 
        I combine my analytical engineering background with modern data tools to uncover insights and solve problems.
        """
    )
    st.write("---")
    import os
    st.write(f"Current working directory: {os.getcwd()}")
    st.write("Files in current directory:")
    st.write(os.listdir('.'))
    if os.path.exists('assets'):
        st.write("Files in assets folder:")
        st.write(os.listdir('assets'))
    
    resume_path = "assets/Sandip_Resume.pdf"
    if os.path.exists(resume_path):
        st.success(f"Resume found at: {resume_path}")
        with open(resume_path, "rb") as f:
            pdf_data = f.read()
        st.download_button(
            label="📄 Download Resume",
            data=pdf_data,
            file_name="Sandip_Resume.pdf",
            mime="application/pdf",
        )
    else:
        st.error(f"Resume NOT found at {resume_path}")

with col2:
    # Logic to display profile picture
    profile_pic_path = "assets/profile-pic.png"  # Default name for your profile picture
    
    if os.path.exists(profile_pic_path):
        img_base64 = get_img_as_base64(profile_pic_path)
        img_src = f"data:image/png;base64,{img_base64}"
    else:
        # Fallback to placeholder if file doesn't exist
        img_src = "https://ui-avatars.com/api/?name=Sandip+Barariya&background=f472b6&color=fff&size=300&rounded=true&bold=true"

    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="{img_src}" class="profile-img" width="300">
        </div>
        """,
        unsafe_allow_html=True
    )

# --- ABOUT ME ---
st.header("About Me")
st.write(
    """
    <div style="background-color: rgba(255, 255, 255, 0.05); padding: 20px; border-radius: 10px; border-left: 5px solid #f472b6;">
    I am a fresher with a strong foundation in <b>Electrical Engineering</b>, now channeling my analytical skills into <b>Data Analytics</b>. 
    My journey from engineering to data science is driven by a passion for logic, problem-solving, and continuous learning.
    <br><br>
    I am actively building projects to demonstrate my expertise in <b>Python</b>, <b>Data Visualization</b>, and <b>Machine Learning</b>. 
    I am eager to contribute to data-driven teams and tackle real-world challenges.
    </div>
    """,
    unsafe_allow_html=True
)
