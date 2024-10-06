Select Position ,Draft_Year, avg(Superstar)
from NbaDraftTransformed 
Group by Position, Draft_Year
HAVING avg(Superstar) > 0.02;