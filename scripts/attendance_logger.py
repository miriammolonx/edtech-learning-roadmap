def check_attendance_status(student_id, present_days, total_school_days):
    """
    Analyzes student attendance to identify 'At-Risk' students 
    who fall below the mandatory threshold (e.g., 80%).
    
    Args:
        student_id (str): Unique ID of the student
        present_days (int): Days attended
        total_school_days (int): Total instructional days
    """
    if total_school_days == 0:
        return "Error: Total days cannot be zero."
    
    attendance_rate = (present_days / total_school_days) * 100
    attendance_rate = round(attendance_rate, 2)
    
    status = "Good Standing"
    if attendance_rate < 80.0:
        status = "⚠️ AT RISK (Below 80%)"
    elif attendance_rate < 90.0:
        status = "Warning"
        
    return {
        "id": student_id,
        "rate": f"{attendance_rate}%",
        "status": status
    }

# --- Test Case ---
# Student 101 has attended 35 out of 50 days
student_data = check_attendance_status("STU-101", 35, 50)
print(f"Attendance Report: {student_data}")
