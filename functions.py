"""
functions.py
Reusable functions for the Student Performance Analytics System.
Demonstrates: Variables, Data Types, Functions, Loops, Conditions, NumPy, and Pandas.
"""

from typing import Dict, List, Tuple, Any
import numpy as np
import pandas as pd

# Default core subjects defined for analytics
DEFAULT_SUBJECTS: List[str] = [
    'Mathematics',
    'Physics',
    'Computer_Science',
    'Python_Programming',
    'Data_Science'
]

# Benchmark constants
PASSING_MARK_PER_SUBJECT: float = 40.0
PASSING_AVERAGE: float = 50.0
MIN_ATTENDANCE_PERCENT: float = 75.0


def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load student dataset from a CSV file into a Pandas DataFrame.
    Validates file existence and basic structure.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"[SUCCESS] Dataset successfully loaded from '{file_path}'.")
        return df
    except FileNotFoundError:
        print(f"[ERROR] The file '{file_path}' was not found. Please verify the path.")
        raise
    except Exception as e:
        print(f"[ERROR] An unexpected error occurred while loading the data: {e}")
        raise


def inspect_dataset(df: pd.DataFrame, subjects: List[str] = DEFAULT_SUBJECTS) -> Dict[str, Any]:
    """
    Inspect the DataFrame: shape, columns, missing values, and data types.
    Returns a dictionary of inspection summary.
    """
    total_records, total_columns = df.shape
    missing_values = df.isnull().sum().to_dict()
    column_types = {col: str(dtype) for col, dtype in df.dtypes.items()}

    inspection_summary = {
        "total_records": total_records,
        "total_columns": total_columns,
        "column_names": list(df.columns),
        "missing_values": missing_values,
        "column_types": column_types,
        "subjects": [s for s in subjects if s in df.columns]
    }
    return inspection_summary


def assign_grade(average_mark: float) -> str:
    """
    Assign a letter grade based on a clearly defined grading scale:
      - 90% and above : A+ (Outstanding)
      - 80% to 89.99% : A  (Excellent)
      - 70% to 79.99% : B  (Very Good)
      - 60% to 69.99% : C  (Good)
      - 50% to 59.99% : D  (Satisfactory)
      - Below 50%     : F  (Fail / Needs Improvement)
    """
    if average_mark >= 90.0:
        return 'A+'
    elif average_mark >= 80.0:
        return 'A'
    elif average_mark >= 70.0:
        return 'B'
    elif average_mark >= 60.0:
        return 'C'
    elif average_mark >= 50.0:
        return 'D'
    else:
        return 'F'


def evaluate_pass_fail(
    student_row: pd.Series,
    subjects: List[str] = DEFAULT_SUBJECTS,
    min_subject_mark: float = PASSING_MARK_PER_SUBJECT,
    min_average: float = PASSING_AVERAGE,
    min_attendance: float = MIN_ATTENDANCE_PERCENT
) -> Tuple[str, str]:
    """
    Evaluate student pass/fail status using clearly defined academic criteria:
      1. Must score >= 40 in each individual subject.
      2. Must achieve an overall average >= 50%.
      3. Must maintain attendance >= 75%.
    Returns:
      Tuple[str, str]: (Result: 'Pass' | 'Fail', Remarks: Reason for failure or approval)
    """
    failed_subjects: List[str] = []
    
    # Check individual subject cutoff using loop
    for subj in subjects:
        score = student_row[subj]
        if score < min_subject_mark:
            failed_subjects.append(f"{subj} ({score})")
            
    avg_mark = student_row['Average_Marks']
    attendance = student_row['Attendance']
    
    reasons = []
    if failed_subjects:
        reasons.append(f"Failed in subject(s): {', '.join(failed_subjects)}")
    if avg_mark < min_average:
        reasons.append(f"Average {avg_mark:.2f}% below required {min_average}%")
    if attendance < min_attendance:
        reasons.append(f"Attendance {attendance:.1f}% below minimum {min_attendance}%")
        
    if len(reasons) == 0:
        return ("Pass", "Cleared all academic & attendance requirements")
    else:
        return ("Fail", "; ".join(reasons))


