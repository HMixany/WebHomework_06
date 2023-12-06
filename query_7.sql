SELECT s.full_name AS StudentName, grades.grade AS Grade, subjects.name AS SubjectName
FROM students s
JOIN grades ON s.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
JOIN groups ON s.group_id = groups.id
WHERE groups.id  = 1 AND subjects.id  = 1
ORDER by StudentName;