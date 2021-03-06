CREATE TABLE t_mp3(
id INT PRIMARY KEY AUTO_INCREMENT,
mp3_name VARCHAR(200) NOT NULL UNIQUE,
mp3_file VARCHAR(200) NOT NULL
);

CREATE TABLE t_user(
id INT PRIMARY KEY AUTO_INCREMENT,
username VARCHAR(200) NOT NULL UNIQUE,
password VARCHAR(200) NOT NULL
);

CREATE TABLE t_play_list(
id INT PRIMARY KEY AUTO_INCREMENT,
uid INT,
mid INT,
CONSTRAINT FOREIGN KEY (uid) REFERENCES t_user (id),
CONSTRAINT FOREIGN KEY (mid) REFERENCES t_mp3 (id)
);