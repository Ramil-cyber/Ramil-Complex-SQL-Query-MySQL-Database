CREATE TABLE players (
    player_id INT,
    first_name STRING,
    last_name STRING,
    name STRING,
    last_season INT,
    current_club_id INT,
    player_code STRING,
    country_of_birth STRING,
    city_of_birth STRING,
    country_of_citizenship STRING,
    date_of_birth TIMESTAMP,
    sub_position STRING,
    position STRING,
    foot STRING,
    height_in_cm INT,
    contract_expiration_date DATE,  -- This column is empty in the given data, but can be useful for future entries
    agent_name STRING,
    image_url STRING,
    url STRING,
    current_club_domestic_competition_id STRING,
    current_club_name STRING,
    market_value_in_eur INT,
    highest_market_value_in_eur INT
);
