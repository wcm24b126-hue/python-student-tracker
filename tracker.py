def calculate_grade(score):
    if score >= 75: return "A (Distinction) 🏆"
    elif score >= 65: return "B (Very Good)"
    elif score >= 55: return "C (Credit)"
    elif score >= 45: return "S (Pass)"
    else: return "W (Fail) - Keep pushing, machan! 💪"

print("--- University Grade Tracker ---")
subject = input("Enter Subject Name: ")
marks = int(input(f"Enter your marks for {subject}: "))

result = calculate_grade(marks)
print(f"\nResults for {subject}:")
print(f"Final Grade: {result}")
