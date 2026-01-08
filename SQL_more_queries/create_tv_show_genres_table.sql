CREATE TABLE IF NOT EXISTS tv_show_genres (
    tv_show_id INT,
    genre_id INT,
    PRIMARY KEY (tv_show_id, genre_id),
    FOREIGN KEY (tv_show_id) REFERENCES tv_shows(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);
