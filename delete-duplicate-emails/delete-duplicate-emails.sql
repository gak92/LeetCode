# Write your MySQL query statement below
​
#DELETE p1 FROM Person as p1, Person as p2 WHERE p1.Email = p2.Email AND p1.Id > p2.Id;
​
​
DELETE FROM person 
WHERE id NOT IN (
    SELECT id 
    FROM (
        SELECT MIN(id) AS id 
        FROM person 
        GROUP BY email
    ) AS id
)
​
​
​
# DELETE FROM Person
# WHERE Id <> (
#     SELECT Id
#     FROM (
#         SELECT * FROM Person
#     ) as P
#       WHERE Email = Person.Email
#       ORDER BY Id
#       LIMIT 1
# )
​
​
