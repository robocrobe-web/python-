import sys
print(sys.executable)  


import pandas as pd       
 
 # Load CSV file
df = pd.read_csv("students.csv")

# Calculate Total Marks
df["Total"] = (
    df["Physics"] + df["Chemistry"] + df["Maths"])  

# Calculate Percentage 
df["Percentage"] =(df["Total"] / 300) * 100
 
# Grade Function
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60: 
        return "C"
    else:
        return "F"

# Apply Grades
df["Grade"] = df["Percentage"].apply(get_grade)

# Rank Students
df["Rank"] = (
    df["Percentage"]
    .rank(ascending=False, method="dense")
    .astype(int)
)

# Sort by Rank
df = df.sort_values(by="Rank")

#  Topper Information
topper = df.iloc[0]

print("\n===== STUDENT RESULT REPORT =====\n")
print(df)


print(f"Topper's Name: {topper['Name']}")  
print(f"Percentage: {topper['Percentage']:.2f}%")
print(f"Grade: {topper['Grade']}")
 
# Subject-wise Averages 

print(f"Physics: {df['Physics'].mean():.2f}")
print(f"Chemistry: {df['Chemistry'].mean():.2f}")
print(f"Maths: {df['Maths'].mean():.2f}")

# Save Report
df.to_csv("student_report.csv", index=False)

print("\nReport saved as 'student_report.csv'")    
 

