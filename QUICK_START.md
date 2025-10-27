# 🍫 ChocoCrunch Analytics - Quick Start Guide

## 🚀 How to Run This Project

### Option 1: One-Command Setup (Recommended)
```bash
# Navigate to project folder
cd ChocoCrunch_Analytics

# Create virtual environment
python -m venv choco_env

# Activate environment (Windows)
choco_env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run complete project
python run_project.py

# Launch dashboard
streamlit run streamlit_app/app.py
```

### Option 2: Step-by-Step Execution
```bash
# 1. Setup environment
python -m venv choco_env
choco_env\Scripts\activate
pip install -r requirements.txt

# 2. Extract data (15-20 minutes)
python src/data_extraction.py

# 3. Process data (5-10 minutes)
python src/data_cleaning.py
python src/feature_engineering.py

# 4. Create database (2-5 minutes)
python sql/insert_data.py

# 5. Launch dashboard
streamlit run streamlit_app/app.py
```

### Option 3: Demo Mode (Instant)
```bash
# Skip data extraction, use sample data
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

---

## 📊 All Project Features

### 1. Data Pipeline
- **✅ API Extraction**: 12,000+ chocolate products from OpenFoodFacts
- **✅ Data Cleaning**: Missing values, outliers, quality validation
- **✅ Feature Engineering**: Health categories, business metrics
- **✅ Database Creation**: 3-table SQLite schema with indexes

### 2. SQL Analytics (27 Queries)
- **📋 Product Queries (1-6)**: Brand analysis, counts, categories
- **🥜 Nutrition Queries (7-13)**: Calories, sugar, fat analysis
- **📊 Derived Metrics (14-20)**: Health scores, ratios, categories
- **🔄 Advanced Joins (21-27)**: Multi-table insights, rankings

### 3. Interactive Dashboard (5 Pages)

#### Page 1: 📊 Overview
- **KPI Cards**: Products, brands, health metrics
- **Market Share**: Top 5 brands pie chart
- **Health Alerts**: Calorie and sugar warnings
- **Quick Stats**: Category distributions

#### Page 2: 🔍 SQL Query Results
- **Query Categories**: Organized by analysis type
- **Dynamic Execution**: Run queries on-demand
- **Formatted Results**: Tables with metrics
- **Export Options**: Download results

#### Page 3: 📈 EDA Analysis
- **Distribution Analysis**: Calorie/sugar histograms
- **Correlation Matrix**: Nutrition component relationships
- **Category Comparison**: Box plots by health categories
- **Brand Analysis**: Statistical comparisons

#### Page 4: ⚠️ Health Risk Assessment
- **Risk Categories**: High/Moderate/Low classification
- **Threshold Analysis**: WHO-based nutrition limits
- **Product Alerts**: High-risk product identification
- **Recommendations**: Consumer guidance

#### Page 5: 🏆 Brand Comparison
- **Health Rankings**: Best vs worst brands
- **Nutrition Metrics**: Average values by brand
- **Market Positioning**: Brand healthiness scores
- **Consumer Insights**: Purchase recommendations

### 4. Business Intelligence Features

#### Health Analytics
- **Calorie Categories**: Low (<300), Moderate (300-500), High (>500 kcal/100g)
- **Sugar Categories**: Low (<15g), Moderate (15-35g), High (>35g per 100g)
- **Ultra-processed**: NOVA group 4 classification
- **Health Risk Score**: Composite risk assessment

#### Market Intelligence
- **Brand Segmentation**: Major/Medium/Minor brand classification
- **Product Innovation**: Healthier formulation trends
- **Consumer Trends**: Health-conscious purchasing patterns
- **Competitive Analysis**: Brand positioning insights

### 5. Technical Features
- **Error Handling**: Robust fallbacks and validation
- **Sample Data**: Demo mode when API unavailable
- **Flexible Columns**: Adapts to different data sources
- **Performance**: Cached operations and optimized queries
- **Debug Tools**: DataFrame inspection and logging

---

## 🎯 Usage Examples

### Running Specific Analysis
```python
# Extract only 1000 products for testing
python src/data_extraction.py --limit 1000

# Run specific SQL queries
python -c "
import sqlite3
conn = sqlite3.connect('data/database/chococrunch.db')
result = conn.execute('SELECT brand, COUNT(*) FROM product_info GROUP BY brand')
print(result.fetchall())
"

# Generate specific visualizations
python -c "
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/processed/chocolate_products_engineered.csv')
df['energy_kcal_value'].hist(bins=30)
plt.savefig('calorie_distribution.png')
"
```

### Custom Dashboard Pages
```python
# Add to streamlit_app/app.py
def show_custom_analysis(df):
    st.markdown("## 🔬 Custom Analysis")
    
    # Your custom analysis here
    custom_metric = df['sugars_value'] / df['fat_value']
    fig = px.scatter(df, x='energy_kcal_value', y=custom_metric,
                    title="Sugar-to-Fat Ratio vs Calories")
    st.plotly_chart(fig)
```

### Database Queries
```sql
-- Find healthiest chocolate brands
SELECT 
    p.brand,
    AVG(n.energy_kcal_value) as avg_calories,
    AVG(n.sugars_value) as avg_sugar,
    COUNT(*) as product_count
FROM product_info p
JOIN nutrient_info n ON p.product_code = n.product_code
GROUP BY p.brand
HAVING product_count >= 10
ORDER BY avg_calories ASC, avg_sugar ASC
LIMIT 10;
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Dashboard Won't Load
```bash
# Check if Streamlit is running
netstat -an | findstr 8501

# Kill existing processes
taskkill /f /im streamlit.exe

# Restart with clean cache
streamlit cache clear
streamlit run streamlit_app/app.py
```

#### Database Errors
```bash
# Recreate database
del data\database\chococrunch.db
python sql/insert_data.py

# Check database contents
sqlite3 data/database/chococrunch.db ".tables"
```

#### API Timeouts
```bash
# Check connection
ping world.openfoodfacts.org

# Use smaller batch size
python src/data_extraction.py --page-size 100
```

#### Missing Dependencies
```bash
# Reinstall all packages
pip uninstall -r requirements.txt -y
pip install -r requirements.txt
```

---

## 📱 Access Your Dashboard

After running the project, access your dashboard at:
- **Local URL**: http://localhost:8501
- **Network URL**: http://[your-ip]:8501

### Dashboard Navigation
1. **📊 Overview** - Start here for project summary
2. **🔍 SQL Results** - Explore 27 analytical queries
3. **📈 EDA** - Interactive data visualizations
4. **⚠️ Health Risk** - Nutrition alerts and warnings
5. **🏆 Brand Comparison** - Competitive analysis

---

## 🎉 Project Highlights

### Data Science Excellence
- **12,000+ Products**: Comprehensive chocolate market dataset
- **27 SQL Queries**: Complete analytical framework
- **5-Page Dashboard**: Professional business intelligence
- **Health Focus**: WHO-based nutrition guidelines

### Technical Achievements
- **Real-time API**: OpenFoodFacts integration
- **Complete ETL**: End-to-end data pipeline
- **Interactive Viz**: Plotly-powered dashboards
- **Robust Design**: Error handling and fallbacks

### Business Value
- **Market Insights**: Brand positioning and trends
- **Health Intelligence**: Risk assessment and alerts
- **Consumer Guidance**: Evidence-based recommendations
- **Competitive Analysis**: Brand comparison tools

---

**🍫 Ready to explore the sweet world of chocolate analytics? Run the commands above and dive into the data! 📊✨**