SELECT s.full_name AS StudentName
FROM groups g
JOIN students s ON g.id = s.group_id
WHERE g.id = 2
ORDER BY StudentName;