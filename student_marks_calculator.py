import pandas as pd   
 
df = pd.read_csv("student.csv") 

df["total"] = df["Physics"] + df["Chemistry"] + df["Maths"] 

df["percentage"] = df["total"] / 300 

def grade_function(percentage): 
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
         
df["grade"] = df["percentage"].apply(get_grades)


df["Rank"] = (
    df["Percentage"]
    .rank(ascending=False, method="dense")
    .astype(int)
)

df = df.sort_values(by="Rank")

topper = df.iloc[0]


print(df)


print(f"Name: {topper['Name']}") 
print(f"Percentage: {topper['Percentage']:.2f}%")
print(f"Grade: {topper['Grade']}")
 


print(f"Physics: {df['Physics'].mean():.2f}")
print(f"Chemistry: {df['Chemistry'].mean():.2f}")
print(f"Maths: {df['Maths'].mean():.2f}")


df.to_csv("student_report.csv", index=False)

print("Report saved as 'student_report.csv'") 
