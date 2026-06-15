import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io

# 1. Page Configuration (Setting a clean layout and title)
st.set_page_config(page_title="Executive Sales Intelligence", page_icon="📈", layout="wide")

# Custom CSS styling to make the app look like an expensive premium SaaS platform
st.markdown("""
    <style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    h1 {color: #1E3A8A; font-weight: 800;}
    h3 {color: #1F2937; font-weight: 600;}
    div[data-testid="stMetricValue"] {font-size: 2.2rem; font-weight: 700; color: #0284C7;}
    </style>
""", unsafe_allow_html=True)

st.title("📊 Executive Sales Intelligence Platform")
st.write("Transforming raw operational ledgers into multi-dimensional enterprise analytics panels.")

# --- SIDEBAR: DATA INGESTION & ADVANCED CONTROL PANEL ---
st.sidebar.header("🕹️ Control Panel")
uploaded_file = st.sidebar.file_uploader("Upload Transaction Ledger (CSV or XLSX)", type=["xlsx", "csv"])

# --- DATA SEED ENGINE (FALLBACK DATA) ---
if uploaded_file is None:
    st.info(
        "💡 Displaying operational sample pipeline. Ingest custom files via the control panel sidebar to compile real-time models.")
    data = {
        "order_id": [101, 102, 103, 104, 105, 106, 107],
        "product_name": ["Mouse", "Keyboard", "Notebook", "Pen", "Monitor", "Bag", "Printer"],
        "category": ["IT", "IT", "Stationery", "Stationery", "IT", "Stationery", "IT"],
        "quantity": [3, 2, 5, 10, 1, 4, 2],
        "price_each": [500, 1200, 50, 10, 7000, 600, 5000],
        "order_date": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-20", "2024-02-01", "2024-02-05",
                       "2024-02-10"],
        "region": ["East", "West", "North", "East", "South", "North", "West"]
    }
    df = pd.DataFrame(data)
    df["order_date"] = pd.to_datetime(df["order_date"])
else:
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"])

# Calculate base feature columns
df["sales_amount"] = df["quantity"] * df["price_each"]

# --- ADVANCED ADDITION: DYNAMIC INTERACTIVE SIDEBAR FILTERS ---
st.sidebar.divider()
st.sidebar.subheader("🎯 Data Segmentation Filters")
categories = ["All Categories"] + list(df["category"].unique())
selected_category = st.sidebar.selectbox("Filter Segment by Category:", categories)

regions = ["All Regions"] + list(df["region"].unique())
selected_region = st.sidebar.selectbox("Filter Segment by Region:", regions)

# Mutate and slice dataset based on user dashboard interaction
filtered_df = df.copy()
if selected_category != "All Categories":
    filtered_df = filtered_df[filtered_df["category"] == selected_category]
if selected_region != "All Regions":
    filtered_df = filtered_df[filtered_df["region"] == selected_region]

# --- EXECUTIVE SUMMARY METRICS PANEL ---
total_sales = filtered_df["sales_amount"].sum()
total_orders = filtered_df["order_id"].nunique()
total_items = filtered_df["quantity"].sum()
avg_order_value = total_sales / total_orders if total_orders > 0 else 0

m1, m2, m3, m4 = st.columns(4)
m1.metric(label="💰 Gross Revenue", value=f"₹{total_sales:,}")
m2.metric(label="📦 Volume Processed", value=f"{total_orders:,} Orders")
m3.metric(label="🛒 Units Distributed", value=f"{total_items:,} SKUs")
m4.metric(label="📊 Avg Ticket Size (AOV)", value=f"₹{round(avg_order_value, 2):,}")

st.divider()

# --- GRAPHICAL PLOT GRID (PLOTLY ADVANCED UPGRADE) ---
col_graph1, col_graph2 = st.columns(2)

with col_graph1:
    st.subheader("🗺️ Geographical Revenue Distribution")
    region_data = filtered_df.groupby("region")["sales_amount"].sum().reset_index()

    # Advanced Plotly Donut Chart
    fig_pie = px.pie(
        region_data,
        values='sales_amount',
        names='region',
        hole=0.5,
        color_discrete_sequence=px.colors.sequential.RdBu,
        template="plotly_white"
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=320)
    st.plotly_chart(fig_pie, use_container_width=True)

with col_graph2:
    st.subheader("🏆 SKU Velocity Matrix (Top Products)")
    product_data = filtered_df.groupby("product_name")["sales_amount"].sum().reset_index().sort_values(
        by="sales_amount", ascending=True).head(5)

    # Advanced Plotly Horizontal Bar Chart for better scanning
    fig_bar = px.bar(
        product_data,
        x='sales_amount',
        y='product_name',
        orientation='h',
        labels={'sales_amount': 'Gross Sales (₹)', 'product_name': 'Product Description'},
        template="plotly_white",
        color='sales_amount',
        color_continuous_scale=px.colors.sequential.Viridis
    )
    fig_bar.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=320, coloraxis_showscale=False)
    st.plotly_chart(fig_bar, use_container_width=True)

# --- TIME-SERIES TIMELINE TREND ANALYSIS ---
st.subheader("📈 Chronological Sales Run Rate")
filtered_df["month"] = filtered_df["order_date"].dt.to_period("M").astype(str)
timeline_data = filtered_df.groupby("month")["sales_amount"].sum().reset_index()

# Advanced Plotly Area Trend Spline Chart
fig_line = px.area(
    timeline_data,
    x='month',
    y='sales_amount',
    labels={'sales_amount': 'Monthly Income (₹)', 'month': 'Accounting Period'},
    template="plotly_white",
    markers=True
)
fig_line.update_traces(line_shape='spline', line_color='#0284C7', fillcolor='rgba(2, 132, 199, 0.15)')
fig_line.update_layout(height=350, margin=dict(t=20, b=20, l=10, r=10))
st.plotly_chart(fig_line, use_container_width=True)

st.divider()

# --- REPORT GENERATION ENGINE ---
st.subheader("📋 Audit Matrix Explorer")
st.dataframe(filtered_df.drop(columns=['month']), use_container_width=True)

# Compiling targeted in-memory binaries for export routines
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name="Master Raw Ledger", index=False)
    filtered_df.to_excel(writer, sheet_name="Filtered Scope Audit", index=False)
    if not filtered_df.empty:
        region_data.to_excel(writer, sheet_name="Regional Summary", index=False)
        product_data.to_excel(writer, sheet_name="Product Matrix Analysis", index=False)

st.sidebar.divider()
st.sidebar.subheader("💾 Export Hub")
st.sidebar.download_button(
    label="🟢 Download Multi-Sheet Audit Report",
    data=buffer.getvalue(),
    file_name="sales_corporate_intelligence.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    use_container_width=True
)