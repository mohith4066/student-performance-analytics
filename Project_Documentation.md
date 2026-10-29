# Project Documentation: Student Performance Analytics System

---

## 1. Project Title
* **Project Name:** Student Performance Analytics System
* **Course:** Python with AI
* **Student Name:** Mohith
* **Academic Submission:** Mini Project Assignment (EWB Courses)
* **Date:** October 2026

---

## 2. Objective
Educational institutions handle large volumes of student examination and attendance records across diverse academic disciplines. Manual evaluation of student performance, calculation of total marks, grade allocation, and pass/fail identification is time-consuming and prone to human error.

The **Student Performance Analytics System** was developed to automate the ingestion, calculation, analysis, and reporting of student academic performance. By leveraging Python's powerful numerical (`NumPy`) and data manipulation (`Pandas`) libraries, this project solves the following core problems:
* Eliminates manual tabulation errors in calculating totals and percentage averages.
* Standardizes grade assignments based on strict institutional grading boundaries.
* Implements multi-factor eligibility checks (individual subject cutoffs, overall average cutoffs, and mandatory attendance thresholds).
* Generates actionable institutional insights: identifying high-achieving top performers, subject-wise bottlenecks, and students at academic risk who require targeted intervention.

---

## 3. Technologies Used
* **Programming Language:** Python 3.13+
* **Numerical Computing Library:** NumPy (v2.3.1)
  * Vectorized multi-dimensional array operations (`np.sum`, `np.mean`, `np.max`, `np.min`, `np.std`, `np.median`)
  * Boolean indexing, `np.argmax`, `np.argmin`
* **Data Analysis & Manipulation Library:** Pandas (v2.3.3)
  * `pd.DataFrame`, `pd.read_csv`, `pd.Series`
  * Structural inspection, filtering, grouping (`groupby`), and CSV export
* **Environment & Tools:**
  * Visual Studio Code / Antigravity IDE
  * Git & GitHub for version control

---

## 4. Dataset Description
The dataset (`students.csv`) comprises 20 realistic student records representing diverse academic branches and varying achievement levels:

### Columns & Attributes:
1. **`StudentID`** (`str`): Unique student identification code (e.g., `STU101` to `STU120`).
2. **`Name`** (`str`): Full name of the student.
3. **`Department`** (`str`): Academic department (`Artificial Intelligence`, `Computer Science`, `Data Science`, `Information Technology`).
4. **`Mathematics`** (`int` / `float`): Marks scored out of 100 in Mathematics.
5. **`Physics`** (`int` / `float`): Marks scored out of 100 in Physics.
6. **`Computer_Science`** (`int` / `float`): Marks scored out of 100 in Computer Science.
7. **`Python_Programming`** (`int` / `float`): Marks scored out of 100 in Python Programming.
8. **`Data_Science`** (`int` / `float`): Marks scored out of 100 in Data Science.
9. **`Attendance`** (`float`): Percentage of lecture attendance attended (0.0% to 100.0%).

### Dataset Integrity:
* Total Records: 20 rows
* Null / Missing Values: 0 (No missing or corrupt data)
* Range of Marks: 35 to 99 across subjects to represent high achievers, average scorers, borderline students, and failing cases.

---

## 5. Implementation
The project follows a modular, 5-step implementation pipeline adhering to the EWB project guidelines:

### Step 1 – Prepare the Dataset
* Created a realistic dataset (`students.csv`) containing 20 student entries spanning 4 academic departments.

### Step 2 – Read and Inspect Data
* Utilized `pandas.read_csv()` in `functions.load_dataset()`.
* Carried out structural audits via `functions.inspect_dataset()`, extracting row counts, column counts, missing values count, and data types.

### Step 3 – Process the Data
* **NumPy Vectorized Calculations:** Converted the 5 subject marks columns into a 2D NumPy array (`marks_matrix`). Calculated `Total_Marks` with `np.sum(marks_matrix, axis=1)` and `Average_Marks` with `np.mean(marks_matrix, axis=1)` in a single vectorized pass.
* **Grading Logic:** Implemented `assign_grade()` based on institutional rubrics:
  * $\ge 90\%$: `A+`
  * $80\% - 89.99\%$: `A`
  * $70\% - 79.99\%$: `B`
  * $60\% - 69.99\%$: `C`
  * $50\% - 59.99\%$: `D`
  * $< 50\%$: `F`
* **Pass / Fail Logic:** Implemented `evaluate_pass_fail()` with three concurrent criteria:
  1. Student must score at least 40 marks in each individual subject.
  2. Student must achieve an overall aggregate of at least 50%.
  3. Student must meet the mandatory attendance threshold of 75%.
* **Loops for Processing:** Iterated over rows using explicit Python `for` loops to assign individual grades, track individual failure causes, and assign personalized remarks.

### Step 4 – Perform In-Depth Analysis
* Computed overall class statistics using NumPy: mean, median, standard deviation, max, and min.
* Formulated answers to the 4 essential practical questions.
* Executed subject-wise performance aggregations with loops and NumPy arrays.
* Extracted top 5 rankers with `get_top_performers()`.
* Performed departmental aggregation using `groupby()` to evaluate departmental pass percentages.

### Step 5 – Final Output & Export
* Rendered clean, formatted terminal outputs with ASCII headers and organized tabular displays.
* Exported the fully augmented DataFrame to `processed_students.csv`.
* Exported the complete executive analytical report to `analytics_summary.txt`.

---

