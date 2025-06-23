import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Central Limit Theorem Visualizer")

# Upload dataset
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Get numeric columns
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if not numeric_cols:
        st.error("No numeric columns found in the dataset.")
    else:
        # Column selection
        selected_col = st.selectbox("Select a numeric column for sampling", numeric_cols)

        # Sample size and number of samples
        sample_size = st.number_input("Sample size (n ≥ 30)", min_value=30, value=50)
        num_samples = st.number_input("Number of times to extract samples", min_value=1, value=100)

        if st.button("Generate Sampling Distribution"):
            samples = []
            for _ in range(num_samples):
                sample = df[selected_col].dropna().sample(sample_size, replace=True)
                samples.append(sample.mean())

            # Plotting
            
            fig, ax = plt.subplots()
            sns.histplot(samples,bins=20, kde=True, ax=ax, edgecolor='black', color='skyblue',line_kws={'color': 'red', 'linewidth': 2})
            # ax.axvline(samples, color='red', linestyle='--', label=f'Population Mean: {samples:.2f}')
            ax.set_title("Sampling Distribution with KDE")
            ax.set_xlabel("Sample Means")
            ax.set_ylabel("Frequency")
            ax.legend()
            st.pyplot(fig)
