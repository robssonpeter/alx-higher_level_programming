-- List shows
-- by genres
SELECT tv_shows.title, tv_genres.name, COUNT(tv_show_genres.genre_id) no_of_shows FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_shows.title ORDER BY tv_shows.title ASC;

SELECT tv_shows.title, tv_genres.name, COUNT(tv_show_genres.show_id) FROM tv_genres LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id;
