select * from anal as a left join
(select day, code, min(mesutime) mt
from anal
group by day, code) as t on a.be < 3
where a.day = t.day and a.code = t.code and a.mesutime = t.mt
and t.mt < '2016-11-07 09:10:00'
order by a.day