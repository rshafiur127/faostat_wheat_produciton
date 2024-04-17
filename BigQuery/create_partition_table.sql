
-- We used the following query to create the partition table from the non-partitioned table

create or replace table dtc-de-411905.project.qcl_wheat_produce_part
partition by DATETIME_TRUNC(year, YEAR) 
cluster by area
as select * from dtc-de-411905.project.qcl_wheat_produce;
