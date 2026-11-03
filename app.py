import time
import streamlit as st

st.set_page_config(
    page_title="Calphen Hardware Showcase", page_icon="🏗️", layout="centered"
)

# Custom styling to make it look like a video presentation screen
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    .slide-box {
        padding: 40px;
        border-radius: 15px;
        background: linear-gradient(135deg, #1f2937, #111827);
        border: 2px solid #374151;
        text-align: center;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5);
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.title("🏗️ Calphen Hardware Live Display")
st.write(
    "All building and construction appliances under one roof. Sit back or"
    " control the slides below!"
)
st.markdown("---")

# Define the slides/appliances showcase
slides = [
    {
        "title": "Welcome to Calphen Hardware",
        "desc": (
            "Your trusted partner for all building and construction"
            " appliances."
        ),
        "icon": "🏗️",
        "tag": "Open For Business",
    },
    {
        "title": "Cement & Heavy Aggregates",
        "desc": "Top-grade 50kg cement bags and structural materials.",
        "icon": "🧱",
        "tag": "Best Sellers",
    },
    {
        "title": "Roofing Sheets & Timber",
        "desc": "Gauge 28 roofing sheets, iron sheets, and framing timber.",
        "icon": "🏠",
        "tag": "Quality Assured",
    },
    {
        "title": "Plumbing Supplies",
        "desc": "PVC water pipes, ball valves, fittings, and connectors.",
        "icon": "🚰",
        "tag": "All Sizes Available",
    },
    {
        "title": "Electrical Appliances",
        "desc": "Conduit pipes, cables, switches, and wiring fixtures.",
        "icon": "⚡",
        "tag": "Safe & Certified",
    },
    {
        "title": "Fasteners & Hardware Tools",
        "desc": "Assorted nails, binding wire, hinges, and locks.",
        "icon": "🔩",
        "tag": "Everything You Need",
    },
    {
        "title": "Visit Us Today or Order for Site Delivery!",
        "desc": "Call or WhatsApp us for fast delivery right to your construction site.",
        "icon": "🚚",
        "tag": "Contact Us Now",
    },
]

# Session state to track slide index
if "slide_index" not in st.session_state:
  st.session_state.slide_index = 0

# Control buttons
col_prev, col_auto, col_next = st.columns([1, 2, 1])

with col_prev:
  if st.button("◀ Previous", use_container_width=True):
    st.session_state.slide_index = (st.session_state.slide_index - 1) % len(
        slides
    )

with col_next:
  if st.button("Next ▶", use_container_width=True):
    st.session_state.slide_index = (st.session_state.slide_index + 1) % len(
        slides
    )

with col_auto:
  auto_play = st.checkbox("▶ Auto-Play Slideshow", value=False)

# Get current slide data
current = slides[st.session_state.slide_index]

# Render the presentation slide card
st.markdown(
    f"""
    <div class="slide-box">
        <h1 style="font-size: 80px; margin: 0;">{current['icon']}</h1>
        <p style="color: #60a5fa; font-weight: bold; letter-spacing: 2px; text-transform: uppercase; margin-top: 15px;">{current['tag']}</p>
        <h2 style="color: white; margin-top: 10px;">{current['title']}</h2>
        <p style="font-size: 20px; color: #9ca3af; margin-top: 15px;">{current['desc']}</p>
    </div>
""",
    unsafe_allow_html=True,
)

# Progress indicator
st.markdown(
    f"<p style='text-align: center; color: #6b7280; margin-top: 20px;'>Slide"
    f" {st.session_state.slide_index + 1} of {len(slides)}</p>",
    unsafe_allow_html=True,
)

# Auto-play loop logic if checked
if auto_play:
  time.sleep(4)
  st.session_state.slide_index = (st.session_state.slide_index + 1) % len(
      slides
  )
  st.rerun()
