# E-commerce Sales Analysis | Python + SQL + Power BI

**End-to-end project: Raw data → Python cleaning → SQL validation → Interactive Power BI dashboard**  
**Analyzed $8.91M in retail transactions to identify 82% UK market concentration**

### 📊 Dashboard Preview
[View Dashboard PDF](E-commerce_Sales_Overview.pdf)

### 🔧 Tech Stack
**Python**: pandas, numpy, sqlite3 | **SQL**: SQLite | **BI**: Power BI, DAX, Power Query

### 🔍 Project Workflow
1. **Data Cleaning & SQL Analysis** `python_scripts/`
   - **cleaning.py**: Processed 541K+ rows using pandas
     - Removed nulls, cancelled orders `InvoiceNo LIKE 'C%'`, duplicates
     - Created `TotalPrice` column: `Quantity * Price`
     - Exported `cleaned_retail.csv` for Power BI
   - **analysis.py**: Validated metrics using SQL + pandas
     ```sql
     SELECT Country, 
            ROUND(SUM(TotalPrice),2) as Revenue,
            ROUND(SUM(TotalPrice)*100.0/(SELECT SUM(TotalPrice) FROM retail),1) as Percent 
     FROM retail 
     GROUP BY Country 
     ORDER BY Revenue DESC LIMIT 5

      - Programmatically confirmed *82.0% UK revenue concentration*
Output: 541,909 total cleaned transactions analyzed


## 1. Dashboard Development Ecommerce_Sales.pbix
- Custom DAX measure: FORMAT(SUM('cleaned retail'[TotalPrice]), "$#,##0")
- Interactive date slicer controlling all visuals simultaneously
- Donut chart showing country-wise revenue breakdown
- Configured visual interactions to prevent cross-filtering conflicts

### 💡 Key Business Insight

**82.01% revenue concentration in United Kingdom** indicates high market dependency and major opportunity for geographic expansion. Date slicer enables stakeholders to analyze seasonal trends and campaign performance.

### 📁 Repository Structure

├── E-commerce_Sales_Overview.pdf    # Dashboard export
├── Ecommerce_Sales.pbix              # Power BI source file
├── python_scripts/
│   ├── cleaning.py                  # Pandas data cleaning
│   └── analysis.py                  # SQL + pandas validation
└── requirements.txt                  # Python dependencies

### 🎯 Skills Demonstrated
Python | pandas | SQL | SQLite | Power BI | DAX | Data Cleaning | Data Validation | Data Visualization | Business Analysis

