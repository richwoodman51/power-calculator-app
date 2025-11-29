import streamlit as st
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
    analysis = TTestIndPower()
    
    sample_size = analysis.solve_power(
        effect_size=effect_size,
        alpha=alpha,
        power=power,
        ratio=1.0,  # Assuming equal group sizes
        alternative='two-sided'
    )
    
    # --- Display the Result ---
    st.metric(
        label="Required Sample Size (per group)",
        value=f"{round(sample_size)}"
    )

    st.info("This calculation assumes a two-sample, two-sided t-test with equal-sized groups.", icon="ℹ️")
