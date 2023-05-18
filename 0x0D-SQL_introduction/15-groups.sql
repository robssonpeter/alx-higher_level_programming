-- number by score
-- select similar scores
SELECT score, count(id) AS number FROM second_table GROUP BY score;
