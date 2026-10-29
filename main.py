"""
main.py
Student Performance Analytics System
Author: Mohith
Course: Python with AI (EWB Courses)

Executes the 5 Implementation Steps:
  Step 1: Prepare & Verify Dataset
  Step 2: Read Data & Basic Information Checks
  Step 3: Process Data (NumPy, Loops, Functions, Grading, Pass/Fail)
  Step 4: Perform Analysis (Highest/Lowest, Subject-wise, Departmental, Practical Questions)
  Step 5: Final Formatted Output & Export of Reports
"""

import os
import sys
import pandas as pd
import numpy as np

# Import custom reusable functions from functions.py
from functions import (
    DEFAULT_SUBJECTS,
    PASSING_MARK_PER_SUBJECT,
    PASSING_AVERAGE,
    MIN_ATTENDANCE_PERCENT,
    load_dataset,
    inspect_dataset,
    process_student_records,
    compute_overall_statistics,
    analyze_subject_performance,
    get_top_performers,
    analyze_department_performance,
    answer_practical_questions
)


def print_banner(title: str, character: str = "=", width: int = 80) -> None:
    """Print an eye-catching section banner."""
    print()
    print(character * width)
    print(f" {title.upper()} ".center(width, character))
    print(character * width)


def print_sub_banner(title: str, width: int = 80) -> None:
    """Print a sub-section divider."""
    print()
    print("-" * width)
    print(f">> {title}")
    print("-" * width)


