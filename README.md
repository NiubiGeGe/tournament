# tournament
tournament

## Quick Start:

  1. This file requires the installation of [psycopg2] (http://initd.org/psycopg/) in order to enter psql command line interface.
  2. Clone the repo: ```git clone https://github.com/jowangz/tournament.git```
  3. Import the database schema by using command ```psql -f tournament.sql```
  4. To test to code: ```python tournament_test.py```
  5. ```Success!  All tests pass!``` will be shown if the code ran successfully.

## Basic psql commands:
  * Use command ```psql tournament``` to enter command line interface.
  * Use hot key ```control + D``` to exit command line interface.

## What's included:

```
  movies/
│   ├── tournament.py
│   ├── tournament.sql
│   ├── tournament_test.py
│   ├── README.md
```

## Features:
  
  * The code includes 9 differenct test case.
  * This is a simple swiss pairing python application. It makes matches based on
    the ranking of individual player. This version supports draw game.


## Creator:

**Zheng Wang**

* https://github.com/jowangz

**Udacity**

* https://udacity.com
