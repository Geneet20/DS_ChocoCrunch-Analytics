# 🍫✨ ChocoCrunch Analytics: Sweet Stats & Sour Truths

## 📋 Project Overview
A comprehensive data analytics project analyzing the global chocolate market using OpenFoodFacts API data. This project demonstrates end-to-end data science skills including API integration, ETL processes, SQL database design, exploratory data analysis, and interactive visualization.

**Key Features:**
- **Real-Time API Integration**: OpenFoodFacts API with pagination support for 12,000+ products
- **Comprehensive ETL Pipeline**: Automated data extraction, cleaning, and feature engineering
- **SQL Analytics Engine**: 27 predefined queries across 4 analysis categories
- **Interactive Dashboard**: Multi-page Streamlit application with real-time insights
- **Health Risk Assessment**: Evidence-based nutrition analysis and categorization
- **Business Intelligence**: Brand comparison and market trend analysis

## 🎯 Business Objectives
- **Health Risk Identification**: Identify calorie and sugar-heavy chocolate products with health warnings
- **Market Trend Analysis**: Track ultra-processed chocolate trends via NOVA classification
- **Brand Comparison**: Comprehensive brand-wise healthiness comparison based on nutrition metrics
- **Product Categorization**: Categorize products based on derived calorie and sugar classes
- **Stakeholder Reporting**: Provide interactive dashboard for business decision-making
- **Consumer Insights**: Generate actionable insights for health-conscious consumers

## 📊 Technical Skills Demonstrated
- **API Data Extraction**: Python requests with pagination, error handling, and data validation
- **ETL Pipeline Design**: Complete Extract, Transform, Load process with automated execution
- **Data Quality Management**: Advanced cleaning, imputation, and outlier detection
- **Feature Engineering**: Creation of derived health metrics and categorical variables
- **Database Design**: Normalized 3-table SQLite schema with indexes and views
- **SQL Analytics**: Complex queries with joins, aggregations, and window functions
- **Exploratory Data Analysis**: Statistical analysis with 10+ visualization types
- **Interactive Dashboards**: Multi-page Streamlit application with dynamic filtering
- **Business Intelligence**: KPI tracking, trend analysis, and actionable insights

## 🏗️ Project Structure
```
ChocoCrunch_Analytics/
├── src/                          # Core processing modules
│   ├── config.py                 # Central configuration and constants
│   ├── data_extraction.py        # OpenFoodFacts API integration with pagination
│   ├── data_cleaning.py         # Data quality and preprocessing pipeline
│   └── feature_engineering.py   # Health metrics and derived features
├── sql/                         # Database operations and analytics
│   ├── schema.sql               # Normalized 3-table database schema
│   ├── queries.sql              # 27 comprehensive analysis queries
│   └── insert_data.py           # Automated data insertion with validation
├── notebooks/                   # Analysis and exploration
│   ├── 01_data_exploration.ipynb    # Initial data discovery and profiling
│   ├── 02_eda_analysis.ipynb       # Comprehensive EDA with visualizations
│   └── 03_sql_queries.ipynb       # SQL query execution and results
├── streamlit_app/              # Interactive dashboard
│   ├── app.py                  # 5-page dashboard with navigation
│   └── utils.py                # Database helpers and visualization utilities
├── data/                       # Data storage hierarchy
│   ├── raw/                    # Raw API response data (CSV format)
│   ├── processed/              # Cleaned and engineered datasets
│   └── database/               # SQLite database with indexed tables
├── visualizations/             # Generated charts and exports
│   └── exports/                # High-resolution plot exports
├── run_project.py              # Complete pipeline execution script
└── requirements.txt            # Python dependencies with version pinning
```

## 🚀 Quick Start Guide

### Option 1: Complete Pipeline Execution (Recommended)
```bash
# Navigate to project directory
cd ChocoCrunch_Analytics

# Create and activate virtual environment
python -m venv choco_env
choco_env\Scripts\activate  # Windows
# source choco_env/bin/activate  # Linux/Mac

# Install all dependencies
pip install -r requirements.txt

# Run complete automated pipeline
python run_project.py
```

### Option 2: Manual Step-by-Step Execution
```bash
# 1. Extract data from OpenFoodFacts API (~15-20 minutes)
python src/data_extraction.py

# 2. Clean and validate data quality
python src/data_cleaning.py

# 3. Engineer derived features and health metrics
python src/feature_engineering.py

# 4. Create SQLite database and insert processed data
python sql/insert_data.py

# 5. Launch interactive dashboard
streamlit run streamlit_app/app.py
```

### Option 3: Analysis-Only (Using Sample Data)
```bash
# Install dependencies
pip install -r requirements.txt

# Launch dashboard with sample data
streamlit run streamlit_app/app.py

# Open EDA notebook for analysis
jupyter notebook notebooks/02_eda_analysis.ipynb
```

## 📈 Analysis Components & Features

