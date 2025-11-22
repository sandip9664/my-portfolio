import streamlit as st

st.title("My Skills 🛠️")

# --- LOAD CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

st.write("Here is a breakdown of my technical expertise.")

st.write("---")

st.header("Technical Skills")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Programming & Tools")
    # Grouping skills for better layout
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap;">
        <span class="skill-chip">Python 🐍</span>
        <span class="skill-chip">SQL 🗄️</span>
        <span class="skill-chip">Power BI 📊</span>
        <span class="skill-chip">Excel 📗</span>
        <span class="skill-chip">Git & GitHub 🐙</span>
        <span class="skill-chip">VS Code 💻</span>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.subheader("Data Science")
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap;">
        <span class="skill-chip">Pandas 🐼</span>
        <span class="skill-chip">NumPy 🔢</span>
        <span class="skill-chip">Matplotlib 📈</span>
        <span class="skill-chip">Seaborn 🌊</span>
        <span class="skill-chip">Scikit-Learn 🤖</span>
        <span class="skill-chip">Machine Learning 🧠</span>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.header("Soft Skills")
st.write(
    """
    - **Problem Solving**: Strong analytical mindset from engineering background.
    - **Communication**: Ability to explain complex technical concepts clearly.
    - **Teamwork**: Experience working in collaborative environments.
    - **Adaptability**: Quick learner and eager to adopt new technologies.
    """
)