def main():
    # Configure Pandas display settings for optimal terminal readability
    pd.set_option('display.max_columns', 15)
    pd.set_option('display.width', 1000)
    pd.set_option('display.float_format', lambda x: f'{x:.2f}')

    print_banner("STUDENT PERFORMANCE ANALYTICS SYSTEM", "=")
    print("Project: Python with AI Mini Project Assignment")
    print("Technologies: Python 3, NumPy, Pandas")
    print("Concepts: Variables, Data Types, Loops, Functions, NumPy, Pandas, Data Analysis")

    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, "students.csv")
    output_csv_path = os.path.join(base_dir, "processed_students.csv")
    output_summary_path = os.path.join(base_dir, "analytics_summary.txt")

    # =========================================================================
    # STEP 1: PREPARE THE DATASET
    # =========================================================================
    print_banner("STEP 1: PREPARE AND VERIFY THE DATASET", "-")
    if not os.path.exists(dataset_path):
        print(f"[ERROR] Target dataset file not found at: {dataset_path}")
        sys.exit(1)
    print(f"[OK] Dataset confirmed present: '{dataset_path}'")
    print("Dataset includes 20 student records with attributes: StudentID, Name, Department,")
    print("5 subject marks (Mathematics, Physics, Computer Science, Python, Data Science), and Attendance.")

    # =========================================================================
    # STEP 2: READ THE DATA
    # =========================================================================
    print_banner("STEP 2: READ AND INSPECT DATA USING PANDAS", "-")
    raw_df = load_dataset(dataset_path)
    inspection = inspect_dataset(raw_df, DEFAULT_SUBJECTS)

    print_sub_banner("Dataset Dimensionality & Structure")
    print(f"Total Student Records : {inspection['total_records']}")
    print(f"Total Attributes/Cols : {inspection['total_columns']}")
    print(f"Column Names          : {', '.join(inspection['column_names'])}")

    print_sub_banner("Data Type Verification & Null Value Check")
    dtype_check_df = pd.DataFrame({
        'Column': raw_df.columns,
        'Data Type': [str(t) for t in raw_df.dtypes],
        'Null Count': [raw_df[col].isnull().sum() for col in raw_df.columns]
    })
    print(dtype_check_df.to_string(index=False))

    print_sub_banner("Raw Dataset Preview (First 5 Records)")
    print(raw_df.head(5).to_string(index=False))

    # =========================================================================
    # STEP 3: PROCESS THE DATA
    # =========================================================================
    print_banner("STEP 3: PROCESS THE DATA (NUMPY & CUSTOM LOGIC)", "-")
    print("Applying reusable processing functions:")
    print(" 1. Vectorized NumPy row summation for Total Marks")
    print(" 2. Vectorized NumPy mean calculation for Average Percentage")
    print(" 3. Iterative grading logic (A+, A, B, C, D, F)")
    print(" 4. Multi-condition academic pass/fail evaluation:")
    print(f"    - Pass condition: Subject marks >= {PASSING_MARK_PER_SUBJECT}")
    print(f"                      Overall average >= {PASSING_AVERAGE}%")
    print(f"                      Attendance >= {MIN_ATTENDANCE_PERCENT}%")

    processed_df = process_student_records(raw_df, DEFAULT_SUBJECTS)
    print(f"\n[OK] Processing complete. Augmented DataFrame now has {len(processed_df.columns)} columns.")

    print_sub_banner("Processed Student Records Sample (Top 5)")
    preview_cols = ['StudentID', 'Name', 'Department', 'Total_Marks', 'Average_Marks', 'Grade', 'Attendance', 'Result']
    print(processed_df[preview_cols].head(5).to_string(index=False))

    # =========================================================================
    # STEP 4: PERFORM ANALYSIS
    # =========================================================================
    print_banner("STEP 4: PERFORM IN-DEPTH DATA ANALYSIS", "-")

    overall_stats = compute_overall_statistics(processed_df)
    subject_df = analyze_subject_performance(processed_df, DEFAULT_SUBJECTS)
    top_performers_df = get_top_performers(processed_df, n=5)
    dept_df = analyze_department_performance(processed_df)
    answers = answer_practical_questions(processed_df, overall_stats, subject_df)

    # 4.1 Practical Questions Answered
    print_sub_banner("Core Practical Questions (Assignment Step 4 Requirements)")
    print(f"1. Which student has the highest average?")
    print(f"   -> {answers['highest_student_average']}")
    print(f"\n2. Which subject has the best average?")
    print(f"   -> {answers['best_subject_average']}")
    print(f"\n3. How many students passed?")
    print(f"   -> {answers['students_passed']} (Failed: {overall_stats['fail_count']})")
    print(f"\n4. What is the overall class average?")
    print(f"   -> {answers['overall_class_average']} (Median: {overall_stats['class_median']}%, Std Dev: {overall_stats['class_std_dev']})")

    # 4.2 Subject-wise Performance Analysis
    print_sub_banner("Subject-Wise Performance Analysis (NumPy Aggregations)")
    print(subject_df.to_string(index=False))

    # 4.3 Top-Performing Students Leaderboard
    print_sub_banner("Top-Performing Students (Rank 1 to 5)")
    print(top_performers_df.to_string(index=False))

    # 4.4 Department-Wise Performance Breakdown
    print_sub_banner("Department-Wise Performance Analytics")
    print(dept_df.to_string(index=False))

    # 4.5 Academic Status & Failure Reason Breakdown
    print_sub_banner("Students Requiring Academic Attention (Failed Status)")
    failed_students = processed_df[processed_df['Result'] == 'Fail'][['StudentID', 'Name', 'Department', 'Average_Marks', 'Attendance', 'Remarks']]
    if len(failed_students) > 0:
        print(failed_students.to_string(index=False))
    else:
        print("All students met the passing criteria!")

    # =========================================================================
    # STEP 5: FINAL OUTPUT & EXPORT
    # =========================================================================
    print_banner("STEP 5: FINAL OUTPUT PRESENTATION & EXPORT", "-")

    # Export Processed Dataset to CSV
    processed_df.to_csv(output_csv_path, index=False)
    print(f"[EXPORT] Full processed dataset saved to: '{output_csv_path}'")

    # Export Analytical Summary Report to text file
    with open(output_summary_path, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("STUDENT PERFORMANCE ANALYTICS SYSTEM - SUMMARY REPORT\n")
        f.write("=" * 80 + "\n\n")

        f.write("1. EXECUTIVE SUMMARY\n")
        f.write("-" * 40 + "\n")
        f.write(f"Total Students Evaluated  : {overall_stats['total_students']}\n")
        f.write(f"Class Overall Average     : {overall_stats['class_average']}%\n")
        f.write(f"Class Median Average      : {overall_stats['class_median']}%\n")
        f.write(f"Class Standard Deviation  : {overall_stats['class_std_dev']}\n")
        f.write(f"Passing Students          : {overall_stats['pass_count']} ({overall_stats['pass_percentage']}%)\n")
        f.write(f"Failing Students          : {overall_stats['fail_count']}\n")
        f.write(f"Highest Performing Student: {overall_stats['top_student']['name']} ({overall_stats['top_student']['average']}%)\n")
        f.write(f"Lowest Performing Student : {overall_stats['lowest_student']['name']} ({overall_stats['lowest_student']['average']}%)\n\n")

        f.write("2. CORE PRACTICAL QUESTIONS ANSWERED\n")
        f.write("-" * 40 + "\n")
        f.write(f"Q1. Which student has highest average? -> {answers['highest_student_average']}\n")
        f.write(f"Q2. Which subject has best average?    -> {answers['best_subject_average']}\n")
        f.write(f"Q3. How many students passed?          -> {answers['students_passed']}\n")
        f.write(f"Q4. What is overall class average?     -> {answers['overall_class_average']}\n\n")

        f.write("3. SUBJECT-WISE PERFORMANCE TABLE\n")
        f.write("-" * 40 + "\n")
        f.write(subject_df.to_string(index=False) + "\n\n")

        f.write("4. TOP 5 PERFORMING STUDENTS\n")
        f.write("-" * 40 + "\n")
        f.write(top_performers_df.to_string(index=False) + "\n\n")

        f.write("5. DEPARTMENT-WISE PERFORMANCE SUMMARY\n")
        f.write("-" * 40 + "\n")
        f.write(dept_df.to_string(index=False) + "\n\n")

        f.write("6. STUDENTS REQUIRING ATTENTION (FAIL / SHORTAGE)\n")
        f.write("-" * 40 + "\n")
        f.write(failed_students.to_string(index=False) + "\n")

    print(f"[EXPORT] Executive text summary report saved to: '{output_summary_path}'")
    print("\n[COMPLETE] All 5 Project Implementation Steps successfully executed!")
    print_banner("END OF EXECUTION", "=")


if __name__ == "__main__":
    main()
