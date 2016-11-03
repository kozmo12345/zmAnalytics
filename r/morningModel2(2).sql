select zm_date, code, min(maxc_msc), min(second)
from zma where gr > 1000000 and grade >= 0 and grade <= 30 
and grad >= 0.7 and srgrad > -0.01
and second >= 32500 and second < 34000
and msr_mdr > 1 and smsr_mdr > 1
group by zm_date, code
order by min(maxc_msc)