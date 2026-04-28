# E-commerce Sales Analysis | Python + Power BI

**End-to-end project: Data cleaning in Python → Interactive dashboard in Power BI**  
**Analyzed $8.91M in retail transactions to identify 82% UK market concentration**

### 📊 Dashboard Preview
[View Dashboard PDF](E-commerce_Sales_Overview.pdf)

### 🔧 Tech Stack
**Python**: pandas, numpy, Jupyter | **BI**: Power BI, DAX, Power Query

### 🔍 Project Workflow
1. **Data Cleaning** `python_scripts/data_cleaning.py`
   - Handled 541K+ rows: removed nulls, cancelled orders, duplicates
   - Created `TotalPrice` column: `Quantity * Price`
   - Exported `cleaned_retail.csv` for Power BI

2. **Exploratory Analysis** `python_scripts/eda.ipynb`
   - Initial revenue trends + country breakdown in Python
   - Validated data quality before BI build

3. **Dashboard Development** `Ecommerce_Sales.pbix`
   - Custom DAX measure: `FORMAT(SUM('cleaned retail'[TotalPrice]), "$#,##0")`
   - Interactive date slicer + donut chart by country
   - Built dynamic date filtering affecting all visuals simultaneously
   - Configured visual interactions to prevent cross-filtering

### 💡 Key Business Insight
**82.01% revenue concentration in United Kingdom** indicates high market dependency and major opportunity for geographic expansion.

### 📁 Repository Structure
├── E-commerce_Sales_Overview.pdf    # Dashboard export
├── Ecommerce_Sales.pbix              # Power BI source file
├── python_scripts/
│   ├── data_cleaning.py             # Pandas cleaning script
│   └── eda.ipynb                     # Exploratory analysis
└── requirements.txt                  # Python dependencies


### 🎯 Skills Demonstrated
Python | pandas | Power BI | DAX | Data Cleaning | Data Visualization | Business Analysis
