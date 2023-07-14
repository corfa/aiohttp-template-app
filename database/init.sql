\c tasks;
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT
);

INSERT INTO tasks (description)
VALUES
    ('Task 1'),
    ('Task 2'),
    ('Task 3');