def process_student_records(df: pd.DataFrame, subjects: List[str] = DEFAULT_SUBJECTS) -> pd.DataFrame:
    """
    Process student data:
      - Uses NumPy for vectorized matrix summation and average computation.
      - Uses explicit loops to assign grades and determine pass/fail status.
    Returns:
      pd.DataFrame: Augmented DataFrame with Total_Marks, Average_Marks, Grade, Result, Remarks.
    """
    processed_df = df.copy()

    # NumPy numerical calculation: Convert subject columns to NumPy 2D array
    marks_matrix = processed_df[subjects].to_numpy(dtype=float)
    
    # Vectorized NumPy calculations for row sums and means
    totals = np.sum(marks_matrix, axis=1)
    averages = np.mean(marks_matrix, axis=1)

    processed_df['Total_Marks'] = np.round(totals, 2)
    processed_df['Average_Marks'] = np.round(averages, 2)

    # Use loops where iteration is required across student records
    grades: List[str] = []
    results: List[str] = []
    remarks: List[str] = []

    for index, row in processed_df.iterrows():
        # Assign grade
        grade = assign_grade(row['Average_Marks'])
        grades.append(grade)

        # Evaluate pass / fail condition
        status, reason = evaluate_pass_fail(row, subjects)
        results.append(status)
        remarks.append(reason)

    processed_df['Grade'] = grades
    processed_df['Result'] = results
    processed_df['Remarks'] = remarks

    return processed_df


