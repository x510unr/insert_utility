
import csv
import mysql.connector as c
import sys

conn = c.connect(host='localhost', user='root', password='root', database='prod')

cursor = conn.cursor(buffered=True)


def is_csv(filename):
	return filename.lower().endswith('.csv')



def old_or_new(n):
	query = "select count(*) from dependencydtls where masterid = %d" %n
	
	cursor.execute(query)
	result = cursor.fetchone()
	count = result[0]
	
	if count > 0: return 'old'
	else: return 'new'
	cursor.close()
	conn.close()

def job_check(n):
	query = "select count(*) from dependencydtls where dependent_jobid= %d" %n
	
	cursor.execute(query)
	result = cursor.fetchone()
	count = result[0]
	
	if count > 0: return False
	else: return True



	
def new_insert():
	
	with open(sys.argv[1]) as f:
		f_csv = csv.reader(f)
		headers = next(f_csv)
		#print(headers)
		lower_headers = [header.lower() for header in headers]
		if ['depedentdbname','dependenttblname','dependent_jobid','createdby','frequency'] == lower_headers:
			for row in f_csv:
				query="""insert into dependencydtls (depedentdbname, dependenttblname, dependent_jobid, createdby,masterid, frequency)
	values(%r, %r, %d, %r, %d, %r)""" %(row[0], row[1], int(row[2]), row[3], masterid,row[4])
				
				cursor.execute(query)
				conn.commit()
				#print('%r' %query)
		else: print("check the header names again")
		
		
		f.close()
		cursor.close()
		conn.close()

		



def old_insert():

	with open(sys.argv[1]) as f:
		f_csv = csv.reader(f)
		headers = next(f_csv)
		#print(headers)
		lower_headers = [header.lower() for header in headers]
		if ['depedentdbname','dependenttblname','dependent_jobid','createdby','frequency'] == lower_headers:
			
			for row in f_csv:
			
				check_flag = job_check(int(row[2]))
				
				if check_flag:
				
					query="""insert into dependencydtls (depedentdbname, dependenttblname, dependent_jobid, createdby,masterid, frequency)
		values(%r, %r, %d, %r, %d, %r)""" %(row[0], row[1], int(row[2]), row[3], masterid,row[4])
					
					cursor.execute(query)
					conn.commit()
				else: pass
				
		else: print("check the header names again")
		
		
		f.close()
		cursor.close()
		conn.close()


filee = is_csv(sys.argv[1])
masterid=int(sys.argv[2])




if filee and len(sys.argv) == 3 :
	old_or_new = old_or_new(masterid)
	if old_or_new == 'old': old_insert()
	else: new_insert()

else: print("the input file should be only in csv format and 1 input should be present")





		
		
		
		
		
		

	
