SELECT DISTINCT subjects.name AS CourseName
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE students.id = 1 AND teachers.id = 1
ORDER BY CourseName;