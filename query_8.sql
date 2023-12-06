SELECT t.full_name AS TeacherName, subjects.name AS SubjectName, AVG(grades.grade) AS AverageGrade
FROM teachers t
JOIN subjects ON t.id = subjects.teacher_id
JOIN grades ON subjects.id = grades.subject_id
JOIN students ON grades.student_id = students.id
WHERE t.id = 1
GROUP by t.full_name, subjects.name
ORDER by TeacherName, SubjectName;