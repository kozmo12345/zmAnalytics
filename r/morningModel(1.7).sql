declare @ming int 
declare @maxg int 
declare @dgr int 
declare @cost int 
declare @rate float
declare @grad float
declare @grad2 float

set @cost = 3000000 --가격
set @ming = 2    --grade 최소값
set @maxg = 20    --grade 최소값
set @dgr = 1000000 --gr최소값
set @rate = 30
set @grad = -1.6
set @grad2 = 1

select zm_date, code, min(maxc_msc)
from zma where gr > 460000 and grade >= 0 and grade <= 30 
and grad >= 0.7 and srgrad > -0.01
and second >= 32500 and second < 34000
and msr_mdr > 1 and smsr_mdr > 1
group by zm_date, code
order by min(maxc_msc)
