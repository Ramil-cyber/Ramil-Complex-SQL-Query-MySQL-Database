CREATE TABLE {table_name} AS
SELECT 
    ID,
    Player,
    Position,
    CAST(Draft_Year as int ) as Draft_Year,
    CAST(Projected_SPM as float)  as Projected_SPM,
    CAST(Superstar as float) as Superstar,
    CAST(Starter as float) as Starter,
    CAST(Role_Player as float) as Role_Player,
    CAST(Bust as float) as Bust
FROM NbaDraft;
