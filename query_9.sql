SELECT DISTINCT students.full_name AS StudentName, subjects.name AS CourseName
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.id = 1
ORDER BY CourseName;