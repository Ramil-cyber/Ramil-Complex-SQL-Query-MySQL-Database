select Draft_Year, Position, count(*)
from NbaDraftTransformed
Group by Draft_Year, Position

