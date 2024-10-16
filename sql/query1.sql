Select club.name  as club_name, 
SUM(player.market_value_in_eur) as total_market_value,
COUNT(*) as included_players

from ids706_data_engineering.default.rm564_football_clubs_players player
JOIN ids706_data_engineering.default.rm564_football_clubs club ON player.current_club_id = club.club_id
GROUP BY club_name
ORDER BY total_market_value DESC
limit 20 ;