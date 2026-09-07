use hello;
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(30),
    city VARCHAR(30),
    salary DECIMAL(10,2),
    experience INT,
    age INT
);

INSERT INTO employees
(employee_id, employee_name, department, city, salary, experience, age)
VALUES
(1, 'Arun Kumar', 'IT', 'Kochi', 55000, 3, 25),
(2, 'Anjali Nair', 'HR', 'Calicut', 42000, 2, 24),
(3, 'Rahul Das', 'IT', 'Bangalore', 75000, 6, 30),
(4, 'Sneha Thomas', 'Finance', 'Kochi', 62000, 5, 28),
(5, 'Vishnu Raj', 'IT', 'Calicut', 68000, 4, 27),
(6, 'Fathima Ali', 'HR', 'Kochi', 48000, 3, 26),
(7, 'Nikhil Menon', 'Finance', 'Bangalore', 80000, 7, 32),
(8, 'Amal Dev', 'IT', 'Kochi', 59000, 4, 26),
(9, 'Meera Joseph', 'HR', 'Bangalore', 51000, 5, 29),
(10, 'Sanjay Kumar', 'Finance', 'Calicut', 57000, 3, 25),
(11, 'Anu Krishnan', 'IT', 'Bangalore', 72000, 5, 29),
(12, 'Ramesh Babu', 'HR', 'Kochi', 45000, 2, 23),
(13, 'Akhil Raj', 'Finance', 'Kochi', 67000, 4, 27),
(14, 'Neha Suresh', 'IT', 'Calicut', 63000, 3, 25),
(15, 'Manu Mohan', 'HR', 'Calicut', 46000, 2, 24);

select * from employees;

select COUNT(*) as total_employees from employees;

select SUM(salary) as total_salary from employees;

select AVG(salary) as average_salary from employees;


select MAX(salary) as highest_salary from employees;


select MIN(salary) as lowest_salary from employees;


select * from employees where department in ('IT', 'HR');


select * from employees where city in ('Kochi', 'Calicut');


select * from employees where salary in (55000, 62000, 75000);


select * from employees where employee_name like 'A%';


select * from employees where employee_name like '%n';


select * from employees where employee_name like '%ar%';


select * from employees where city like 'K%';


select * from employees where employee_name like 'A____';


select * from employees where employee_name like '_____';


select DISTINCT city from employees where city like '_o%';



select * from employees;