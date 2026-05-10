FUTURE_DS_01: Business Sales Performance Analytics
📌 Project Overview
This repository showcases an end-to-end data analytics pipeline designed to help businesses optimize profitability. The project covers the full data lifecycle: from raw data extraction and statistical cleaning to relational storage and interactive visualization.

🛠️ Technical Stack
Language: Python 3.x

Libraries: Pandas (Data Manipulation), NumPy (Statistical Analysis)

Database: MySQL (Data Persistence)

Visualization: Tableau Desktop / Tableau Public
📊 Interactive Dashboard
🚀 Click Here to View the Live Interactive Dashboard
(https://public.tableau.com/views/Business_Sales_Analytics/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Version Control: Git & GitHub

📂 Repository Structure
Plaintext
FUTURE_DS_01/
├── data/               # Contains the explored data 
├── reports/            # Tableau dashboard screenshots
├── sql/                # MySQL schema definitions (schema.sql)
├── src/                # Python source code for ETL and Outlier Detection
└── README.md           # Project documentation

⚙️ Methodology & Engineering
1. Data Cleaning (ETL)
Raw sales data often contains noise. I implemented the Interquartile Range (IQR) Method to identify and remove statistical outliers in the Sales and Profit columns. This ensures that extreme, one-off transactions do not skew the overall business trends.

2. Database Design
To move beyond flat files, I architected a MySQL schema to store the refined data. This allows for scalable querying and provides a "single source of truth" for the visualization layer.

3. Interactive Visualization
The final dashboard provides three core business views:

High selling products.

Revenue Trends: A dual-axis timeline tracking Sales vs. Profitability.

Geographic Performance: A map identifying high-value regions (and flagging loss-making states).

Category Analysis: A tree-map visualizing which product segments drive the most volume.

💡 Business Insights & Recommendations
Profit Engine: The West region is the most consistent profit driver; resources should be allocated to maintain its growth.

Operational Risk: The Central region shows high sales volume but low/negative profit margins. Recommendation: Review regional shipping costs and discount strategies.

Inventory Priority: High-performing sub-categories like Binders and Technology Accessories should be prioritized for stock replenishment.

🚀 How to Run
Execute sql/schema.sql in your MySQL environment.

Run src/etl_pipeline.py to process the raw data and load it into the database.

Open reports/tableau/screenshot in Tableau to view the interactive dashboard.
