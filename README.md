

# nba crawler

Acquire fixtures and results for upcoming season and historic seasons.

## Crawlers

1. Fixtures crawler

Call the ESPN API for all future dates not yet processed
Model Python classes for:
    - Season
    - SeasonDates 
    - Games
    - Teams

Deserialise JSON response for each game to the above objects

For each response, write data to the database.