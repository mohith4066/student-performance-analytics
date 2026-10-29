# Student Performance Analytics System

A Python data-analysis project built with **NumPy** and **Pandas** for analyzing student academic and attendance records, generating subject-wise and department-wise metrics, computing grades, evaluating pass/fail statuses, and ranking top performers.

Developed for the **Python with AI** course assignment at **EWB Courses**.

---

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Concepts Covered](#concepts-covered)
- [Project Structure](#project-structure)
- [Dataset Details](#dataset-details)
- [Academic Rules & Conditions](#academic-rules--conditions)
- [Installation & Setup](#installation--setup)
- [Running the Project](#running-the-project)
- [Outputs & Key Results](#outputs--key-results)
- [GitHub Submission Checklist](#github-submission-checklist)

---

## 🎯 Project Overview
The **Student Performance Analytics System** automates the end-to-end processing of student academic data. It reads student records from a CSV file, performs vector calculations using NumPy, filters and groups data using Pandas, identifies top achievers and failing students, and outputs an executive summary report.

### Core Goals:
- Total marks and average percentage computation using NumPy matrix operations.
- Rule-based grade assignment (`A+`, `A`, `B`, `C`, `D`, `F`).
- Pass/Fail verification combining subject cutoffs, overall average, and attendance.
- Comprehensive subject-wise statistical analysis (Mean, Median, Highest, Lowest, Std Dev, Pass Rate).
- Departmental comparative analysis.
- Clear, formatted terminal output and file exports (`.csv` and `.txt`).

---

## 💡 Concepts Covered
- **Python Fundamentals:** Variables, Data Types, Control Structures, Loops, Functions, Formatted Output.
- **NumPy:** Vectorized calculations (`np.sum`, `np.mean`, `np.median`, `np.std`, `np.max`, `np.min`, `np.argmax`, `np.argmin`, boolean indexing).
- **Pandas:** DataFrame creation, reading CSV, column assignments, sorting, grouping (`groupby`), and CSV export.
- **Data Analysis:** Descriptive statistics, distribution analysis, condition-based filtering.

---

## 📁 Project Structure

```text
student-performance-analytics/
├── students.csv                  # Input dataset containing 20 student records
├── functions.py                  # Modular, reusable calculation & processing functions
├── main.py                       # Main driver script executing Steps 1 to 5
├── processed_students.csv        # Augmented dataset output with totals, averages, grades & status
├── analytics_summary.txt         # Auto-generated textual executive summary report
├── Project_Documentation.md      # Comprehensive 10-section project assessment documentation
├── requirements.txt              # Required Python packages (NumPy, Pandas)
├── .gitignore                    # Git ignore file for Python projects
└── README.md                     # Project overview and instructions
```

---

## 📊 Dataset Details
The dataset (`students.csv`) includes **20 student records** across 4 departments with realistic marks and attendance:
- `StudentID`: Unique identifier (e.g. `STU101` to `STU120`)
- `Name`: Full name of student
- `Department`: `Artificial Intelligence`, `Computer Science`, `Data Science`, `Information Technology`
- `Mathematics`: Score out of 100
- `Physics`: Score out of 100
- `Computer_Science`: Score out of 100
- `Python_Programming`: Score out of 100
- `Data_Science`: Score out of 100
- `Attendance`: Percentage of attendance (0 - 100%)

---

## 📜 Academic Rules & Conditions

### 1. Grading Scale
| Average Marks Range | Grade | Description |
|:---|:---:|:---|
| $\ge 90\%$ | **A+** | Outstanding |
| $80\% - 89.99\%$ | **A** | Excellent |
| $70\% - 79.99\%$ | **B** | Very Good |
| $60\% - 69.99\%$ | **C** | Good |
| $50\% - 59.99\%$ | **D** | Satisfactory |
| $< 50\%$ | **F** | Fail / Needs Improvement |

### 2. Pass / Fail Evaluation Conditions
A student is declared **`Pass`** if and only if **all three** criteria are met:
1. **Subject Minimum:** Score $\ge 40$ marks in each individual subject.
2. **Overall Aggregate:** Overall average $\ge 50\%$.
3. **Attendance Minimum:** Minimum attendance $\ge 75\%$.

If any criterion is not met, the student is marked **`Fail`** and the specific reason is recorded in the `Remarks` column.

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.9+ (tested on Python 3.13)
- pip package manager

### 1. Clone or Download the Repository
```bash
git clone https://github.com/mohith4066/student-performance-analytics.git
cd student-performance-analytics
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the main analysis pipeline by executing:

```bash
python main.py
```

The program will execute the 5 sequential implementation steps:
1. **Step 1:** Verify dataset structure and existence.
2. **Step 2:** Read data with Pandas and check null values and data types.
3. **Step 3:** Calculate totals, averages, grades, and pass/fail statuses.
4. **Step 4:** Perform statistical analysis and answer key questions.
5. **Step 5:** Display formatted results and export `processed_students.csv` and `analytics_summary.txt`.

---

## 📈 Outputs & Key Results

### 1. Answers to Practical Questions:
- **Highest Average Student:** Arjun Reddy (`STU115` - Data Science) — **96.80% (Grade A+)**
- **Best Performing Subject:** Python Programming — **79.70 / 100**
- **Students Passed:** **17 out of 20 (85.0%)** (3 failed)
- **Overall Class Average:** **75.42%** (Median: 79.20%, Std Dev: 16.31)

### 2. Top 5 Performers (Leaderboard):
| Rank | Student ID | Name | Department | Total | Average | Grade | Attendance |
|:---:|:---:|:---|:---|:---:|:---:|:---:|:---:|
| 1 | STU115 | Arjun Reddy | Data Science | 484.00 | 96.80% | A+ | 99.0% |
| 2 | STU104 | Ananya Iyer | Information Technology | 473.00 | 94.60% | A+ | 98.0% |
| 3 | STU101 | Aarav Sharma | Artificial Intelligence | 467.00 | 93.40% | A+ | 96.5% |
| 4 | STU110 | Sneha Kulkarni | Computer Science | 456.00 | 91.20% | A+ | 95.5% |
| 5 | STU120 | Kavya Menon | Data Science | 450.00 | 90.00% | A+ | 96.0% |

---

## ✅ GitHub Submission Checklist
- [x] Project completed and tested without errors
- [x] Student dataset (`students.csv`) with 20 realistic records included
- [x] NumPy and Pandas used appropriately for data loading & calculations
- [x] Functions and loops used where required
- [x] Clean repository structure created
- [x] `README.md` and `Project_Documentation.md` included
- [x] GitHub repository push instructions provided
