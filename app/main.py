import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
from app.utils import load_data, get_summary_stats, top_regions_table

st.set_page_config(layout='wide')
st.title("🌍 Solar Energy Comparison Dashboard")

# --- Sidebar
st.sidebar.header("Select Countries")
countries = st.sidebar.multiselect("Choose countries", ['Benin', 'Sierra Leone', 'Togo'], default=['Benin', 'Sierra Leone', 'Togo'])

metric = st.sidebar.selectbox("Select Metric", ['GHI', 'DNI', 'DHI'])

# --- Load data
data_dict = {country: load_data(country) for country in countries}

# --- Boxplot
st.subheader(f"📦 Boxplot Comparison of {metric}")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=[df[metric].dropna() for df in data_dict.values()], ax=ax)
ax.set_xticklabels(data_dict.keys())
ax.set_ylabel(metric)
st.pyplot(fig)

# --- Summary Table
st.subheader("📊 Summary Table")
summary_df = top_regions_table(data_dict)
st.dataframe(summary_df)

# --- ANOVA
if len(data_dict) > 1:
    ghi_values = [df['GHI'].dropna() for df in data_dict.values()]
    f_stat, p_value = f_oneway(*ghi_values)
    st.markdown(f"### 🔬 One-way ANOVA (GHI)")
    st.markdown(f"- F-statistic: `{f_stat:.2f}`")
    st.markdown(f"- P-value: `{p_value:.4f}`")
    if p_value < 0.05:
        st.success("Significant differences detected between countries (p < 0.05)")
    else:
        st.info("No significant difference detected between countries (p ≥ 0.05)")

# --- Visual Ranking
st.subheader("🏅 Country Ranking by Average GHI")
ranking_df = summary_df['Avg GHI'].sort_values(ascending=False).reset_index()
ranking_df.columns = ['Country', 'Avg GHI']
fig2, ax2 = plt.subplots(figsize=(8, 4))
sns.barplot(data=ranking_df, x='Avg GHI', y='Country', ax=ax2, palette='viridis')
st.pyplot(fig2)
