import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Shane Thailand | CFA L3", layout="wide")

# --- Custom CSS for Styling ---
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

    /* Workflow Tiles */
    .workflow-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin-bottom: 30px;
    }
    .workflow-tile {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
    }
    .workflow-tile h4 {
        margin-top: 0;
        color: #deff9a;
    }

    /* Roadmap Styles */
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

    .phase-card.active {
        border: 1px solid #deff9a;
        background-color: #1c2128;
    }

    .phase-badge {
        position: absolute;
        left: -41px;
        top: 20px;
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: #30363d;
        border: 4px solid #0a0c10;
    }

    .phase-badge.active {
        background-color: #deff9a;
        box-shadow: 0 0 10px #deff9a;
    }

    .status-pill {
        display: inline-block;
        padding: 2px 8px;
        border-radius: 10px;
        font-size: 10px;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 10px;
        background-color: #deff9a;
        color: #000;
    }

    .contact-link {
        color: #deff9a;
        text-decoration: none;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- Header ---
st.title("📈 Welcome to the Macro Terminal")

# --- A bit about me ---
st.markdown(
    """
    <div class="intro-section">
        <h3>A bit about me</h3>
        <p>Hi! I’m <strong>Shane from Thailand 🇹🇭</strong>. I recently passed the <strong>CFA Level 3</strong> exam, and after spending so much time buried in textbooks, 
        I really wanted to see if I could actually build something with all that theory. This app is just a hobby project of mine to practice 
        and show how some of those CFA concepts look when you put them into code. It's my way of proving I can bridge the gap 
        between financial theory and practical application!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Workflow ---
st.subheader("How I built this (The 'Finance Guy' way)")
st.write("I’m definitely not a professional developer, so I looked for the easiest and most efficient way to get this running:")

st.markdown(
    """
    <div class="workflow-container">
        <div class="workflow-tile">
            <h4>🐍 Python</h4>
            <p style="font-size: 14px; color: #daffde;">The "gold standard" for finance. Powerful enough to handle heavy math and automate calculations that would take forever in a spreadsheet.</p>
        </div>
        <div class="workflow-tile">
            <h4>🐙 GitHub</h4>
            <p style="font-size: 14px; color: #daffde;">This is basically where I keep my "save files." It stores my code in the cloud so I don't lose it and can track every single change.</p>
        </div>
        <div class="workflow-tile">
            <h4>🎨 Streamlit</h4>
            <p style="font-size: 14px; color: #daffde;">The magic wand. It takes my Python code and turns it into this website, saving me from having to learn web design from scratch.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Balloon magic trigger
if st.button("🎈 Celebrate with Streamlit magic!", use_container_width=True):
    st.balloons()
    st.toast("Balloons sent! 🚀")

st.divider()

# --- Roadmap ---
st.subheader("🗺️ Stuff I’m working on")

st.markdown(
    """
    <div class="roadmap-container">
        <!-- Phase 1 -->
        <div class="phase-card active">
            <div class="phase-badge active"></div>
            <div class="status-pill">Where we are: Phase 1 (Live Now) 🚀</div>
            <h4 style="margin: 0;">Phase 1: Buy & Hold MCS (Current)</h4>
            <p style="color: #8b949e; font-size: 14px; margin-top: 10px;">
                Just the basics. You pick your stocks, choose a date range, and set your weights. The app runs a Monte Carlo Simulation (MCS) to show potential realities for your money.
            </p>
        </div>
        <!-- Phase 2 -->
        <div class="phase-card">
            <div class="phase-badge"></div>
            <h4 style="margin: 0;">Phase 2: Finding "Better" Weights</h4>
            <p style="color: #8b949e; font-size: 14px; margin-top: 10px;">
                Adding an "Efficient Frontier" tool to find the specific mix of stocks that gives you the best return for your target risk level.
            </p>
        </div>
        <!-- Phase 3 -->
        <div class="phase-card">
            <div class="phase-badge"></div>
            <h4 style="margin: 0;">Phase 3: Stress Testing</h4>
            <p style="color: #8b949e; font-size: 14px; margin-top: 10px;">
                Testing how your portfolio would have survived "Black Swan" events like the 2008 crash or the 2020 COVID drop.
            </p>
        </div>
        <!-- Phase 4 -->
        <div class="phase-card">
            <div class="phase-badge"></div>
            <h4 style="margin: 0;">Phase 4: Different Weighting Styles</h4>
            <p style="color: #8b949e; font-size: 14px; margin-top: 10px;">
                Moving beyond "Buy & Hold" to explore institutional methods like Risk Parity and Inverse Volatility.
            </p>
        </div>
        <!-- Phase 5 -->
        <div class="phase-card">
            <div class="phase-badge"></div>
            <h4 style="margin: 0;">Phase 5: Real-World Math</h4>
            <p style="color: #8b949e; font-size: 14px; margin-top: 10px;">
                Adding non-normal distribution models to account for those crazy market "tail risks" that standard math ignores.
            </p>
        </div>
        <!-- Phase 6 -->
        <div class="phase-card">
            <div class="phase-badge"></div>
            <h4 style="margin: 0;">Phase 6: To Rebalance or Not?</h4>
            <p style="color: #8b949e; font-size: 14px; margin-top: 10px;">
                Simulating auto-rebalancing to see if periodic checking actually helps your returns in the long run.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --- Contact ---
st.divider()
st.subheader("🤝 Let’s chat!")
st.markdown(
    """
    I’m currently looking for my first role in finance, so if you’re hiring or just want to talk shop, I’d love to connect!
    
    👉 **LinkedIn:** [shanesri](https://www.linkedin.com/in/shanesri/)
    """,
    unsafe_allow_html=True,
)

# Launch button for the main app
st.link_button("🚀 Open Monte Carlo Simulator", "https://mcsbyshane.streamlit.app/")
