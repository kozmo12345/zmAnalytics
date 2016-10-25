drop table #temta 
drop table #temta2

declare @ming int 
declare @maxg int 
declare @dgr int 
declare @cost int 
declare @rate float
declare @grad float
declare @grad2 float

set @cost = 3000000 --°¡°Ý
set @ming = 2    --grade ÃÖ¼Ò°ª
set @maxg = 20    --grade ÃÖ¼Ò°ª
set @dgr = 1000000 --grÃÖ¼Ò°ª
set @rate = 30
set @grad = -1.6
set @grad2 = 1


select *
into #temta
from zma where gr > @dgr and grade >= @ming and grade <= @maxg and grad < @grad and second >= 32450
order by zm_date

select *
into #temta2
from zma where gr > @dgr and grade >= @ming and grade <= @maxg and grad > @grad2 and second >= 32500

select "second",avg(maxc_msc),count(*) from #temta
group by "second"

select "second", avg(maxc_msc),count(*)   from #temta2
group by "second"
