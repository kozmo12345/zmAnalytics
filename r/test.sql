/****** SSMS의 SelectTopNRows 명령 스크립트 ******/
--delete from anal

select (maxRate - rate) as bene, (maxTime - mesuTime) as interval, * from anal
left join 
(
SELECT today, code, min(mesutime) mesut, count(*) cnt
  FROM [zm].[dbo].[anal]
  group by today, code 
) as t on anal.gr > 1
where anal.today = t.today and anal.code = t.code and anal.mesuTime = t.mesut 
order by (maxRate - rate)
--order by (t.today)

select (maxRate - nextrate) as bene, (maxTime - mesuTime) as interval, * from anal
order by (maxRate - nextrate)


select (maxRate - nextrate) as bene, (maxTime - mesuTime) as interval, * from anal
left join 
(
SELECT today, code, min(mesutime) mesut, count(*) cnt
  FROM [zm].[dbo].[anal]
  group by today, code 
) as t on anal.gr > 1
where anal.today = t.today and anal.code = t.code and anal.mesuTime = t.mesut 
--order by (maxRate - nextrate)
order by (t.today)


select today, count(*)
from anal
group by today