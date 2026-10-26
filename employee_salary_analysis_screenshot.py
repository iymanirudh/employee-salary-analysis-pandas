import pandas as pd
import matplotlib.pyplot as plt

# Employee data
data = {
    "Name": ["Rahul Sharma", "Priya Patel", "Amit Verma", "Sneha Kulkarni",
             "Rohan Desai", "Neha Joshi", "Karan Mehta", "Pooja Nair",
             "Vikram Singh", "Anjali Rao", "Suresh Iyer", "Meera Shah"],
    "Department": ["IT", "HR", "Finance", "IT", "Marketing", "HR",
                   "Finance", "Marketing", "IT", "Finance", "HR", "Marketing"],
    "Salary": [65000, 48000, 72000, 70000, 52000, 50000,
               68000, 55000, 85000, 76000, 46000, 58000]
}
df = pd.DataFrame(data)

# Names, departments and salaries
print("EMPLOYEE DETAILS")
print(df)

# Average salary for each department
avg = df.groupby("Department")["Salary"].mean()
print("\nAVERAGE SALARY BY DEPARTMENT")
print(avg)

# Highest salary
top = df.loc[df["Salary"].idxmax()]
print("\nHIGHEST PAID EMPLOYEE")
print(top["Name"], "-", top["Department"], "-", top["Salary"])

# Bar chart
avg.plot(kind="bar")
plt.title("Average Salary by Department")
plt.show()

# Histogram
plt.hist(df["Salary"], bins=6)
plt.title("Salary Distribution")
plt.show()
