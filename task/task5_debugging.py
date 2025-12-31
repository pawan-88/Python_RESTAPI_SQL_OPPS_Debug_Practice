import csv
from datetime import datetime
import os


input_file = r'C:\Users\2001k\OneDrive\Desktop\Primis_Tech_Assement_Python\data\employees.csv'

def read_employees(file):
    employees = []

    # Bug1: Added error handling and proper file closing
    try:
        # Check if file exists
        if not os.path.exists(file):
            print(f"Error: File '{file}' not found")
            return []
        
        f = open(file, "r")
        reader = csv.DictReader(f)
        
        for row in reader:
            # Bug2: Convert salary to float with error handling
            try:
                row["salary"] = float(row["salary"])
            except ValueError:
                print(f"Warning: Invalid salary for employee {row.get('name', 'Unknown')}")
                continue
            
            employees.append(row)
        
        f.close()  # Bug3: Added file close

    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return employees

def average_salary_by_department(employees):
    dept_salary = {}
    dept_count = {}
    
    for emp in employees:
        dept = emp["department"]
        
        if dept not in dept_salary:
            dept_salary[dept] = 0
            dept_count[dept] = 0  # Bug4: Initialize dept_count[dept] to 0
        
        dept_salary[dept] += emp["salary"]
        dept_count[dept] += 1
    
    avg_salary = {}
    for d in dept_salary:
        # Bug5: Added check to prevent division by zero
        if dept_count[d] > 0:
            avg_salary[d] = dept_salary[d] / dept_count[d]
    
    return avg_salary


def employees_joined_2023(employees):
    result = []
    
    for emp in employees:
        try:
            # Bug6: Changed date format from "%Y/%m/%d" to "%Y-%m-%d"
            join_date = datetime.strptime(emp["join_date"], "%Y-%m-%d")
            
            # Bug7: Compare year as integer, not string
            if join_date.year == 2023:
                result.append(emp)
        except ValueError:
            print(f"Warning: Invalid date format for employee {emp.get('name', 'Unknown')}")
            continue
    
    return result


def main():
    employees = read_employees(input_file)
    
    if not employees:
        print("No employees loaded. Exiting...")
        return
    print("Total Employees:", len(employees))
    
    avg = average_salary_by_department(employees)
    print("\nAverage Salary by Department:")
    for dept, salary in avg.items():
        print(f"  {dept}: ${salary:.2f}")
    
    joined_2023 = employees_joined_2023(employees)
    print(f"\nEmployees joined in 2023: {len(joined_2023)}")
    
    # details of employees who joined in 2023
    for emp in joined_2023:
        print(f"  - {emp['name']} ({emp['department']})")


# Bug8: Added proper execution guard
if __name__ == "__main__":
    main()