CREATE TABLE IF NOT EXISTS rm564_football_clubs (
    club_id INT,
    club_code STRING,
    name STRING,
    domestic_competition_id STRING,
    total_market_value STRING,  -- Market value is a financial figure but stored as STRING due to possible missing values
    squad_size INT,
    average_age FLOAT,
    foreigners_number INT,
    foreigners_percentage FLOAT,
    national_team_players INT,
    stadium_name STRING,
    stadium_seats INT,
    net_transfer_record STRING,  -- Can include '+' or '-' so stored as STRING
    coach_name STRING,
    last_season INT,  -- Assuming year is stored as INT
    filename STRING,  -- Path to the file
    url STRING        -- URL of the club's page
);