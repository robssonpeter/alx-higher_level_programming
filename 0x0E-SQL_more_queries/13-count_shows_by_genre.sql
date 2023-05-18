-- List shows
-- by genres
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows FROM tv_genres LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id GROUP BY tv_genres.name ORDER BY COUNT(tv_show_genres.genre_id) DESC;
