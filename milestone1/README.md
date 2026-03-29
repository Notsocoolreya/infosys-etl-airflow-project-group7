# 📦 Milestone 1: Data Ingestion & Setup (Weeks 1–2)

## 🎯 Objective
The objective of Milestone 1 is to set up the project environment, create the database schema, and load raw CSV data into a SQLite database using Python scripts.  
This forms the foundation for further data processing in upcoming milestones.

---

## 🛠️ Tasks Implemented

### ✅ 1. Project Setup
- Created project folder structure  
- Organized scripts inside a `scripts/` folder  
- Set up Python environment and required libraries  

### ✅ 2. Database Creation
- Created SQLite database (`infosys.db`)  
- Defined schema for raw tables  
- Tables created:
  - `orders`  
  - `order_details`  
  - `sales_target`  

### ✅ 3. Data Ingestion
- Loaded raw CSV files into SQLite database  
- Used Python (Pandas + SQLite) for ingestion  
- Ensured proper column mapping and data loading  

---

## 📌 Scripts Used
All ingestion logic is implemented inside:


scripts/


---

## 📌 Raw Data Files
The following CSV files are used as input:

- `orders.csv`  
- `order_details.csv`  
- `sales_target.csv`  

---

## 📌 Tables Created
After execution, the following tables are created:

- `orders`  
- `order_details`  
- `sales_target`  

---

## 🧪 Testing & Validation
The ingestion process was validated by:

- Verifying table creation  
- Checking row counts after data loading  
- Ensuring correct data insertion  

Validation script:


scripts/check_data.py


---

## ⚙️ How to Run

Navigate to the scripts folder:

```bash
cd milestone1/scripts

Run the scripts in order:

python create_tables.py
python load_data.py
python check_data.py

📂 Folder Structure
milestone1/
│── scripts/
│   ├── create_tables.py
│   ├── load_data.py
│   └── check_data.py
│── README.md

** 🏁 Conclusion**

Milestone 1 successfully sets up the project environment and loads raw data into the SQLite database.
The created tables serve as the foundation for data cleaning and transformation in Milestone 2.


---

# ✅ Why this works
✔ Proper markdown headings  
✔ Correct spacing for GitHub preview  
✔ Code blocks render correctly  
✔ Matches your Milestone 2 style  

---

If you want next 🚀  
I can:
- Convert **all milestones into one main README (very important for final submission)**  
- Or review your **GitHub repo structure for marks**
