-- Створення таблиці груп
drop table if exists groups CASCADE;
CREATE TABLE groups (
id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);

-- Створення таблиці студентів
drop table if exists students CASCADE;
CREATE TABLE students (
id SERIAL PRIMARY KEY,
full_name VARCHAR(150) NOT NULL,
group_id INTEGER REFERENCES groups(id)
);

-- Створення таблиці викладачів
drop table if exists teachers CASCADE;
CREATE TABLE teachers (
id SERIAL PRIMARY KEY,
full_name VARCHAR(150) NOT NULL
);

-- Створення таблиці предметів
drop table if exists subjects CASCADE;
CREATE TABLE subjects (
id SERIAL PRIMARY KEY,
name VARCHAR(150) NOT NULL,
teacher_id INTEGER REFERENCES teachers(id)
);

-- Створення таблиці оцінок
drop table if exists grades CASCADE;
CREATE TABLE grades (
id SERIAL PRIMARY KEY,
student_id INTEGER REFERENCES students(id),
subject_id INTEGER REFERENCES subjects(id),
grade INTEGER CHECK (grade >= 0 AND grade <= 100),
grade_date DATE NOT NULL
);