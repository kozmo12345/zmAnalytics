declare @ming int 
declare @maxg int 
declare @dgr int 
declare @cost int 
declare @rate float

set @ming = 2    --grade 최소값
set @maxg = 20    --grade 최소값
set @dgr = 690000 --gr최소값
set @cost = 1000000 --가격
set @rate = 30

       -- 시간 , y갯수,n갯수, y/n 비율, y/n gr 비율, y값 30분 내 최소값 평균, max값 평균
select a.[second], yc, nc, (yc * 1.0/nc* 1.0) as yn_rate, ygr/ngr as grrate, mync, mnc, myc from (
select [second], count(*) as yc, AVG(maxc_msc) as myc, min(msc_min30c) as mync, avg(gr) as ygr from zma
where udm2 = 'Y' and grade >= @ming and grade <= @maxg  and gr > @dgr and cost < @cost and mesu < @rate 
group by [second]
) a left join (
select [second], count(*) as nc, avg(gr) as ngr, min(msc_min30c) as mnc  from zma
where udm2 != 'Y' and grade >= @ming and grade <= @maxg and gr > @dgr and cost < @cost and mesu < @rate 
group by [second]
) b on a.[second] = b.[second]
order by (yc * 1.0/nc* 1.0) desc