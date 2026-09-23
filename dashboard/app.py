import streamlit as st
import pandas as pd
import plotly.express as px
from textwrap import dedent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="RetailPulse",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background:
        radial-gradient(
            circle at top left,
            rgba(37, 99, 235, 0.12),
            transparent 35%
        ),
        radial-gradient(
            circle at top right,
            rgba(124, 58, 237, 0.12),
            transparent 35%
        ),
        #080b12;
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0f172a 0%,
        #111827 100%
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* Hero */

.hero {
    padding: 32px;
    border-radius: 22px;
    margin-bottom: 30px;

    background: linear-gradient(
        135deg,
        rgba(37, 99, 235, 0.25),
        rgba(124, 58, 237, 0.22)
    );

    border: 1px solid rgba(255,255,255,0.10);

    box-shadow:
        0 20px 50px rgba(0,0,0,0.30);
}

.hero-title {
    font-size: 40px;
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #60a5fa,
        #a78bfa,
        #f472b6
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-subtitle {
    margin-top: 8px;
    color: #cbd5e1;
    font-size: 16px;
}

/* KPI Cards */

.kpi-card {
    padding: 22px;
    border-radius: 18px;
    min-height: 120px;

    background: linear-gradient(
        145deg,
        rgba(30,41,59,0.95),
        rgba(15,23,42,0.95)
    );

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0 10px 30px rgba(0,0,0,0.25);
}

.kpi-label {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 8px;
}

.kpi-value {
    color: #f8fafc;
    font-size: 28px;
    font-weight: 750;
}

/* Section headers */

.section-header {
    margin-top: 32px;
    margin-bottom: 5px;

    font-size: 25px;
    font-weight: 750;

    color: #f8fafc;
}

.section-description {
    color: #94a3b8;
    font-size: 14px;
    margin-bottom: 18px;
}

/* Finding Cards */

.finding-card {
    padding: 18px;
    margin-bottom: 12px;

    border-radius: 16px;

    background: linear-gradient(
        135deg,
        rgba(30,41,59,0.95),
        rgba(15,23,42,0.95)
    );

    border: 1px solid rgba(255,255,255,0.08);
}

.finding-title {
    color: #94a3b8;
    font-size: 13px;
}

.finding-value {
    color: #f8fafc;
    font-size: 20px;
    font-weight: 700;
    margin-top: 4px;
}

/* Tabs */

button[data-baseweb="tab"] {
    font-size: 15px;
    font-weight: 600;
}

/* Hide Streamlit branding */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

sales_data = pd.read_csv(
    "data/processed/sales_features.csv"
)

sales_data["InvoiceDate"] = pd.to_datetime(
    sales_data["InvoiceDate"]
)


# ============================================================
# MONTH ORDER
# ============================================================

month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


# ============================================================
# HERO SECTION
# ============================================================

hero_html = dedent(
    """
    <div class="hero">
        <div class="hero-title">🛒 RetailPulse</div>
        <div class="hero-subtitle">
            Explore sales performance, customer behavior,
            product performance and geographic trends.
        </div>
    </div>
    """
)

st.markdown(
    hero_html,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown("## 🎛️ Dashboard Filters")

st.sidebar.caption(
    "Use the filters to explore different segments."
)


# Country filter

countries = sorted(
    sales_data["Country"]
    .dropna()
    .unique()
)

selected_countries = st.sidebar.multiselect(
    "🌍 Country",
    options=countries,
    default=countries
)


# Year filter

years = sorted(
    sales_data["Year"]
    .dropna()
    .unique()
)

selected_years = st.sidebar.multiselect(
    "📅 Year",
    options=years,
    default=years
)


st.sidebar.markdown("---")

st.sidebar.caption(
    f"Showing {len(selected_countries)} countries "
    f"across {len(selected_years)} years."
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_data = sales_data[
    sales_data["Country"].isin(selected_countries)
    &
    sales_data["Year"].isin(selected_years)
].copy()


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_revenue = filtered_data["Revenue"].sum()

total_orders = filtered_data["Invoice"].nunique()

total_quantity = filtered_data["Quantity"].sum()

if total_orders > 0:
    average_order_value = (
        total_revenue / total_orders
    )
else:
    average_order_value = 0


# ============================================================
# OVERALL PERFORMANCE
# ============================================================

st.markdown(
    '<div class="section-header">📊 Overall Performance</div>',
    unsafe_allow_html=True
)


kpi1, kpi2, kpi3, kpi4 = st.columns(4)


with kpi1:

    html = dedent(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">💰 Total Revenue</div>
            <div class="kpi-value">{total_revenue:,.2f}</div>
        </div>
        """
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


with kpi2:

    html = dedent(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">🧾 Total Orders</div>
            <div class="kpi-value">{total_orders:,}</div>
        </div>
        """
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


with kpi3:

    html = dedent(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">📦 Quantity Sold</div>
            <div class="kpi-value">{total_quantity:,}</div>
        </div>
        """
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


with kpi4:

    html = dedent(
        f"""
        <div class="kpi-card">
            <div class="kpi-label">🛍️ Average Order Value</div>
            <div class="kpi-value">{average_order_value:,.2f}</div>
        </div>
        """
    )

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# SALES TRENDS
# ============================================================

st.markdown(
    '<div class="section-header">📈 Sales Trends</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Track revenue, orders and average order value over time.'
    '</div>',
    unsafe_allow_html=True
)


# Monthly revenue

monthly_revenue = (
    filtered_data
    .groupby(
        ["Year", "Month", "Month_Name"]
    )["Revenue"]
    .sum()
    .reset_index()
    .sort_values(["Year", "Month"])
)


# Monthly orders

monthly_orders = (
    filtered_data
    .groupby(
        ["Year", "Month", "Month_Name"]
    )["Invoice"]
    .nunique()
    .reset_index(name="Total_Orders")
    .sort_values(["Year", "Month"])
)


# Monthly AOV

monthly_aov = monthly_revenue.merge(
    monthly_orders,
    on=["Year", "Month", "Month_Name"]
)

monthly_aov["AOV"] = (
    monthly_aov["Revenue"]
    / monthly_aov["Total_Orders"]
)


# Month ordering

for dataframe in [
    monthly_revenue,
    monthly_orders,
    monthly_aov
]:

    dataframe["Month_Name"] = pd.Categorical(
        dataframe["Month_Name"],
        categories=month_order,
        ordered=True
    )


# Revenue chart

revenue_chart = px.line(
    monthly_revenue,
    x="Month_Name",
    y="Revenue",
    color="Year",
    markers=True
)

revenue_chart.update_layout(
    title="Monthly Revenue",
    xaxis_title="",
    yaxis_title="Revenue",
    template="plotly_dark",
    hovermode="x unified"
)


# Orders chart

orders_chart = px.line(
    monthly_orders,
    x="Month_Name",
    y="Total_Orders",
    color="Year",
    markers=True
)

orders_chart.update_layout(
    title="Monthly Orders",
    xaxis_title="",
    yaxis_title="Orders",
    template="plotly_dark",
    hovermode="x unified"
)


trend_col1, trend_col2 = st.columns(2)


with trend_col1:

    st.plotly_chart(
        revenue_chart,
        use_container_width=True
    )


with trend_col2:

    st.plotly_chart(
        orders_chart,
        use_container_width=True
    )


# AOV chart

aov_chart = px.line(
    monthly_aov,
    x="Month_Name",
    y="AOV",
    color="Year",
    markers=True
)

aov_chart.update_layout(
    title="Monthly Average Order Value",
    xaxis_title="",
    yaxis_title="AOV",
    template="plotly_dark",
    hovermode="x unified"
)

st.plotly_chart(
    aov_chart,
    use_container_width=True
)


# ============================================================
# PRODUCT PERFORMANCE
# ============================================================

st.markdown(
    '<div class="section-header">📦 Product Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Compare products by revenue, quantity and sales volume.'
    '</div>',
    unsafe_allow_html=True
)


product_data = (
    filtered_data
    .groupby("StockCode")
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Quantity=("Quantity", "sum"),
        Total_Orders=("Invoice", "nunique")
    )
    .reset_index()
)


top_products_revenue = (
    product_data
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
    .head(10)
)


top_products_quantity = (
    product_data
    .sort_values(
        "Total_Quantity",
        ascending=False
    )
    .head(10)
)


product_tab1, product_tab2 = st.tabs(
    ["💰 Revenue", "📦 Quantity"]
)


with product_tab1:

    chart = px.bar(
        top_products_revenue,
        x="Total_Revenue",
        y="StockCode",
        orientation="h",
        text="Total_Revenue"
    )

    chart.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    chart.update_layout(
        title="Top 10 Products by Revenue",
        template="plotly_dark",
        xaxis_title="Revenue",
        yaxis_title="Product"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )


with product_tab2:

    chart = px.bar(
        top_products_quantity,
        x="Total_Quantity",
        y="StockCode",
        orientation="h",
        text="Total_Quantity"
    )

    chart.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    chart.update_layout(
        title="Top 10 Products by Quantity",
        template="plotly_dark",
        xaxis_title="Quantity",
        yaxis_title="Product"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )


# Revenue vs quantity

product_scatter = px.scatter(
    product_data,
    x="Total_Quantity",
    y="Total_Revenue",
    size="Total_Orders",
    hover_data=[
        "StockCode",
        "Total_Orders"
    ]
)

product_scatter.update_layout(
    title="Revenue vs Quantity by Product",
    template="plotly_dark",
    xaxis_title="Quantity Sold",
    yaxis_title="Revenue"
)

st.plotly_chart(
    product_scatter,
    use_container_width=True
)


# ============================================================
# CUSTOMER PERFORMANCE
# ============================================================

st.markdown(
    '<div class="section-header">👥 Customer Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Understand high-value customers and purchasing frequency.'
    '</div>',
    unsafe_allow_html=True
)


customer_data = (
    filtered_data
    .groupby("Customer ID")
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Orders=("Invoice", "nunique"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
    .dropna(subset=["Customer ID"])
)


top_customers_revenue = (
    customer_data
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
    .head(10)
)


top_customers_orders = (
    customer_data
    .sort_values(
        "Total_Orders",
        ascending=False
    )
    .head(10)
)


customer_tab1, customer_tab2 = st.tabs(
    ["💰 Revenue", "🛍️ Orders"]
)


with customer_tab1:

    chart = px.bar(
        top_customers_revenue,
        x="Total_Revenue",
        y="Customer ID",
        orientation="h",
        text="Total_Revenue"
    )

    chart.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    chart.update_layout(
        title="Top 10 Customers by Revenue",
        template="plotly_dark",
        xaxis_title="Revenue",
        yaxis_title="Customer"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )


with customer_tab2:

    chart = px.bar(
        top_customers_orders,
        x="Total_Orders",
        y="Customer ID",
        orientation="h",
        text="Total_Orders"
    )

    chart.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    chart.update_layout(
        title="Top 10 Customers by Orders",
        template="plotly_dark",
        xaxis_title="Orders",
        yaxis_title="Customer"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )


# Repeat customer rate

repeat_customers = customer_data[
    customer_data["Total_Orders"] > 1
]

total_customers = len(customer_data)

if total_customers > 0:

    repeat_customer_rate = (
        len(repeat_customers)
        / total_customers
    ) * 100

else:

    repeat_customer_rate = 0


html = dedent(
    f"""
    <div class="kpi-card">
        <div class="kpi-label">🔁 Repeat Customer Rate</div>
        <div class="kpi-value">{repeat_customer_rate:.2f}%</div>
    </div>
    """
)

st.markdown(
    html,
    unsafe_allow_html=True
)


# ============================================================
# GEOGRAPHIC PERFORMANCE
# ============================================================

st.markdown(
    '<div class="section-header">🌍 Geographic Performance</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'Explore the countries contributing most to revenue and orders.'
    '</div>',
    unsafe_allow_html=True
)


country_data = (
    filtered_data
    .groupby("Country")
    .agg(
        Total_Revenue=("Revenue", "sum"),
        Total_Orders=("Invoice", "nunique"),
        Total_Quantity=("Quantity", "sum")
    )
    .reset_index()
)


top_countries_revenue = (
    country_data
    .sort_values(
        "Total_Revenue",
        ascending=False
    )
    .head(10)
)


top_countries_orders = (
    country_data
    .sort_values(
        "Total_Orders",
        ascending=False
    )
    .head(10)
)


country_tab1, country_tab2 = st.tabs(
    ["💰 Revenue", "🧾 Orders"]
)


with country_tab1:

    chart = px.bar(
        top_countries_revenue,
        x="Total_Revenue",
        y="Country",
        orientation="h",
        text="Total_Revenue"
    )

    chart.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    chart.update_layout(
        title="Top 10 Countries by Revenue",
        template="plotly_dark",
        xaxis_title="Revenue",
        yaxis_title="Country"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )


with country_tab2:

    chart = px.bar(
        top_countries_orders,
        x="Total_Orders",
        y="Country",
        orientation="h",
        text="Total_Orders"
    )

    chart.update_traces(
        texttemplate="%{text:,.0f}",
        textposition="outside"
    )

    chart.update_layout(
        title="Top 10 Countries by Orders",
        template="plotly_dark",
        xaxis_title="Orders",
        yaxis_title="Country"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

# ============================================================
# KEY FINDINGS
# ============================================================

st.markdown(
    '<div class="section-header">💡 Key Findings</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">'
    'These findings update automatically when filters change.'
    '</div>',
    unsafe_allow_html=True
)


# Highest revenue product
if not product_data.empty:

    highest_revenue_product = (
        product_data
        .sort_values(
            "Total_Revenue",
            ascending=False
        )
        .iloc[0]
    )

    highest_quantity_product = (
        product_data
        .sort_values(
            "Total_Quantity",
            ascending=False
        )
        .iloc[0]
    )

else:

    highest_revenue_product = None
    highest_quantity_product = None


# Highest revenue customer
if not customer_data.empty:

    highest_revenue_customer = (
        customer_data
        .sort_values(
            "Total_Revenue",
            ascending=False
        )
        .iloc[0]
    )

    highest_order_customer = (
        customer_data
        .sort_values(
            "Total_Orders",
            ascending=False
        )
        .iloc[0]
    )

else:

    highest_revenue_customer = None
    highest_order_customer = None


# Highest revenue country
if not country_data.empty:

    highest_revenue_country = (
        country_data
        .sort_values(
            "Total_Revenue",
            ascending=False
        )
        .iloc[0]
    )

else:

    highest_revenue_country = None


# ============================================================
# FINDING CARDS
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    st.metric(
        "💰 Highest Revenue Product",
        highest_revenue_product["StockCode"]
        if highest_revenue_product is not None
        else "N/A",
        f"Revenue: {highest_revenue_product['Total_Revenue']:,.2f}"
        if highest_revenue_product is not None
        else None
    )


with col2:

    st.metric(
        "📦 Highest Volume Product",
        highest_quantity_product["StockCode"]
        if highest_quantity_product is not None
        else "N/A",
        f"Units: {highest_quantity_product['Total_Quantity']:,.0f}"
        if highest_quantity_product is not None
        else None
    )


with col3:

    st.metric(
        "🌍 Highest Revenue Country",
        highest_revenue_country["Country"]
        if highest_revenue_country is not None
        else "N/A",
        f"Revenue: {highest_revenue_country['Total_Revenue']:,.2f}"
        if highest_revenue_country is not None
        else None
    )


col4, col5, col6 = st.columns(3)


with col4:

    st.metric(
        "👤 Highest Revenue Customer",
        int(highest_revenue_customer["Customer ID"])
        if highest_revenue_customer is not None
        else "N/A",
        f"Revenue: {highest_revenue_customer['Total_Revenue']:,.2f}"
        if highest_revenue_customer is not None
        else None
    )


with col5:

    st.metric(
        "🛍️ Highest Order Customer",
        int(highest_order_customer["Customer ID"])
        if highest_order_customer is not None
        else "N/A",
        f"Orders: {highest_order_customer['Total_Orders']:,.0f}"
        if highest_order_customer is not None
        else None
    )


with col6:

    st.metric(
        "🔁 Repeat Customer Rate",
        f"{repeat_customer_rate:.2f}%"
    )

# ============================================================
# DATA PREVIEW
# ============================================================

with st.expander("🔎 View Filtered Transaction Data"):

    st.dataframe(
        filtered_data.head(100),
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

footer_html = dedent(
    """
    <div style="
        text-align:center;
        color:#64748b;
        padding:30px;
        font-size:13px;
    ">
        E-Commerce Sales & Customer Analytics
        <br>
        Built with Python • Pandas • Plotly • Streamlit
    </div>
    """
)

st.markdown(
    footer_html,
    unsafe_allow_html=True
)