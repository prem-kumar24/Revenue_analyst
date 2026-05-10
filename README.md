# Sales & Revenue Dashboard

A professional, interactive dashboard built with Streamlit and Plotly for analyzing sales and revenue data in real-time.

## Features

### 📊 KPI Cards
- **Total Revenue** - Sum of all sales transactions (formatted with commas)
- **Total Transactions** - Count of all transactions
- **Average Order Value** - Mean transaction value
- **Top Region by Revenue** - Best performing region

### 📈 Interactive Charts
1. **Revenue Trend Chart** - Line chart showing revenue trends over the last 6 months (month-over-month comparison)
2. **Category Sales Chart** - Bar chart displaying total revenue by product category
3. **Regional Distribution** - Pie chart showing revenue split across regions
4. **Top 5 Products** - Horizontal bar chart of best-performing products

### 🔍 Interactive Filters
- **Date Range Slider** - Filter data by custom date ranges
- **Category Dropdown** - Filter by product category (Electronics, Accessories, etc.)
- **Region Dropdown** - Filter by sales region (North, South, East, West)

### 🎨 Styling
- Professional color scheme with blue tones
- Responsive design that works on any screen size
- Clean card-based layout with shadows and rounded corners
- Custom CSS for enhanced visual appeal

### 📥 Data Export
- Download filtered data as CSV for further analysis

## Installation

### 1. Install Python (if not already installed)
- Download from [python.org](https://www.python.org/downloads/)
- Make sure to check "Add Python to PATH" during installation

### 2. Clone or Download the Project
```bash
cd path/to/your/project
```

### 3. Create a Virtual Environment (Recommended)

**On Windows (PowerShell):**
```powershell
python -m venv venv
venv\Scripts\Activate
```

**On Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Dashboard

### Option 1: Using Command Line

**On Windows (PowerShell):**
```powershell
# Make sure virtual environment is activated
venv\Scripts\Activate

# Run the dashboard
streamlit run dashboard.py
```

**On Windows (Command Prompt):**
```cmd
# Make sure virtual environment is activated
venv\Scripts\activate.bat

# Run the dashboard
streamlit run dashboard.py
```

**On macOS/Linux:**
```bash
# Activate virtual environment
source venv/bin/activate

# Run the dashboard
streamlit run dashboard.py
```

### Option 2: Direct Command (without venv)
```bash
streamlit run dashboard.py
```

## What Happens When You Run It

1. The dashboard will start a local web server
2. Your default web browser should automatically open to `http://localhost:8501`
3. If it doesn't open automatically, copy and paste `http://localhost:8501` into your browser
4. Use the filters in the sidebar to explore your data
5. Interact with the charts by hovering, zooming, and clicking

## Sample Data

The dashboard includes built-in sample data generation:
- **6 months** of historical data (180+ days)
- **500+ transactions** with realistic values
- **10 products** across 4 categories
- **4 sales regions** (North, South, East, West)
- Prices ranging from $30 (Charger) to $1000+ (Laptop)

No external CSV files needed - data is generated on the first run.

## Customization

### Modify Sample Data Generation
Edit the `generate_sample_data()` function in `dashboard.py` to:
- Add more products
- Change date ranges
- Adjust transaction counts
- Modify price ranges

### Change Colors
Look for color codes in the visualization functions:
- Update `color_discrete_sequence` for pie charts
- Modify `color_continuous_scale` for bar/heatmaps
- Change `line=dict(color='#1f77b4')` for line charts

### Add Your Own Data
Replace the `generate_sample_data()` function call with your own CSV loading logic:

```python
# Example: Load from CSV
df = pd.read_csv('your_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
```

## Troubleshooting

### Issue: "streamlit: command not found"
**Solution:** Make sure you've activated the virtual environment and installed requirements
```bash
pip install streamlit
```

### Issue: Port 8501 is already in use
**Solution:** Run on a different port
```bash
streamlit run dashboard.py --server.port 8502
```

### Issue: Module not found errors
**Solution:** Reinstall dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Issue: Dashboard looks slow or unresponsive
**Solution:** Clear Streamlit cache
```bash
streamlit cache clear
```

## Dashboard Layout

```
┌─────────────────────────────────────────┐
│         Sales & Revenue Dashboard       │
├─────────────────────────────────────────┤
│  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐   │
│  │ $   │  │ #   │  │ Avg │  │ Top │   │
│  │Rev  │  │Trans│  │ AOV │  │Reg  │   │
│  └─────┘  └─────┘  └─────┘  └─────┘   │
├─────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐   │
│  │   Revenue    │  │   Category   │   │
│  │    Trend     │  │    Sales     │   │
│  └──────────────┘  └──────────────┘   │
├─────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐   │
│  │   Regional   │  │  Top 5 Prod  │   │
│  │  Distribution│  │   Revenue    │   │
│  └──────────────┘  └──────────────┘   │
├─────────────────────────────────────────┤
│        Detailed Sales Data Table        │
│              (Scrollable)               │
└─────────────────────────────────────────┘
```

## File Structure

```
revenueanalyst/
├── dashboard.py          # Main application file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## System Requirements

- **Python:** 3.8 or higher
- **RAM:** 512 MB minimum (1 GB recommended)
- **Disk Space:** 100 MB for dependencies
- **Browser:** Modern browser (Chrome, Firefox, Safari, Edge)

## Performance Notes

- Dashboard loads data into cache after first run
- Chart interactions are handled client-side via Plotly
- Filter operations are fast even with 500+ transactions
- CSV export completes instantly

## Tips for Best Use

1. **Use Date Range Filter** - Narrowing date ranges speeds up analysis
2. **Stack Filters** - Combine multiple filters for focused insights
3. **Hover Over Charts** - See exact values when hovering
4. **Download CSV** - Export filtered data for presentations
5. **Bookmark URL** - Save your local dashboard URL for quick access

## Future Enhancements

Possible additions to the dashboard:
- Year-over-year comparisons
- Forecasting with trend lines
- Custom metric calculations
- PDF report export
- Real-time data integration
- Multi-user authentication
- Database connectivity

## License

This dashboard is provided as-is for educational and commercial use.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review Streamlit documentation: https://docs.streamlit.io
3. Review Plotly documentation: https://plotly.com/python

## Version History

- **v1.0** (2024-04-27) - Initial release with core features
  - KPI cards
  - 4 main visualizations
  - Interactive filters
  - CSV export

---

**Built with ❤️ using Streamlit & Plotly**