def compute_overall_statistics(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Find highest, lowest, and average performance using NumPy and Pandas.
    """
    averages_arr = df['Average_Marks'].to_numpy()

    class_avg = float(np.mean(averages_arr))
    class_median = float(np.median(averages_arr))
    class_std = float(np.std(averages_arr))
    highest_avg = float(np.max(averages_arr))
    lowest_avg = float(np.min(averages_arr))

    # Highest performing student
    top_student_idx = np.argmax(averages_arr)
    top_student_row = df.iloc[top_student_idx]

    # Lowest performing student
    low_student_idx = np.argmin(averages_arr)
    low_student_row = df.iloc[low_student_idx]

    # Pass / Fail counts using NumPy boolean indexing
    results_arr = df['Result'].to_numpy()
    total_students = len(results_arr)
    pass_count = int(np.sum(results_arr == 'Pass'))
    fail_count = int(np.sum(results_arr == 'Fail'))
    pass_percentage = (pass_count / total_students) * 100.0 if total_students > 0 else 0.0

    return {
        "total_students": total_students,
        "class_average": round(class_avg, 2),
        "class_median": round(class_median, 2),
        "class_std_dev": round(class_std, 2),
        "highest_average": round(highest_avg, 2),
        "top_student": {
            "id": top_student_row['StudentID'],
            "name": top_student_row['Name'],
            "department": top_student_row['Department'],
            "average": top_student_row['Average_Marks'],
            "grade": top_student_row['Grade']
        },
        "lowest_average": round(lowest_avg, 2),
        "lowest_student": {
            "id": low_student_row['StudentID'],
            "name": low_student_row['Name'],
            "department": low_student_row['Department'],
            "average": low_student_row['Average_Marks'],
            "grade": low_student_row['Grade']
        },
        "pass_count": pass_count,
        "fail_count": fail_count,
        "pass_percentage": round(pass_percentage, 2)
    }


def analyze_subject_performance(df: pd.DataFrame, subjects: List[str] = DEFAULT_SUBJECTS) -> pd.DataFrame:
    """
    Generate comprehensive subject-wise performance analysis using loops and NumPy.
    Calculates Average, Median, Std Dev, Max, Min, Top Scorer, and Pass Rate.
    """
    subject_stats = []

    # Iterate through each subject using a loop
    for subj in subjects:
        scores = df[subj].to_numpy()

        subj_mean = float(np.mean(scores))
        subj_median = float(np.median(scores))
        subj_std = float(np.std(scores))
        subj_max = float(np.max(scores))
        subj_min = float(np.min(scores))

        # Top scorer for this subject
        max_idx = np.argmax(scores)
        top_scorer_name = df.iloc[max_idx]['Name']

        # Pass rate in this subject (Score >= 40)
        passed_in_subject = int(np.sum(scores >= PASSING_MARK_PER_SUBJECT))
        pass_rate = round((passed_in_subject / len(scores)) * 100.0, 2)

        subject_stats.append({
            "Subject": subj,
            "Average": round(subj_mean, 2),
            "Median": round(subj_median, 2),
            "Highest": subj_max,
            "Top_Scorer": top_scorer_name,
            "Lowest": subj_min,
            "Std_Dev": round(subj_std, 2),
            "Pass_Rate_%": pass_rate
        })

    subject_df = pd.DataFrame(subject_stats)
    return subject_df


def get_top_performers(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """
    Identify and rank the top n performing students based on Average Marks.
    """
    sorted_df = df.sort_values(by='Average_Marks', ascending=False).reset_index(drop=True)
    top_n = sorted_df.head(n).copy()
    
    # Create rank list using loop
    ranks = []
    for i in range(len(top_n)):
        ranks.append(f"Rank {i + 1}")
    top_n.insert(0, 'Rank', ranks)
    
    return top_n[['Rank', 'StudentID', 'Name', 'Department', 'Total_Marks', 'Average_Marks', 'Grade', 'Attendance', 'Result']]


def analyze_department_performance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze student academic performance grouped by Department.
    """
    dept_group = df.groupby('Department')
    dept_stats = []

    for dept_name, group in dept_group:
        student_count = len(group)
        dept_avg = float(np.mean(group['Average_Marks'].to_numpy()))
        dept_att = float(np.mean(group['Attendance'].to_numpy()))
        passed_count = int(np.sum(group['Result'].to_numpy() == 'Pass'))
        pass_rate = round((passed_count / student_count) * 100.0, 2)

        dept_stats.append({
            "Department": dept_name,
            "Total_Students": student_count,
            "Department_Average": round(dept_avg, 2),
            "Average_Attendance_%": round(dept_att, 2),
            "Passed": passed_count,
            "Pass_Rate_%": pass_rate
        })

    return pd.DataFrame(dept_stats).sort_values(by="Department_Average", ascending=False).reset_index(drop=True)


def answer_practical_questions(
    df: pd.DataFrame,
    overall_stats: Dict[str, Any],
    subject_df: pd.DataFrame
) -> Dict[str, str]:
    """
    Directly answers the practical questions specified in Step 4 of the project guidelines:
      1. Which student has the highest average?
      2. Which subject has the best average?
      3. How many students passed?
      4. What is the overall class average?
    """
    top_stud = overall_stats['top_student']
    highest_avg_str = f"{top_stud['name']} ({top_stud['id']} - {top_stud['department']}) with an average of {top_stud['average']}% (Grade: {top_stud['grade']})"

    # Best subject
    best_subject_row = subject_df.sort_values(by='Average', ascending=False).iloc[0]
    best_subject_str = f"{best_subject_row['Subject']} with an average score of {best_subject_row['Average']} / 100"

    # Pass count
    pass_str = f"{overall_stats['pass_count']} out of {overall_stats['total_students']} students ({overall_stats['pass_percentage']}%)"

    # Class average
    class_avg_str = f"{overall_stats['class_average']}%"

    return {
        "highest_student_average": highest_avg_str,
        "best_subject_average": best_subject_str,
        "students_passed": pass_str,
        "overall_class_average": class_avg_str
    }
