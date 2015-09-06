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
    matches_played INTEGER DEFAULT 0,
    draw_encountered INTEGER DEFAULT 0
);

-- create match table, leave winner as normal integer because of the draw function
CREATE TABLE matches(
    match_id SERIAL primary key,
    player_1_id INTEGER references players(player_id) ON DELETE CASCADE,
    player_2_id INTEGER references players(player_id) ON DELETE CASCADE,
    winner INTEGER
);

-- create player_standings_view 
CREATE VIEW player_standings_view AS
    SELECT player_id, name,
    count(players.player_id = matches.winner)::integer as wins,
    players.matches_played, draw_encountered
    FROM players LEFT JOIN matches on players.player_id = matches.winner
    GROUP BY players.player_id
    ORDER BY wins DESC;
