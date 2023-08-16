--  lists all genres from hbtn_0d_tvshows and 
-- displays the number of shows linked to each.
SELECT name
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres_id
LEFT JOIN tv_show ON tv_show_genres.show_id = tv_show.id
WHERE tv_show.title = 'Dexter'
GROUP BY name
ORDER BY name ASC;