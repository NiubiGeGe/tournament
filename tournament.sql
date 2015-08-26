-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- create table players(player_id serial primary key, name text, matches integer DEFAULT 0, draw integer DEFAULT 0);

-- create table matches(match_id serial primary key, player_1 integer references players(player_id), player_2 integer references players(player_id), winner integer references players(player_id), loser integer references players(player_id));


