CREATE TABLE Departments (
    DeptID INT,
    DeptName VARCHAR(50)
);

SELECT *
FROM Students
INNER JOIN Departments
ON Students.StudentID = Departments.DeptID;