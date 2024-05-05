-- 1. all tasks from one user, user_id = 1
SELECT *
FROM tasks
WHERE user_id=1;

-- 2. all tasks with the same status, status_id = 3
SELECT *
FROM tasks
WHERE status_id=3;

-- 3. set new status 2 for a selected task, task_id = 2
UPDATE tasks SET status_id  = 2 WHERE id = 2;

-- 4. users without tasks
SELECT * 
FROM users 
WHERE id NOT IN (SELECT user_id
	FROM tasks
);

-- 5. add new task for a user, user_id = 2
INSERT into tasks (title, description, status_id, user_id)
VALUES ("Call an important customer", "because we want more money", 1, 2)

-- 6. delete a task with id 6
DELETE FROM tasks
WHERE id = 6;

-- 7. select users with "ro" in their emails
SELECT *
FROM users
WHERE email LIKE "%ro%";

-- 8. update name of a user
UPDATE users SET fullname = "Alexandr Johnson" WHERE id = 3;

-- 9. get number of tasks of each typr
SELECT COUNT(status_id) as total_number, status_id
FROM tasks 
GROUP BY status_id;

-- 10. get tasks from users who has "@example.com" as a domain of email
SELECT * 
FROM tasks
JOIN users ON users.id = tasks.user_id
WHERE users.email LIKE "%@example.com";

-- 11. get tasks w/o description
SELECT *
FROM tasks
WHERE description IS NULL;

-- 12. select users with tasks with status "in progress"
SELECT * 
FROM tasks
JOIN users ON users.id = tasks.user_id
WHERE tasks.status_id IN (SELECT id 
	FROM status 
	WHERE name = "in progress")
GROUP BY users.id;

-- 13. get users and number of their tasks
SELECT users.fullname,  COUNT(tasks.user_id) as total_number
FROM users
LEFT JOIN tasks ON users.id = tasks.user_id
GROUP BY users.fullname;
