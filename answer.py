mport streamlit as st
import pandas as pd

st.set_page_config(page_title="Submission Template", layout="wide")

st.title("📝 Assignment Submission")

# ==========================================
# Task 1
# ==========================================
st.header("Task 1: Build a stock dashboard with sidebar controls")


# Starter code
ticker_info = pd.read_csv("https://raw.githubusercontent.com/justinjiajia/datafiles/refs/heads/main/ticker_info.csv")

# extract S&P 100 tickers from ticker_info
ticker_list = list(ticker_info.Ticker.unique())

# Load the stock data
stock_data = pd.read_csv(
    "https://github.com/justinjiajia/datafiles/raw/refs/heads/main/stock_data_yf.csv", 
    parse_dates=['Date']
)

st.info("Write your Task 1 code below ...")

# --- STUDENT CODE AREA START ---

st.title("S&P 100 Stock Dashboard 📊")

# ---------- Sidebar controls ----------
show_market_cap = st.sidebar.checkbox("Show market cap by sector", value=True)

selected_tickers = st.sidebar.multiselect(
    "Select stocks",
    options=ticker_list,
    default=["TSLA", "NVDA", "AAPL"],
)

selected_years = st.sidebar.slider(
    "Select year range",
    min_value=2020,
    max_value=2025,
    value=(2024, 2025),
)

# ---------- Market cap chart ----------
if show_market_cap:
    st.subheader("Market Cap by Sector")
    st.bar_chart(
        ticker_info,
        x="Market Cap (B)",
        y="Sector",
        color="Ticker",
        horizontal=True,
    )

# ---------- Stock trend charts ----------
if len(selected_tickers) == 0:
    st.error("Please select at least one stock!")
else:
    filtered = stock_data.query(
        f"Date <= '{selected_years[1]}-12-31' and Date >= '{selected_years[0]}-01-01' "
        f"and Ticker in {selected_tickers}"
    )

    st.title(f"Stock Trend Analysis ({selected_years[0]} - {selected_years[1]})")

    st.subheader("Closing Prices")
    st.line_chart(filtered, x="Date", y="Close", color="Ticker")

    st.subheader("Trading Volume")
    st.bar_chart(filtered, x="Date", y="Volume", color="Ticker")

# --- STUDENT CODE AREA ---

st.divider()

# ==========================================
# Task 2
# ==========================================

st.header("Task 2: Display a video based on user input")

st.info("Write your Task 2 code below ...")

# --- STUDENT CODE AREA START ---

# 1. Initialize session state variables
if 'clicked' not in st.session_state:
    st.session_state.clicked = False
if 'url' not in st.session_state:
    st.session_state.url = ""

# 2. Render the input and button side-by-side
col1, col2 = st.columns([2, 1], vertical_alignment="bottom")

with col1:
    url = st.text_input(
        "Enter the URL of a video",
        value="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4",
    )

with col2:
    button = st.button("Submit")

# 3. Handle button click
if button:
    st.session_state.clicked = True
    st.session_state.url = url

# 4. Create the container for the video display
video_container = st.container(
    border=True, width=640, height=400, horizontal_alignment="center"
)

# 5. Display the video or the info message
if st.session_state.clicked:
    with video_container:
        video_url = st.session_state.url.strip()
        try:
            if not video_url.startswith(("http://", "https://")):
                raise ValueError("Invalid URL")
            st.video(video_url)
        except Exception:
            st.error("Invalid URL or the video cannot be loaded. Please check the URL and try again.")
else:
    video_container.info("Please enter a video URL and click Submit to display the video.")

# --- STUDENT CODE AREA END ---
