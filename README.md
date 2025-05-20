# ☀️ Solar Challenge - Week 0

Welcome to the **Solar Challenge - Week 0** repository!  
This project is designed to help you get started with Python-based **solar data analysis**, **interactive dashboards**, and **automation using CI/CD workflows**.

---

## 🚀 Quick Setup

Get started with the project on your local machine:

```bash
# Clone the repository
git clone https://github.com/ET-SPARK/solar-challenge-week0.git

# Navigate into the project directory
cd solar-challenge-week0

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📊 Streamlit Dashboard

We’ve built an interactive dashboard using Streamlit to explore and visualize solar data in a user-friendly web interface.

### ▶️ Run the dashboard locally

```bash
streamlit run app/main.py
```

This will launch the app in your default browser.

### 🖼 Dashboard Screenshots

Preview what the dashboard looks like! Screenshots are available in the `dashboard_screenshots` branch.

**Highlights include:**

- Solar output over time (line charts, bar graphs)
- Wind direction visualizations (windrose plots)
- Summary stats and regional comparisons

---

## 🗂 Project Structure

```bash
solar-challenge-week0/
├── .vscode/                # Editor settings
│   └── settings.json
├── .github/               # GitHub Actions workflows
│   └── workflows/
│       └── ci.yml
├── app/                   # Streamlit dashboard application
│   └── main.py
├── src/                   # Source code (e.g., utils, processing)
├── notebooks/             # Jupyter notebooks for exploration
│   ├── __init__.py
│   └── README.md
├── scripts/               # Helper scripts
│   ├── __init__.py
│   └── README.md
├── tests/                 # Unit tests
│   └── __init__.py
├── requirements.txt       # Python dependencies
├── .gitignore             # Ignored files
└── README.md              # Project overview (this file)
```

---

## 📦 Features

- ✅ Modular Python codebase
- 📊 Interactive Streamlit dashboard
- 🧮 Statistical analysis (e.g., ANOVA via SciPy)
- 🌪 Windrose plots for wind direction
- 🧪 Unit testing setup
- ⚙️ Automated CI with GitHub Actions
- 🔒 Sensitive data kept secure (not tracked by Git)

---

## 🤝 Contributing

We welcome contributions to improve analysis, dashboards, or add new features!

1. Fork the repository
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes
4. Commit and push:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request

---
