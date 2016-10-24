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


select zm_date, code, max(maxc_msc) from zma where gr > @dgr and grade >= @ming and grade <= @maxg and grad < @grad and second >= 32470
group by zm_date, code
union all
select zm_date, code, max(maxc_msc) from zma where gr > @dgr and grade >= @ming and grade <= @maxg and grad > @grad2 and second >= 32500
group by zm_date, code
order by zm_date
