#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    #delete all matches.
    players = c.execute("DELETE FROM matches;")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    #delete all players.
    players = c.execute("DELETE FROM players;")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    #count all players currently registered.
    c.execute("SELECT count(*) as num FROM players;")
    player_count = c.fetchone()[0]
    DB.commit()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """

    DB = connect()
    c = DB.cursor()
    #register a player with name.
    c.execute("INSERT INTO players (name) VALUES (%s)", (name,))
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    c = DB.cursor()
    # Return a list of tuples includes player_id, name, wins and number of
    # matches.
    c.execute("""
        SELECT player_id, name,
        count(players.player_id = matches.winner)::integer, players.matches
        FROM players left join matches on players.player_id = matches.winner
        GROUP BY players.player_id
        ORDER BY count(players.player_id = matches.winner)::integer DESC;
        """)
    player_standing = c.fetchall()
    DB.commit()
    DB.close()
    return player_standing


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    # Insert match result into Match table.
    c.execute("""
        INSERT INTO matches (player_1, player_2, winner, loser)
        VALUES (%s, %s, %s, %s)""", (winner, loser, winner, loser))
    # Update winner matches count.
    c.execute("""
        UPDATE players
        SET matches = matches + 1
        WHERE player_id = (%s)""", [winner])
    # Update loser matches count.
    c.execute("""
        UPDATE players SET matches = matches + 1
        WHERE player_id = (%s)""", [loser])
    DB.commit()
    DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    DB = connect()
    c = DB.cursor()
    # Crate a view that ranks all players order by wins.
    c.execute("""
        CREATE VIEW pairings as
        SELECT player_id, name,
        count(players.player_id = matches.winner)::integer as wins
        FROM players left join matches on players.player_id = matches.winner
        GROUP BY players.player_id
        ORDER BY wins DESC;""")
    # Return player_id and name order by players ranking.
    c.execute("""
        SELECT player_id, name
        FROM pairings;""")
    # retrieves an array of all fetch data. 
    pairings = c.fetchall()
    print pairings
    #create an empty list.
    pairings2 = []

    for i in pairings:
        for j in i:
            pairings2.append(j)
    # Return a list of tuples contains (id1, name1, id2, name2)
    it = iter(pairings2)
    pairings2 = zip(it, it, it, it)
    return pairings2
    # Drop the view.
    c.execute("DROP VIEW pairings;")
    DB.commit()
    DB.close()
