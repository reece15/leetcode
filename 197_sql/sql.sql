
select w1.id as Id 
from Weather w1 left join Weather w2
on (date_sub(w1.`RecordDate`, interval 1 day) = w2.`RecordDate`)
where w1.`Temperature` > w2.`Temperature`