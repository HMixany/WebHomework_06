SELECT groups.name AS GroupName, ROUND(AVG(g.grade), 2) AS AverageGrade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN groups ON s.group_id = groups.id
WHERE g.subject_id = 1
GROUP by groups.name
ORDER by groups.name;