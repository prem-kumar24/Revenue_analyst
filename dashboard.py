"""
Sales & Revenue Dashboard using Streamlit and Plotly
A comprehensive analytics dashboard with KPIs, charts, and interactive filters.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import calendar


# ============================================================================
# PAGE CONFIGURATION & STYLING
# ============================================================================

st.set_page_config(
    page_title="Sales & Revenue Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main background color */
    .main {
        background-color: #f8f9fa;
    }
    
    /* KPI Card styling */
    .kpi-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .kpi-value {
        font-size: 28px;
        font-weight: bold;
        color: #1f77b4;
        margin: 10px 0;
    }
    
    .kpi-label {
        font-size: 14px;
        color: #666;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Chart containers */
    .chart-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    
    /* Title styling */
    .dashboard-title {
        color: #1f77b4;
        text-align: center;
        margin-bottom: 10px;
    }
    
    .dashboard-subtitle {
        color: #666;
        text-align: center;
        margin-bottom: 30px;
    }
    
    /* Sidebar styling */
    .sidebar-title {
        font-size: 18px;
        font-weight: bold;
        color: #1f77b4;
        margin-top: 20px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================================
# DATA GENERATION FUNCTION
# ============================================================================

@st.cache_data
def generate_sample_data():
    """
    Generate 6 months of sample sales data.
    Returns a pandas DataFrame with sales information.
    """
    # Define parameters
    start_date = datetime.now() - timedelta(days=180)
    dates = pd.date_range(start=start_date, end=datetime.now(), freq='D')
    
    products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor', 
                'Keyboard', 'Mouse', 'Webcam', 'Router', 'Charger']
    categories = ['Electronics', 'Accessories', 'Peripherals', 'Mobile']
    regions = ['North', 'South', 'East', 'West']
    
    # Product to category mapping
    product_category = {
        'Laptop': 'Electronics',
        'Smartphone': 'Mobile',
        'Tablet': 'Mobile',
        'Headphones': 'Accessories',
        'Monitor': 'Electronics',
        'Keyboard': 'Peripherals',
        'Mouse': 'Peripherals',
        'Webcam': 'Peripherals',
        'Router': 'Electronics',
        'Charger': 'Accessories'
    }
    
    # Product base prices (for realistic revenue generation)
    product_prices = {
        'Laptop': 1000,
        'Smartphone': 800,
        'Tablet': 600,
        'Headphones': 200,
        'Monitor': 400,
        'Keyboard': 100,
        'Mouse': 50,
        'Webcam': 80,
        'Router': 150,
        'Charger': 30
    }
    
    # Generate random transactions
    np.random.seed(42)
    data = []
    
    for _ in range(500):  # 500 transactions
        date = np.random.choice(dates)
        product = np.random.choice(products)
        category = product_category[product]
        region = np.random.choice(regions)
        
        # Generate amount with some variation around base price
        base_price = product_prices[product]
        quantity = np.random.randint(1, 5)
        variation = np.random.uniform(0.8, 1.2)  # ±20% variation
        amount = base_price * quantity * variation
        
        data.append({
            'Date': date,
            'Product': product,
            'Category': category,
            'Amount': round(amount, 2),
            'Region': region
        })
    
    df = pd.DataFrame(data)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date').reset_index(drop=True)
    
    return df


# ============================================================================
# KPI CALCULATION FUNCTIONS
# ============================================================================

def calculate_kpis(df):
    """Calculate key performance indicators from the data."""
    total_revenue = df['Amount'].sum()
    total_transactions = len(df)
    average_order_value = df['Amount'].mean()
    top_region = df.groupby('Region')['Amount'].sum().idxmax()
    
    return {
        'total_revenue': total_revenue,
        'total_transactions': total_transactions,
        'average_order_value': average_order_value,
        'top_region': top_region
    }


def format_currency(value):
    """Format value as currency with comma separator."""
    return f"${value:,.2f}"


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def create_revenue_trend_chart(df):
    """
    Create a line chart showing revenue trends over time (month-over-month).
    """
    # Group by month and sum revenue
    df['YearMonth'] = df['Date'].dt.to_period('M')
    monthly_revenue = df.groupby('YearMonth')['Amount'].sum().reset_index()
    monthly_revenue['YearMonth'] = monthly_revenue['YearMonth'].astype(str)
    
    fig = px.line(
        monthly_revenue,
        x='YearMonth',
        y='Amount',
        title='Revenue Trend (Month-over-Month)',
        labels={'YearMonth': 'Month', 'Amount': 'Revenue ($)'},
        markers=True,
        line_shape='spline'
    )
    
    fig.update_traces(
        line=dict(color='#1f77b4', width=3),
        marker=dict(size=8)
    )
    
    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='rgba(240, 240, 240, 0.5)',
        height=400,
        font=dict(size=12)
    )
    
    return fig


def create_category_chart(df):
    """
    Create a bar chart showing sales revenue by category.
    """
    category_sales = df.groupby('Category')['Amount'].sum().reset_index()
    category_sales = category_sales.sort_values('Amount', ascending=False)
    
    fig = px.bar(
        category_sales,
        x='Category',
        y='Amount',
        title='Sales Revenue by Category',
        labels={'Category': 'Category', 'Amount': 'Revenue ($)'},
        color='Amount',
        color_continuous_scale='Blues'
    )
    
    fig.update_layout(
        hovermode='x unified',
        plot_bgcolor='rgba(240, 240, 240, 0.5)',
        height=400,
        showlegend=False,
        font=dict(size=12)
    )
    
    fig.update_yaxes(title_text='Revenue ($)')
    
    return fig


def create_region_pie_chart(df):
    """
    Create a pie chart showing revenue distribution by region.
    """
    region_revenue = df.groupby('Region')['Amount'].sum().reset_index()
    region_revenue = region_revenue.sort_values('Amount', ascending=False)
    
    fig = px.pie(
        region_revenue,
        values='Amount',
        names='Region',
        title='Revenue Distribution by Region',
        color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    )
    
    fig.update_traces(
        textposition='inside',
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Revenue: $%{value:,.2f}<br>Percentage: %{percent}<extra></extra>'
    )
    
    fig.update_layout(
        height=400,
        font=dict(size=12)
    )
    
    return fig


def create_top_products_chart(df):
    """
    Create a horizontal bar chart showing top 5 products by revenue.
    """
    product_revenue = df.groupby('Product')['Amount'].sum().reset_index()
    product_revenue = product_revenue.sort_values('Amount', ascending=True).tail(5)
    
    fig = px.bar(
    product_revenue,
    x='Amount',
    y='Product',
    title='Top 5 Products by Revenue',
    labels={'Product': 'Product', 'Amount': 'Revenue ($)'},
    color='Amount',
    color_continuous_scale='Greens',
    orientation='h'   # 👈 yeh add karo
)
    
    fig.update_layout(
        hovermode='y unified',
        plot_bgcolor='rgba(240, 240, 240, 0.5)',
        height=400,
        showlegend=False,
        font=dict(size=12)
    )
    
    fig.update_xaxes(title_text='Revenue ($)')
    fig.update_yaxes(title_text='')
    
    return fig


# ============================================================================
# MAIN APPLICATION
# ============================================================================

def main():
    """Main application entry point."""
    
    # Load data
    df = generate_sample_data()
    
    # Dashboard Header
    st.markdown('<div class="dashboard-title"><h1>📊 Sales & Revenue Dashboard</h1></div>', 
                unsafe_allow_html=True)
    st.markdown('<div class="dashboard-subtitle">Real-time analytics and insights for your business</div>', 
                unsafe_allow_html=True)
    
    # ========================================================================
    # SIDEBAR FILTERS
    # ========================================================================
    
    st.sidebar.markdown('<div class="sidebar-title">🔍 Filters</div>', 
                       unsafe_allow_html=True)
    
    # Date range slider
    date_range = st.sidebar.slider(
        "Select Date Range",
        min_value=df['Date'].min().date(),
        max_value=df['Date'].max().date(),
        value=(df['Date'].min().date(), df['Date'].max().date()),
        format="YYYY-MM-DD"
    )
    
    # Filter data by date range
    filtered_df = df[(df['Date'].dt.date >= date_range[0]) & 
                     (df['Date'].dt.date <= date_range[1])]
    
    # Category filter
    all_categories = ['All Categories'] + sorted(df['Category'].unique().tolist())
    selected_category = st.sidebar.selectbox(
        "Filter by Category",
        all_categories
    )
    
    if selected_category != 'All Categories':
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]
    
    # Region filter
    all_regions = ['All Regions'] + sorted(df['Region'].unique().tolist())
    selected_region = st.sidebar.selectbox(
        "Filter by Region",
        all_regions
    )
    
    if selected_region != 'All Regions':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    
    # Apply filters info
    st.sidebar.markdown("---")
    st.sidebar.info(
        f"📈 **Active Filters**\n\n"
        f"Date Range: {date_range[0]} to {date_range[1]}\n\n"
        f"Transactions shown: {len(filtered_df):,}"
    )
    
    # ========================================================================
    # KPI CARDS
    # ========================================================================
    
    kpis = calculate_kpis(filtered_df)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Total Revenue</div>
                <div class="kpi-value">{format_currency(kpis['total_revenue'])}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Total Transactions</div>
                <div class="kpi-value">{kpis['total_transactions']:,}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Average Order Value</div>
                <div class="kpi-value">{format_currency(kpis['average_order_value'])}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-label">Top Region</div>
                <div class="kpi-value">{kpis['top_region']}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    st.markdown("---")
    
    # ========================================================================
    # CHARTS - ROW 1
    # ========================================================================
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_revenue_trend_chart(filtered_df), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_category_chart(filtered_df), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ========================================================================
    # CHARTS - ROW 2
    # ========================================================================
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_region_pie_chart(filtered_df), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.plotly_chart(create_top_products_chart(filtered_df), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ========================================================================
    # DETAILED DATA TABLE
    # ========================================================================
    
    st.markdown("---")
    st.markdown("### 📋 Detailed Sales Data")
    
    # Show sample of data
    display_df = filtered_df.copy()
    display_df['Date'] = display_df['Date'].dt.strftime('%Y-%m-%d')
    display_df['Amount'] = display_df['Amount'].apply(lambda x: f"${x:,.2f}")
    
    st.dataframe(
        display_df,
        use_container_width=True,
        height=300
    )
    
    # Download data button
    csv = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Download CSV",
        data=csv,
        file_name=f"sales_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )
    
    # ========================================================================
    # FOOTER
    # ========================================================================
    
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #999; font-size: 12px; padding: 20px;">
            Sales & Revenue Dashboard | Data last updated: """ + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + """ | 
            Built with Streamlit & Plotly
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
