# comsci assessment

def get_grade_input(quarter):
    while True:
        try:
            grade = float(input(f"Enter {quarter} Quarter Grade: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

def get_rating(average):
    if 96 <= average <= 100:
        return "Excellent"
    elif 91 <= average <= 95:
        return "Very Good"
    elif 86 <= average <= 90:
        return "Good"
    elif 81 <= average <= 85:
        return "Satisfactory"
    elif 76 <= average <= 81:  # Note: you said 76-81, overlaps with 81 above
        return "Substandard"
    else:  # below 76
        return "Fail"

# Get quarter grades
q1 = get_grade_input("First")
q2 = get_grade_input("Second") 
q3 = get_grade_input("Third")
q4 = get_grade_input("Fourth")

# Get summative test
summative = get_grade_input("Summative Test")

# Calculate average of all 5 scores
average = (q1 + q2 + q3 + q4 + summative) / 5

# Get the rating string based on the average
rating = get_rating(average)

# Display the results
print(f"\nYour Average: {average:.2f}")
print(f"Performance Rating: {rating}")