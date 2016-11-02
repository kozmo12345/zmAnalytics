select zm_date, code, min(maxc_msc)
from zma where 
msr_mdr > 1 and smsr_mdr > 1
and second >= 37800
and grad <= 0
and rgrad > 1.1
and mesu < 20
and srgrad > -0.01
group by zm_date, code
order by min(maxc_msc)