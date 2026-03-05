import streamlit as st
import pandas as pd
import altair as alt
from datetime import date

# ----------------------------
# Page config
# ----------------------------
st.set_page_config(
    page_title="Interactive Resume | Deyi Kong",
    page_icon="📄",
    layout="wide"
)

st.markdown(
    """
    <style>
      .resume-card {
        padding: 1.1rem 1.2rem;
        border: 1px solid rgba(49, 51, 63, 0.15);
        border-radius: 16px;
        background: rgba(255, 255, 255, 0.6);
        box-shadow: 0 6px 18px rgba(0,0,0,0.06);
      }
      .resume-card h4 {
        margin: 0 0 0.35rem 0;
        font-size: 0.95rem;
        color: rgba(49, 51, 63, 0.75);
        font-weight: 600;
      }
      .resume-card .value {
        font-size: 1.35rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 0.25rem;
      }
      .resume-card .sub {
        font-size: 0.92rem;
        color: rgba(49, 51, 63, 0.70);
        margin: 0;
      }
      .snap-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
      }
      @media (max-width: 900px) {
        .snap-grid { grid-template-columns: 1fr; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Resume content (from your PDF)
# ----------------------------
PROFILE = {
    "name": "Deyi Kong",
    "title": "Data Scientist | Data Analytics Engineer | Quantitative Analyst",
    "location": "Toronto, ON",
    "email": "deyi.kong@rotman.utoronto.ca",
    "phone": "(647) 888-1441",
    "linkedin": "https://linkedin.com/in/deyi-kong",
    "github": "https://github.com/eeeee-cmd",
    "summary": (
        "MMA candidate at Rotman with experience building production-style data pipelines, "
        "agentic NLP workflows, and risk-ranking models across capital markets and analytics."
    ),
}

# Skills (table + chart)
skills_df = pd.DataFrame(
    [
        {"Skill": "Python (Pandas, NumPy)", "Category": "Programming", "Proficiency": 90},
        {"Skill": "PySpark", "Category": "Data Engineering", "Proficiency": 78},
        {"Skill": "SQL", "Category": "Data Engineering", "Proficiency": 82},
        {"Skill": "Databricks", "Category": "Data Engineering", "Proficiency": 80},
        {"Skill": "Power BI", "Category": "BI/Visualization", "Proficiency": 78},
        {"Skill": "Tableau", "Category": "BI/Visualization", "Proficiency": 70},
        {"Skill": "Excel (VBA & Macros)", "Category": "Productivity", "Proficiency": 80},
        {"Skill": "LangChain", "Category": "ML / LLM", "Proficiency": 72},
        {"Skill": "XGBoost", "Category": "ML / LLM", "Proficiency": 78},
        {"Skill": "Scikit-learn", "Category": "ML / LLM", "Proficiency": 76},
        {"Skill": "PyTorch", "Category": "ML / LLM", "Proficiency": 68},
        {"Skill": "TensorFlow", "Category": "ML / LLM", "Proficiency": 60},
        {"Skill": "Git/GitHub", "Category": "Tools", "Proficiency": 75},
        {"Skill": "Jupyter Lab", "Category": "Tools", "Proficiency": 80},
        {"Skill": "R (Tidyverse, ggplot2)", "Category": "Programming", "Proficiency": 65},
        {"Skill": "MATLAB", "Category": "Programming", "Proficiency": 55},
        {"Skill": "Jira / Monday", "Category": "Tools", "Proficiency": 60},
    ]
)

education_df = pd.DataFrame(
    [
        {
            "Program": "Master of Management Analytics (Candidate)",
            "School": "Rotman School of Management, University of Toronto",
            "Dates": "Aug 2025 – Current",
            "Highlights": "Neural Network & Deep Learning; Databases & Dashboard; Predictive & Experimentation ML Modelling",
        },
        {
            "Program": "BSc Mathematics and Statistics",
            "School": "University of Toronto",
            "Dates": "Sep 2021 – Aug 2025",
            "Highlights": "",
        },
    ]
)

# Experience (with dates for timeline chart)
exp_df = pd.DataFrame(
    [
        {
            "Role": "Data Scientist (Global Capital Markets Advisory)",
            "Company": "NASDAQ",
            "Domain": "Data Science / Engineering",
            "Start": date(2026, 1, 12),
            "End": date(2026, 6, 11),  # ongoing (approx placeholder for timeline rendering)
            "Impact": [
                "Orchestrated a Databricks ETL pipeline using Pandas + PySpark; published curated SQL tables into Power BI Dataflows for automated refresh.",
                "Developed an agentic AI workflow with LangChain + OpenAI API to extract themes, generate summaries, and compute standardized sentiment scores; reduced time spent by 85%.",
                "Built an XGBoost investor-risk ranking model using AUM/flows/holdings/mandate signals; achieved 86% accuracy and visualized a risk heat matrix with Matplotlib.",
            ],
            "Tech": ["Databricks", "PySpark", "Python", "SQL", "Power BI", "LangChain", "XGBoost"],
        },
        {
            "Role": "Investment Analyst",
            "Company": "CITIC Securities (Shanghai, China)",
            "Domain": "Finance",
            "Start": date(2024, 8, 1),
            "End": date(2024, 8, 31),
            "Impact": [
                "Synthesized internal + client meetings into market briefs on macro trends, product positioning, and client priorities to improve sales alignment.",
                "Built an asset tracking + inventory audit system in Excel using advanced formulas, macros, and VBA automation to streamline loss reporting.",
                "Supported brokerage/trading operations across FICC, derivatives, and compliance workflows; strengthened understanding of front-to-back securities processes.",
            ],
            "Tech": ["Excel", "VBA", "Markets", "FICC"],
        },
        {
            "Role": "Investment Banking Associate",
            "Company": "Bank of Shanghai (Shanghai, China)",
            "Domain": "Finance / Risk",
            "Start": date(2023, 5, 1),
            "End": date(2023, 8, 31),
            "Impact": [
                "Conducted financial due diligence (BS/IS/CF) for tech + automotive clients; supported bond prospectus drafting and capital issuance.",
                "Redesigned risk reporting by integrating credit-risk stress testing and HQLA portfolio analytics to enhance liquidity monitoring and regulatory capital assessment.",
                "Leveraged Wind Financial Terminal for macro + company data to support screening and strategic evaluation.",
            ],
            "Tech": ["Financial Statements", "Risk", "HQLA", "Wind"],
        },
    ]
)

achievements_df = pd.DataFrame(
    [
        {
            "Achievement": "1st Place — Toronto Police Service Data & Safety Case",
            "Details": "Developed an event-aware, station-day crime risk model using 450K+ historical records + transit data for major city events (FIFA 2026).",
        },
        {
            "Achievement": "2nd Place — META Digital Marketing Strategy Case",
            "Details": "Market + audience analysis; designed omnichannel strategy to re-engage Gen Z/Millennials and accelerate online sales.",
        },
        {
            "Achievement": "2nd Place — BMO GAM Asset Allocation Case",
            "Details": "Built strategic asset allocation portfolio for HNW clients ($10M) using macro scenarios and risk-adjusted optimization.",
        },
        {"Achievement": "Finalists — Scotiabank Risk Management Case", "Details": ""},
    ]
)

# Projects section (derived from experience/achievements; feel free to add GitHub links)
projects_df = pd.DataFrame(
    [
        {
            "Project": "Agentic Qualitative NLP Workflow",
            "Type": "LLM / NLP",
            "Description": "LangChain + OpenAI workflow to extract themes, summarize text, and compute standardized sentiment scoring; reduced effort by 85%.",
        },
        {
            "Project": "Investor Risk Ranking Model",
            "Type": "Machine Learning",
            "Description": "XGBoost model for investor risk prioritization using AUM/flows/holdings/mandate signals; 86% accuracy + risk heat matrix.",
        },
        {
            "Project": "Event-aware Crime Risk Model (450K+ records)",
            "Type": "Applied Analytics",
            "Description": "Station-day risk forecasting using historical crime + transit/event signals to support resource planning for major city events (FIFA 2026).",
        },
    ]
)

# ----------------------------
# Sidebar widgets (3+ required)
# ----------------------------
st.sidebar.title("🔧 Customize View")

section = st.sidebar.radio(
    "Go to section",
    ["Overview", "Experience", "Projects", "Skills", "Education", "Achievements"],
    index=0
)

domain_filter = st.sidebar.multiselect(
    "Filter experience by domain",
    options=sorted(exp_df["Domain"].unique().tolist()),
    default=sorted(exp_df["Domain"].unique().tolist())
)

min_proficiency = st.sidebar.slider(
    "Minimum skill proficiency",
    min_value=0,
    max_value=100,
    value=65,
    step=5
)

show_links = st.sidebar.checkbox("Show contact links", value=True)

skills_view_mode = st.sidebar.selectbox(
    "Skills chart view",
    ["Top N skills", "Group by category"],
    index=0
)

# ----------------------------
# Header
# ----------------------------
left, right = st.columns([3, 2])

with left:
    st.title(f"📄 {PROFILE['name']}")
    st.subheader(PROFILE["title"])
    st.write(PROFILE["summary"])

with right:
    st.markdown("### Contact")
    st.write(f"📍 {PROFILE['location']}")
    st.write(f"✉️ {PROFILE['email']}")
    st.write(f"📞 {PROFILE['phone']}")
    if show_links:
        st.write(f"🔗 LinkedIn: {PROFILE['linkedin']}")
        st.write(f"💻 GitHub: {PROFILE['github']}")

st.divider()

# ----------------------------
# Overview
# ----------------------------
if section == "Overview":
    st.markdown("## Snapshot")

    st.markdown(
        """
        <div class="snap-grid">
          <div class="resume-card">
            <h4>Current</h4>
            <div class="value">MMA Candidate</div>
            <p class="sub">Rotman School of Management, UofT</p>
          </div>
          <div class="resume-card">
            <h4>Focus</h4>
            <div class="value">Data × ML × LLM</div>
            <p class="sub">Pipelines, modeling, agentic NLP workflows</p>
          </div>
          <div class="resume-card">
            <h4>Industries</h4>
            <div class="value">Capital Markets</div>
            <p class="sub">Risk, investor analytics, reporting automation</p>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### What you’ll find here")
    st.write("- Interactive filters for experience and skills")
    st.write("- Tables for education / achievements")
    st.write("- Charts for skills and experience timeline")

# ----------------------------
# Experience
# ----------------------------
elif section == "Experience":
    st.markdown("## Professional Experience")

    filtered_exp = exp_df[exp_df["Domain"].isin(domain_filter)].copy()

    exp_table = filtered_exp[["Role", "Company", "Domain", "Start", "End"]].copy()
    exp_table["Start"] = exp_table["Start"].astype(str)
    exp_table["End"] = exp_table["End"].astype(str)
    st.dataframe(exp_table, use_container_width=True, hide_index=True)

    st.markdown("### Drill into a role")
    role_choice = st.selectbox("Select a role", options=filtered_exp["Role"].tolist())
    row = filtered_exp[filtered_exp["Role"] == role_choice].iloc[0]

    st.markdown(f"**{row['Role']} — {row['Company']}**  \n*{row['Domain']} | {row['Start']} → {row['End']}*")
    st.write("**Impact:**")
    for b in row["Impact"]:
        st.write(f"- {b}")
    st.write("**Tech:** " + ", ".join(row["Tech"]))

    st.markdown("### Experience timeline")
    timeline = filtered_exp.copy()
    timeline["Start"] = pd.to_datetime(timeline["Start"])
    timeline["End"] = pd.to_datetime(timeline["End"])

    chart = (
        alt.Chart(timeline)
        .mark_bar()
        .encode(
            x=alt.X("Start:T", title="Start"),
            x2="End:T",
            y=alt.Y("Role:N", sort="-x", title="Role"),
            tooltip=["Role", "Company", "Domain", "Start", "End"],
        )
        .properties(height=260)
    )
    st.altair_chart(chart, use_container_width=True)

# ----------------------------
# Projects
# ----------------------------
elif section == "Projects":
    st.markdown("## Selected Projects")

    ptype = st.selectbox("Filter by project type", ["All"] + sorted(projects_df["Type"].unique().tolist()))
    view = projects_df if ptype == "All" else projects_df[projects_df["Type"] == ptype]

    st.dataframe(view, use_container_width=True, hide_index=True)

# ----------------------------
# Skills (table + chart)
# ----------------------------
elif section == "Skills":
    st.markdown("## Technical Skills")

    skills_view = skills_df[skills_df["Proficiency"] >= min_proficiency].copy()
    st.dataframe(skills_view, use_container_width=True, hide_index=True)

    st.markdown("### Skills chart")

    if skills_view.empty:
        st.info("No skills meet the current proficiency threshold. Lower the slider.")
    else:
        if skills_view_mode == "Top N skills":
            top_n = st.slider("Top N to display", 3, min(12, len(skills_view)), 8)
            plot_df = skills_view.sort_values("Proficiency", ascending=False).head(top_n)

            chart = (
                alt.Chart(plot_df)
                .mark_bar()
                .encode(
                    x=alt.X("Proficiency:Q", scale=alt.Scale(domain=[0, 100])),
                    y=alt.Y("Skill:N", sort="-x"),
                    tooltip=["Skill", "Category", "Proficiency"],
                )
                .properties(height=320)
            )
        else:
            chart = (
                alt.Chart(skills_view)
                .mark_bar()
                .encode(
                    x=alt.X("Skill:N", sort="-y"),
                    y=alt.Y("Proficiency:Q", scale=alt.Scale(domain=[0, 100])),
                    column=alt.Column("Category:N", title=None),
                    tooltip=["Skill", "Category", "Proficiency"],
                )
                .properties(height=320)
            )

        st.altair_chart(chart, use_container_width=True)

# ----------------------------
# Education
# ----------------------------
elif section == "Education":
    st.markdown("## Education")
    st.dataframe(education_df, use_container_width=True, hide_index=True)

# ----------------------------
# Achievements
# ----------------------------
elif section == "Achievements":
    st.markdown("## Achievements & Interests")
    st.dataframe(achievements_df, use_container_width=True, hide_index=True)
    st.markdown("### Interests")
    st.write("Skiing, photography, planting, travel, reading books")