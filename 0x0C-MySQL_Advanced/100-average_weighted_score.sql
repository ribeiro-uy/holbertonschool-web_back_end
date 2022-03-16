-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
DECLARE average FLOAT;
SET average = (SELECT (SUM(score * weight)/SUM(weight)) FROM corrections AS newTable INNER JOIN projects ON project_id = id WHERE newTable.user_id=user_id);
UPDATE users SET average_score=average WHERE id=user_id;
END;
|