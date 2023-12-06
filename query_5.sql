SELECT teachers.full_name AS TeacherName, subjects.name AS CourseName
FROM teachers
JOIN subjects ON teachers.id = subjects.teacher_id
WHERE teachers.id = 1
ORDER BY TeacherName, CourseName;