## 6. Key Features
* **Modular Code Architecture:** Separation of concerns between `functions.py` (reusable business logic) and `main.py` (driver script).
* **NumPy Performance Optimization:** Vectorized 2D matrix calculations for row-wise sums and column-wise statistics.
* **Comprehensive Eligibility Verification:** Holistic evaluation accounting for subject mastery, aggregate performance, and attendance discipline.
* **Granular Failure Diagnostics:** Detailed failure reasons documented in `Remarks` (e.g., specific subject failed, low attendance shortage).
* **Subject & Departmental Insights:** Automated statistical computation (Mean, Median, Highest, Lowest, Std Dev, and Pass Rates).
* **Dual Format Reporting:** Simultaneous terminal dashboard, persistent CSV export, and text report generation.

---

## 7. Output / Terminal Execution Results

### 7.1 Core Practical Questions Answered:
```text
1. Which student has the highest average?
   -> Arjun Reddy (STU115 - Data Science) with an average of 96.8% (Grade: A+)

2. Which subject has the best average?
   -> Python_Programming with an average score of 79.7 / 100

3. How many students passed?
   -> 17 out of 20 students (85.0%) (Failed: 3)

4. What is the overall class average?
   -> 75.42% (Median: 79.2%, Std Dev: 16.31)
```

### 7.2 Subject-Wise Performance Analysis:
```text
           Subject  Average  Median  Highest  Top_Scorer  Lowest  Std_Dev  Pass_Rate_%
       Mathematics    72.90   77.00    96.00 Arjun Reddy   35.00    18.34        90.00
           Physics    70.65   73.00    94.00 Arjun Reddy   38.00    15.91        95.00
  Computer_Science    77.25   81.00    98.00 Arjun Reddy   42.00    15.80       100.00
Python_Programming    79.70   84.50    99.00 Arjun Reddy   45.00    15.80       100.00
      Data_Science    76.60   80.50    97.00 Ananya Iyer   40.00    16.26       100.00
```

### 7.3 Top 5 Performing Students (Leaderboard):
```text
  Rank StudentID           Name              Department  Total_Marks  Average_Marks Grade  Attendance Result
Rank 1    STU115    Arjun Reddy            Data Science       484.00          96.80    A+       99.00   Pass
Rank 2    STU104    Ananya Iyer  Information Technology       473.00          94.60    A+       98.00   Pass
Rank 3    STU101   Aarav Sharma Artificial Intelligence       467.00          93.40    A+       96.50   Pass
Rank 4    STU110 Sneha Kulkarni        Computer Science       456.00          91.20    A+       95.50   Pass
Rank 5    STU120    Kavya Menon            Data Science       450.00          90.00    A+       96.00   Pass
```

### 7.4 Department-Wise Analytics:
```text
             Department  Total_Students  Department_Average  Average_Attendance_%  Passed  Pass_Rate_%
 Information Technology               5               77.52                 87.40       5       100.00
Artificial Intelligence               5               75.88                 87.10       4        80.00
           Data Science               5               74.88                 86.90       4        80.00
       Computer Science               5               73.40                 85.30       4        80.00
```

### 7.5 Academic Attention Required (Failed Students):
```text
StudentID         Name              Department  Average_Marks  Attendance  Remarks
   STU109 Aditya Joshi Artificial Intelligence          54.60       78.00  Failed in subject(s): Mathematics (38)
   STU111  Rahul Mehra            Data Science          46.20       71.00  Average 46.20% below required 50.0%; Attendance 71.0% below minimum 75.0%
   STU117 Varun Kapoor        Computer Science          40.00       65.00  Failed in subject(s): Mathematics (35), Physics (38); Average 40.00% below required 50.0%; Attendance 65.0% below minimum 75.0%
```

---

## 8. Final Outcome
The project successfully met and exceeded all objectives set forth in the EWB Python assignment:
1. Complete automation of student data intake and statistical analysis.
2. Fast and robust calculations utilizing NumPy 2D array operations.
3. Clean, transparent eligibility evaluation with clear causes identified for non-passing students.
4. Production of structured CSV datasets and an executive summary text report.
5. Error-free, self-contained project architecture ready for submission and GitHub hosting.

---

## 9. Challenges & Learning
* **Balancing Vectorization with Iterative Logic:** The assignment specified both using NumPy for numerical calculations and using loops where iteration is required. This was solved cleanly by utilizing NumPy for vectorized matrix sums and averages, while using loops to inspect individual subject thresholds, build multi-reason diagnostic remarks, and construct rank boards.
* **Multi-Factor Pass/Fail Criteria:** Real-world grading requires more than just an aggregate percentage. Accounting for individual subject minimums (40 marks) and attendance shortages (75%) provided a realistic academic data analysis model.
* **Handling Numerical Precision:** Floating-point averages were explicitly rounded using `np.round()` to prevent precision artifacts when comparing against threshold boundaries.
* **Key Learning:** Deepened understanding of NumPy array indexing, Pandas DataFrame manipulation, functional modularity in Python, and automated report generation.

---

## 10. GitHub Repository
* **Repository Name:** `student-performance-analytics`
* **Repository Link:** `https://github.com/mohith4066/student-performance-analytics` *(Update with your GitHub username)*
* **Contents Included:**
  * `main.py`
  * `functions.py`
  * `students.csv`
  * `processed_students.csv`
  * `analytics_summary.txt`
  * `Project_Documentation.md`
  * `README.md`
  * `requirements.txt`
  * `.gitignore`
