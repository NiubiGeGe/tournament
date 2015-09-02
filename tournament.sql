-- Table definitions for the tournament project.

-- Drop database tournament if exists to prevent any duplicate database
DROP DATABASE IF EXISTS tournament;
-- create database
CREATE DATABASE tournament;
-- connect to database
\c tournament

-- create player table
CREATE TABLE players(
    player_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    matches INTEGER DEFAULT 0,
    draw INTEGER DEFAULT 0
);

-- create match player
CREATE TABLE matches(
    match_id serial primary key,
    winner integer references players(player_id) ON DELETE CASCADE,
    loser integer references players(player_id) ON DELETE CASCADE,
    CHECK (winner <> loser)
);
