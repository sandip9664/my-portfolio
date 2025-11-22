import streamlit as st

st.title("My Projects 🚀")

# --- LOAD CSS ---
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

st.write("Here are some of the key projects I've worked on during my journey into Data Science.")

# --- PROJECT 1 ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # SQL Project Image
        st.image("assets/sql_project1.png", width="stretch") 
        st.info("SQL Project") 
    with col2:
        st.subheader("SQL Data Analysis Project")
        st.write(
            """
            **Description:**
            A learning-based SQL project built in **pgAdmin 4** to practice PostgreSQL queries. 
            
            It includes comprehensive examples of:
            - `SELECT` statements & Data Filtering
            - Joins (Inner, Left, Right, Full)
            - `GROUP BY` & Aggregations
            - Common Table Expressions (CTEs)
            - Window Functions
            - Complex Data Analysis Queries
            
            **Tools Used:**
            - 🐘 **PostgreSQL** (Database)
            - 🛠️ **pgAdmin 4** (Database Management Tool)
            """
        )
        st.markdown("https://github.com/sandip9664/SQL_DATA_ANALYST_PROJECT") 

st.write("---")

# --- PROJECT 2 ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # PowerBI Project Image
        st.image("assets/cc_transaction_report_screenshot.png", width="stretch") 
        st.info("PowerBI Project")
    with col2:
        st.subheader("Credit Card Weekly Dashboard")
        st.write(
            """
            **Description:**
            A comprehensive and dynamic **Power BI** dashboard for credit card transaction and customer analysis.
            
            **Objective:**
            To provide real-time insights into key performance metrics and trends, enabling stakeholders to monitor and analyze credit card operations effectively.
            
            **Key Features:**
            - Real-time insight into transaction trends.
            - Customer segmentation and analysis.
            - Performance monitoring of credit card operations.
            
            **Tools Used:**
            - 📊 **Power BI** (Dashboard & Visualization)
            - 🐘 **PostgreSQL** (Data Source)
            """
        )
        st.markdown("https://github.com/sandip9664/credit_card_analysis_project")

st.write("---")

# --- PROJECT 3 ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # Fraud Detection Project Image
        st.image("assets/fraud_detection.png", width="stretch")
        st.info("Fraud Transaction Detection")
    with col2:
        st.subheader("Credit Card Fraud Detection")
        st.write(
            """
            **Description:**
            Developed and evaluated machine learning models for credit card fraud detection using a highly imbalanced dataset. The goal was to maximize recall for fraudulent transactions while maintaining overall performance.
            
            **Key Findings:**
            - **XGBoost Classifier** emerged as the best model, balancing high Recall and superior AUC-ROC score.
            - Successfully addressed severe class imbalance (0.1727% fraud) using stratification and feature scaling.
            
            **Methodology:**
            - **Preprocessing:** Stratified split, StandardScaler.
            - **Models:** Logistic Regression, Random Forest, XGBoost.
            - **Tuning:** GridSearchCV for XGBoost optimization.
            
            **Tools Used:**
            - 🤖 **Scikit-Learn & XGBoost** (Machine Learning)
            - 🐍 **Python** (Pandas, NumPy)
            """
        )
        st.markdown("https://github.com/sandip9664/credit-card-fraud-detection-using-machine-learning")

st.write("---")

# --- PROJECT 4 ---
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        # Predictive Maintenance Project Image
        st.image("assets/maintenance-lifecycle.png", width="stretch")
        st.info("Machine Maintenance Lifecycle")
    with col2:
        st.subheader("Predictive Maintenance Model")
        st.write(
            """
            **Description:**
            Developed a predictive maintenance model to anticipate machine failures and classify their specific types (e.g., Power Failure, Overstrain Failure).
            
            **Key Findings:**
            - **High Accuracy:** Optimized Random Forest model achieved **F1 scores of ~0.98** for both binary (failure vs. no failure) and multi-class classification.
            - **Critical Features:** Torque [Nm], Rotational speed [rpm], and Tool wear [min] were identified as the most influential predictors.
            
            **Practical Application:**
            - Designed for integration into real-time monitoring systems.
            - Enables proactive maintenance to reduce downtime and extend equipment lifespan.
            
            **Tools Used:**
            - 🌲 **Random Forest Classifier** (Machine Learning)
            - 🐍 **Python** (Scikit-Learn, Pandas)
            """
        )
        st.markdown("https://github.com/sandip9664/predictive-machine-maintenance-using-ML-model")

st.write("---")
