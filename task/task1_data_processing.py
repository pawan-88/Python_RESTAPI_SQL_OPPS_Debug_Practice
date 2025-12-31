import csv
from datetime import datetime
import os

input_file = r'C:\Users\2001k\OneDrive\Desktop\Primis_Tech_Assessment_Python\data\employees.csv'
output_file = r'C:\Users\2001k\OneDrive\Desktop\Primis_Tech_Assessment_Python\output\employees_2023.csv'

 
def load_emp(input_file):
    employees = []

    try:
        # Check if file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        with open(input_file, 'r') as file:  # open file
            reader = csv.DictReader(file)
            for row in reader:               # read all rows
                row["salary"] = float(row["salary"]) # convert salary to number
                row["join_date"] = datetime.strptime(row["join_date"], "%Y-%m-%d") # convert date string to datetime
                employees.append(row)
            
        return employees
    

    except FileNotFoundError as e:
        print(f"Error: {e}")


# function to count total employees
def get_total_employees(employees):
    return len(employees)

# calculate average salary by department
def get_avg_salary_department(employees):
    department_salary = {}

    # collect all salaries by department
    for emp in employees:
        dept = emp["department"]
        salary = emp["salary"]

        if dept not in department_salary:
            department_salary[dept] = []

        department_salary[dept].append(salary)

    average_salary = {}
    for dept, salaries in department_salary.items(): # calculate averages
        average_salary[dept] = sum(salaries) / len(salaries)

    return average_salary

# find department with highest average salary
def get_highest_avg_department(average_salary):
    return max(average_salary, key=average_salary.get)

# function to find employees with maximum salary
def get_highest_paid_employees(employees):
    max_salary = max(emp["salary"] for emp in employees)
    return [emp for emp in employees if emp["salary"] == max_salary]

#employees joined in 2023
def get_employees_joined_2023(employees):
    return [emp for emp in employees if emp["join_date"].year == 2023]

# save employees to csv file
def save_employees_csv(employees, OUTPUT_FILE):
    if not employees:
        print("No employees to save")
        return
    
    try:

        with open(OUTPUT_FILE, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=employees[0].keys())
            writer.writeheader()

            for emp in employees:
             emp_copy = emp.copy()
             emp_copy["join_date"] = emp_copy["join_date"].strftime("%Y-%m-%d")
             writer.writerow(emp_copy)

    except Exception as e:
        print(f"Error while saving file: {e}")


def main():
    employees = load_emp(input_file)

    # Get Total Employees
    print("Total Employees:", get_total_employees(employees))

    # Get Average Salary by Department
    average_salary = get_avg_salary_department(employees)
    print("\nAverage Salary by Department:")
    for dept, avg in average_salary.items():
        print(dept, ":", round(avg, 2))

    # Get Department with highest average salary
    highest_dept = get_highest_avg_department(average_salary)
    print("\nDepartment with Highest Average Salary:", highest_dept)

    # Get Employees with highest salary
    print("\nHighest Paid Employee(s):")
    for emp in get_highest_paid_employees(employees):
        print(emp["name"], "-", emp["salary"])

    # Get Employees who joined in 2023
    joined_2023 = get_employees_joined_2023(employees)
    print("\nEmployees who joined in 2023:",joined_2023)

    # Export 2023 employees to employees_2023.csv
    save_employees_csv(joined_2023, output_file)
    print("\nEmployees joined in 2023 saved to:", output_file)


if __name__ == "__main__":
    main()
