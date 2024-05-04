# insert_utility
inserting a csv file to mysql table using python.

if you want to insert the values to the table using the file, it will check if the record is present it will not insert if not it will insert the new records.

This is my table, now I want to insert values to this table.

mysql> select * from dependencydtls;
+----+----------------+----------------------+-----------------+---------------------+-----------+----------+-----------+
| id | depedentdbname | dependenttblname     | dependent_jobid | createdon           | createdby | masterid | frequency |
+----+----------------+----------------------+-----------------+---------------------+-----------+----------+-----------+
|  1 | flexcube_uae   | fttb_contract_master |            1179 | 2024-05-04 09:15:40 | gray      |        9 | daily     |
+----+----------------+----------------------+-----------------+---------------------+-----------+----------+-----------+
1 row in set (0.00 sec)

my csv file

depedentdbname,dependenttblname,dependent_jobid,createdby,frequency
flexcube_india,actb_history,2001,gray,daily
ops_volume_sla_preprod,ictb_icalc_final,1009,gray,daily
flexcube_uae,fttb_contract_master,1179,gray,daily


so 2 new records will be inserted 
the command for running the file. one input will be the csv file and will be masterid.
python insert_utility.py dependency_list.csv 9

The table after insertion.

mysql> select * from dependencydtls;
+----+------------------------+----------------------+-----------------+---------------------+-----------+----------+-----------+
| id | depedentdbname         | dependenttblname     | dependent_jobid | createdon           | createdby | masterid | frequency |
+----+------------------------+----------------------+-----------------+---------------------+-----------+----------+-----------+
|  1 | flexcube_uae           | fttb_contract_master |            1179 | 2024-05-04 09:15:40 | gray      |        9 | daily     |
| 28 | flexcube_india         | actb_history         |            2001 | 2024-05-04 20:30:41 | gray      |        9 | daily     |
| 29 | ops_volume_sla_preprod | ictb_icalc_final     |            1009 | 2024-05-04 20:30:42 | gray      |        9 | daily     |
+----+------------------------+----------------------+-----------------+---------------------+-----------+----------+-----------+
3 rows in set (0.00 sec)

