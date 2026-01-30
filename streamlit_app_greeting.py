import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Shane Thailand | CFA L3 Candidate", layout="wide")

# --- Custom CSS ---
st.markdown(
    """
    <style>
    [data-testid="stAppViewBlockContainer"] {
        max-width: 1000px !important;
        margin: 0 auto !important;
        padding-top: 2rem !important;
    }
    .intro-section {
        background-color: #1e2130;
        padding: 30px;
        border-radius: 15px;
        border: 1px solid #30363d;
        margin-bottom: 30px;
    }
    .roadmap-container {
        border-left: 2px solid #30363d;
        margin-left: 20px;
        padding-left: 30px;
        position: relative;
    }
    .phase-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        position: relative;
    }
    .phase-card.active { border: 1px solid #4589ff; background-color: #1c2128; }
    .phase-badge {
        position: absolute; left: -41px; top: 20px; width: 20px; height: 20px;
        border-radius: 50%; background-color: #30363d; border: 4px solid #0e1117;
    }
    .phase-badge.active { background-color: #4589ff; box-shadow: 0 0 10px #4589ff; }
    .status-pill {
        display: inline-block; padding: 2px 8px; border-radius: 10px; font-size: 10px;
        font-weight: 800; text-transform: uppercase; margin-bottom: 10px;
        background-color: #4589ff; color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
st.title("👋 Welcome to the Macro Terminal")

# --- Intro ---
st.markdown(
    """
    <div class="intro-section">
        <h3>About Me</h3>
        <p>Hi, I'm <strong>Shane Thailand</strong>. I am a <strong>CFA Level 3 Passed</strong> candidate looking for a high-impact financial role where I can combine investment expertise with modern technology.</p>
        <h3>The Goal</h3>
        <p>My goal is to explore financial concepts using <strong>AI-assisted coding, Python, and Streamlit</strong> to create "Finance Made Easy" tools.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Roadmap ---
st.subheader("🗺️ Strategic Roadmap")
st.markdown(
    """
    <div class="roadmap-container">
        <div class="phase-card active"><div class="phase-badge active"></div><div class="status-pill">Phase 1: LIVE NOW</div>
            <h4>VER 1: Buy & Hold MCS</h4>
            <p style="color: #8b949e; font-size: 14px;">The foundation simulation engine. User picks assets, dates, and weights.</p>
        </div>
        <div class="phase-card"><div class="phase-badge"></div>
            <h4>VER 2: Efficient Frontier Integration</h4>
            <p style="color: #8b949e; font-size: 14px;">Automated portfolio weighting optimization to maximize returns.</p>
        </div>
        <div class="phase-card"><div class="phase-badge"></div>
            <h4>VER 3: Stress Testing</h4>
            <p style="color: #8b949e; font-size: 14px;">Feature-rich stress tests for MCS against Black Swan events.</p>
        </div>
        <div class="phase-card"><div class="phase-badge"></div>
            <h4>VER 4-7: Advanced Analytics</h4>
            <p style="color: #8b949e; font-size: 14px;">Non-normal distributions and Auto-rebalancing feature simulations.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Links ---
st.divider()
st.subheader("🤝 Connect with Me")
st.markdown("👉 **LinkedIn:** [shanesri](https://www.linkedin.com/in/shanesri/)")

# Link to your MAIN MCS APP
st.link_button("🚀 Launch Monte Carlo Simulator", "https://portmng.streamlit.app")
