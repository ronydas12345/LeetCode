# Write your MySQL query statement below
/*
with val as (
    select 
        tiv_2016,
        lat,
        lon,
    from Insurance
    where 
        tiv_2016 = tiv_2015
)

with loc as (
    select
        tiv_2016,
        lat,
        lon,
    from Insurance
    where
        lat is distinct
)
*/

select 
    round(
        sum(tiv_2016)
        , 2
    ) as tiv_2016
from Insurance
where
    (lat, lon) in (
        select
            lat,
            lon
        from Insurance
        group by lat, lon
        having
            count(*) = 1
    ) and
    tiv_2015 in (
        select 
            tiv_2015
        from Insurance
        group by tiv_2015
        having count(*) > 1
    )
;