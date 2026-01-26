def calculate_weighted_average(scores, weights):
    """
    Calculates the final grade based on weighted components.
    Commonly used in Learning Management Systems (LMS) backend logic.
    
    Args:
        scores (list): A list of raw scores [Exam, Quiz, Project]
        weights (list): A list of weights in decimals [0.50, 0.20, 0.30]
    """
    if len(scores) != len(weights):
        return "Error: Scores and weights must match in length."
    
    final_grade = 0
    for i in range(len(scores)):
        final_grade += scores[i] * weights[i]
        
    return round(final_grade, 2)

# --- Test Case ---
# Scenario: 50% Exam, 20% Quiz, 30% Project
current_scores = [85, 90, 95] 
current_weights = [0.50, 0.20, 0.30]

result = calculate_weighted_average(current_scores, current_weights)
print(f"Student Final Grade: {result}")
