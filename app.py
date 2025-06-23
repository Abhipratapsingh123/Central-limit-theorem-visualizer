import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde

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
        selected_col = st.selectbox(
            "Select a numeric column for sampling", numeric_cols)

        # Sample size and number of samples
        sample_size = st.number_input(
            "Sample size (n ≥ 30)", min_value=30, value=50)
        num_samples = st.number_input(
            "Number of times to extract samples", min_value=1, value=100)

        if st.button("Generate Sampling Distribution"):
            samples = []
            for _ in range(num_samples):
                sample = df[selected_col].dropna().sample(
                    sample_size, replace=True)
                samples.append(sample.mean())

             # Plotting
            fig, ax = plt.subplots()

            # Histogram of sample means
            sns.histplot(samples, bins=20, ax=ax, edgecolor='black',
                         color='skyblue', stat='density', alpha=0.6)

            # KDE line using scipy
            kde = gaussian_kde(samples)
            x_vals = np.linspace(min(samples), max(samples), 1000)
            ax.plot(x_vals, kde(x_vals), color='red', linewidth=2, label='KDE')

            # Population mean line
            pop_mean = df[selected_col].mean()
            ax.axvline(pop_mean, color='green', linestyle='--',
                       label=f'Population Mean: {pop_mean:.2f}')

            ax.set_title("Sampling Distribution with KDE")
            ax.set_xlabel("Sample Means")
            ax.set_ylabel("Density")
            ax.legend()
            st.pyplot(fig)
