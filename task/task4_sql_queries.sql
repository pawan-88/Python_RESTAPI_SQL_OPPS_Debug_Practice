
# Fetch all employees query:-

    SELECT * FROM employees;

# Count employees:-

    SELECT COUNT(*) FROM employees;

# Average salary by department:-

    SELECT 
        department, AVG(salary)
    FROM 
        employees
    GROUP BY 
        department;

# Highest average salary department:-

    SELECT 
        department,
        AVG(salary) AS average_salary
    FROM 
        employees
    GROUP BY 
        department
    ORDER BY 
        average_salary DESC
    LIMIT 1;

# Highest paid employee:- 

    SELECT 
        *
    FROM 
        employees
    WHERE 
        salary = (SELECT MAX(salary) 
    FROM 
        employees);

# Employees joined in 2023:-

    SELECT 
        *
    FROM 
        employees
    WHERE 
        YEAR(join_date) = 2023;

# Count employees per department:-

    SELECT 
        department, 
        COUNT(*) AS employee_count
    FROM 
        employees
    GROUP BY 
        department;