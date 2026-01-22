# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="YouTube Analytics | Canada",
#     page_icon="📊",
#     layout="wide"
# )

# # ---------------- CUSTOM DARK CSS ----------------
# st.markdown("""
# <style>
#     body {
#         background-color: #0e1117;
#         color: #fafafa;
#     }
#     .metric-card {
#         background: #161b22;
#         padding: 20px;
#         border-radius: 14px;
#         text-align: center;
#         box-shadow: 0 4px 20px rgba(0,0,0,0.4);
#     }
#     .metric-value {
#         font-size: 32px;
#         font-weight: bold;
#         color: #58a6ff;
#     }
#     .metric-label {
#         font-size: 14px;
#         color: #8b949e;
#     }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- TITLE ----------------
# st.markdown("## 📊 YouTube Trending Analytics – Canada")
# st.markdown(
#     "<span style='color:#8b949e'>Professional dashboard built with Streamlit & AI</span>",
#     unsafe_allow_html=True
# )

# # ---------------- LOAD DATA ----------------
# @st.cache_data
# def load_data():
#     return pd.read_csv("CAvideos.csv")

# df = load_data()

# # ---------------- SIDEBAR ----------------
# st.sidebar.title("⚙️ Controls")

# top_n = st.sidebar.slider(
#     "Top N Records",
#     5, 20, 10
# )

# sample_size = st.sidebar.slider(
#     "Scatter Sample Size",
#     500, 3000, 1200
# )

# st.sidebar.markdown("---")
# st.sidebar.caption("Dataset: Kaggle – YouTube Trending Videos")

# # ---------------- KPI CARDS ----------------
# c1, c2, c3, c4 = st.columns(4)

# def metric_card(col, label, value):
#     col.markdown(f"""
#     <div class="metric-card">
#         <div class="metric-value">{value}</div>
#         <div class="metric-label">{label}</div>
#     </div>
#     """, unsafe_allow_html=True)

# metric_card(c1, "Total Videos", f"{len(df):,}")
# metric_card(c2, "Total Views", f"{df['views'].sum():,}")
# metric_card(c3, "Avg Likes", f"{int(df['likes'].mean()):,}")
# metric_card(c4, "Avg Comments", f"{int(df['comment_count'].mean()):,}")

# st.markdown("---")

# # ---------------- TOP CHANNELS ----------------
# channel_views = (
#     df.groupby("channel_title")["views"]
#     .sum()
#     .sort_values(ascending=False)
#     .head(top_n)
#     .reset_index()
# )

# fig_channels = px.bar(
#     channel_views,
#     x="views",
#     y="channel_title",
#     orientation="h",
#     title="🔥 Top Channels by Total Views",
#     template="plotly_dark",
#     color="views",
#     color_continuous_scale="blues"
# )

# st.plotly_chart(fig_channels, use_container_width=True)

# # ---------------- TOP VIDEOS ----------------
# top_videos = df.sort_values("views", ascending=False).head(top_n)

# fig_videos = px.bar(
#     top_videos,
#     x="views",
#     y="title",
#     orientation="h",
#     title="🎬 Top Trending Videos by Views",
#     template="plotly_dark",
#     color="views",
#     color_continuous_scale="viridis"
# )

# st.plotly_chart(fig_videos, use_container_width=True)

# # ---------------- SCATTER ANALYSIS ----------------
# fig_scatter = px.scatter(
#     df.sample(sample_size, random_state=42),
#     x="views",
#     y="likes",
#     size="comment_count",
#     hover_name="title",
#     title="📈 Views vs Likes Relationship",
#     template="plotly_dark",
# )

# st.plotly_chart(fig_scatter, use_container_width=True)

# # ---------------- DATA PREVIEW ----------------
# with st.expander("📂 Preview Dataset"):
#     st.dataframe(df.head(100), use_container_width=True)

# # ---------------- FOOTER ----------------
# st.markdown(
#     "<center style='color:#8b949e'>Built with ❤️ using Streamlit & AI</center>",
#     unsafe_allow_html=True
# )




import streamlit as st
import pandas as pd
import plotly.express as px

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="YouTube Trending Analytics | Canada",
    page_icon="📊",
    layout="wide"
)

# ---------------- DARK THEME CSS ----------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #fafafa;
}
.metric-box {
    background: #161b22;
    padding: 20px;
    border-radius: 14px;
    text-align: center;
    box-shadow: 0 6px 25px rgba(0,0,0,0.4);
}
.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #58a6ff;
}
.metric-label {
    font-size: 13px;
    color: #8b949e;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("## 📊 YouTube Trending Dashboard – Canada")
st.markdown(
    "<span style='color:#8b949e'>AI-powered professional data analytics</span>",
    unsafe_allow_html=True
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    return pd.read_csv("CAvideos_small.csv")

df = load_data()

# ---------------- DATA CLEANING ----------------
df["comment_count"] = df["comment_count"].fillna(0)
df["likes"] = df["likes"].fillna(0)
df["views"] = df["views"].fillna(0)

# Negative ya zero size avoid karne ke liye
df = df[df["comment_count"] >= 0]


# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Filters")

top_n = st.sidebar.slider("Top Channels / Videos", 5, 20, 10)
sample_size = st.sidebar.slider("Scatter Sample Size", 300, 3000, 1200)

st.sidebar.markdown("---")
st.sidebar.caption("Dataset: Kaggle – YouTube Trending Videos (Canada)")

# ---------------- KPI METRICS ----------------
c1, c2, c3, c4 = st.columns(4)

def metric(col, label, value):
    col.markdown(f"""
    <div class="metric-box">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """, unsafe_allow_html=True)

metric(c1, "Total Videos", f"{len(df):,}")
metric(c2, "Total Views", f"{df['views'].sum():,}")
metric(c3, "Average Likes", f"{int(df['likes'].mean()):,}")
metric(c4, "Average Comments", f"{int(df['comment_count'].mean()):,}")

st.markdown("---")

# ---------------- TOP CHANNELS ----------------
top_channels = (
    df.groupby("channel_title")["views"]
    .sum()
    .sort_values(ascending=False)
    .head(top_n)
    .reset_index()
)

fig_channels = px.bar(
    top_channels,
    x="views",
    y="channel_title",
    orientation="h",
    title="🔥 Top YouTube Channels by Views",
    template="plotly_dark",
    color="views",
    color_continuous_scale="blues"
)

st.plotly_chart(fig_channels, use_container_width=True)

# ---------------- TOP VIDEOS ----------------
top_videos = df.sort_values("views", ascending=False).head(top_n)

fig_videos = px.bar(
    top_videos,
    x="views",
    y="title",
    orientation="h",
    title="🎬 Most Viewed Trending Videos",
    template="plotly_dark",
    color="views",
    color_continuous_scale="viridis"
)

st.plotly_chart(fig_videos, use_container_width=True)

# ---------------- SCATTER PLOT ----------------
fig_scatter = px.scatter(
    df.sample(sample_size, random_state=42),
    x="views",
    y="likes",
    size="comment_count",
    hover_name="title",
    title="📈 Views vs Likes Relationship",
    template="plotly_dark"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# ---------------- DATA PREVIEW ----------------
with st.expander("📂 View Dataset Sample"):
    st.dataframe(df.head(100), use_container_width=True)

# ---------------- FOOTER ----------------
st.markdown(
    "<center style='color:#8b949e'>Built with Streamlit • Python • AI</center>",
    unsafe_allow_html=True
)
