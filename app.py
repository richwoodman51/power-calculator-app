import streamlit as st
# Import the power calculation function from statsmodels
from statsmodels.stats.power import TTestIndPower

# --- Page Configuration ---
st.set_page_config(layout="wide", page_title="Power Calculator")

# --- App Title and Description ---
st.title("Interactive Power Calculator")
st.write("Calculate the required sample size for a two-sample t-test.")

# --- UI Layout ---
st.divider() # Adds a horizontal line
col1, col2, col3 = st.columns(3)

# --- Column 1: Study Parameters ---
with col1:
    st.header("Study Parameters")
    alpha = st.slider("Significance level (alpha)", 0.01, 0.10, 0.05, 0.01,
                      help="The probability of a Type I error (rejecting a true null hypothesis).")
    
    power = st.slider("Desired power (1 - beta)", 0.5, 0.99, 0.8, 0.01,
                      help="The probability of correctly rejecting a false null hypothesis.")

# --- Column 2: Effect Size ---
with col2:
    st.header("Effect Size")
    effect_size = st.slider("Effect size (Cohen's d)", 0.1, 2.0, 0.5, 0.05,
                            help="The standardized mean difference between the two groups.")

# --- Column 3: Calculation and Results ---
with col3:
    st.header("Calculated Sample Size")
    
    # --- Perform the Power Calculation ---
    # 1. Initialize the power analysis object
    analysis = TTestIndPower()
    
    # 2. Calculate the sample size
    # We pass effect_size, alpha, and power. 'nobs1=None' tells the function this is what we want to solve for.
    sample_size = analysis.solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=1.0,  # Assuming equal group sizes
        alternative='two-sided'
    )
    
    # --- Display the Result ---
    # Use st.metric for a nice, clear display
    st.metric(
        label="Required Sample Size (per group)",
        value=f"{round(sample_size)}"
    )

    st.info("This calculation assumes a two-sample, two-sided t-test with equal-sized groups.", icon="ℹ️")

# ===================================================================
# CELL 3: RUN THE APP
# ===================================================================

# Step 3: Set up the ngrok tunnel and run the Streamlit app
from pyngrok import ngrok
import subprocess

# Paste your ngrok authtoken here
ngrok.set_auth_token("367yOdDU7U93A1EWqnHuacehtJ9_4UL4xJVb8scVovhqdeU6e")

# Open a tunnel to the streamlit port (8501)
public_url = ngrok.connect(8501)
print(f"Your Streamlit app is live at: {public_url}")

# Run the streamlit app in the background.
# This is a more robust way to run it in Colab.
process = subprocess.Popen(["streamlit", "run", "app.py", "--server.runOnSave", "true"])