### 🔢 Derived Health Metrics
- **sugar_to_carb_ratio**: Quantifies sugar concentration relative to total carbohydrates
- **calorie_category**: Classification (Low: <300, Moderate: 300-500, High: >500 kcal/100g)
- **sugar_category**: Classification (Low: <10g, Moderate: 10-25g, High: >25g per 100g)
- **is_ultra_processed**: NOVA group 4 classification for processed food identification
- **health_score**: Composite metric combining multiple nutrition factors

### 🗄️ Database Architecture
```sql
-- Normalized 3-table schema with relationships
product_info (barcode, product_name, brands, nova_group, etc.)
nutrient_info (barcode, energy_kcal, sugars, fat, fiber, etc.)
derived_metrics (barcode, sugar_to_carb_ratio, calorie_category, etc.)
```

### 📊 SQL Analytics Engine (27 Queries)
**Product Information Queries (1-6):**
- Product count and brand analysis
- NOVA group distribution
- Country and category insights

**Nutrient Analysis Queries (7-13):**
- Statistical summaries (mean, median, std)
- Distribution analysis by nutrition score
- Calorie and sugar content analysis

**Derived Metrics Queries (14-20):**
- Health category distributions
- Sugar-to-carb ratio analysis
- Ultra-processed food trends

**Advanced Joins & Analysis (21-27):**
- Multi-table insights
- Brand healthiness rankings
- Consumer recommendation queries

### 📱 Interactive Dashboard Pages
1. **Overview**: KPI summary cards and key metrics
2. **SQL Query Results**: Dynamic query execution with formatted results
3. **EDA Insights**: Statistical analysis and distribution visualizations
4. **Health Risk Assessment**: Nutrition alerts and category analysis
5. **Brand Comparison**: Comparative analysis across chocolate brands

## 🔍 Key Business Insights
*Generate after running complete analysis:*

### Health & Nutrition Findings
- **High-Risk Products**: X% of products exceed recommended sugar limits
- **Ultra-Processed Prevalence**: Y% classified as NOVA group 4
- **Brand Health Rankings**: Top 10 healthiest vs. least healthy brands
- **Consumer Warnings**: Products requiring health advisory labels

### Market Intelligence
- **Brand Market Share**: Distribution by major chocolate manufacturers
- **Product Innovation Trends**: Healthier alternatives and formulations
- **Geographic Patterns**: Regional differences in chocolate nutrition profiles
- **Price-Health Correlation**: Analysis of premium vs. standard nutrition quality

## 🛠️ Technology Stack & Dependencies

### Core Technologies
- **Python 3.8+**: Primary programming language
- **Pandas ≥1.5.0**: Data manipulation and analysis
- **Requests**: RESTful API integration with OpenFoodFacts
- **SQLite3**: Lightweight database for development and production
- **NumPy**: Numerical computing and statistical operations

### Visualization & Analytics
- **Matplotlib**: Static plot generation and publication-quality charts
- **Seaborn**: Statistical data visualization with enhanced aesthetics
- **Plotly**: Interactive charts and dashboard components
- **Streamlit**: Web application framework for dashboard deployment

### Development & Analysis
- **Jupyter**: Interactive analysis notebooks and documentation
- **SQLAlchemy**: Database ORM and connection management
- **Logging**: Comprehensive error tracking and pipeline monitoring

## 📊 Project Deliverables & Status

### ✅ Completed Components
- [x] **Project Structure**: Complete directory organization and file structure
- [x] **Configuration Management**: Centralized settings and API parameters
- [x] **API Integration**: OpenFoodFacts extraction with pagination and error handling
- [x] **Data Processing Pipeline**: Cleaning, validation, and feature engineering modules
- [x] **Database Design**: Normalized 3-table schema with indexes and relationships
- [x] **SQL Analytics**: All 27 queries implemented and tested
- [x] **EDA Analysis**: Comprehensive notebook with 10+ visualization types
- [x] **Interactive Dashboard**: 5-page Streamlit application with real-time insights
- [x] **Automation Scripts**: Complete pipeline execution with progress tracking
- [x] **Documentation**: README with setup instructions and technical details

### 🔄 Execution Ready
- [x] **Data Extraction**: Automated API calls for 12,000+ chocolate products
- [x] **ETL Pipeline**: End-to-end data processing workflow
- [x] **Health Analytics**: Risk assessment and categorization algorithms
- [x] **Business Intelligence**: Brand comparison and market analysis tools
- [x] **Sample Data Generation**: Demo functionality when API data unavailable

## ⏱️ Execution Timeline & Performance

**Initial Setup**: 5-10 minutes (environment and dependencies)
**Data Extraction**: 15-25 minutes (12,000+ products via API)
**Data Processing**: 5-10 minutes (cleaning and feature engineering)
**Database Setup**: 2-5 minutes (table creation and data insertion)
**Dashboard Launch**: 1-2 minutes (Streamlit application startup)

**Total Pipeline Execution**: ~30-45 minutes end-to-end
10 days from project start date

## 📝 References
- OpenFoodFacts API Documentation
- Streamlit Documentation
- Power BI Integration Guides
- Nutrition Analytics Best Practices

---
**Created By**: Nilofer Mubeen | **Verified By**: Shadiya | **Approved By**: Nehlath Harmain