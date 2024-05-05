
import sys
import mysql.connector as c

conn = c.connect(host='localhost', user='root', password='root', database='prod')

cursor = conn.cursor(buffered=True)



def is_csv(input_file):
	
	return input_file.endswith('.csv')



def sql_check(db, tbl):
	
	query = """select count(*) from dependencydtls where masterid=%d and depedentdbname = %r and dependenttblname = %r""" %(masterid, db, tbl)
	
	cursor.execute(query)
	result = cursor.fetchone()
	count = result[0]
	
	return count

def update(roww):
	depedentdbname,dependenttblname,dependent_jobid,createdby,frequency = roww
	
	query = """update dependencydtls set dependent_jobid = %d, createdby = %r, frequency = %r where masterid = %d and depedentdbname = %r and dependenttblname = %r""" %(int(dependent_jobid), createdby, frequency, masterid, depedentdbname, dependenttblname)
	
	cursor.execute(query)
	conn.commit()
	
def insert(roww):
	
	depedentdbname,dependenttblname,dependent_jobid,createdby,frequency = roww
	query = """insert into dependencydtls (depedentdbname, dependenttblname, dependent_jobid, createdby,masterid, frequency)
	values(%r, %r, %d, %r, %d, %r)""" %(depedentdbname,dependenttblname,int(dependent_jobid),createdby,masterid,frequency)
	
	cursor.execute(query)
	conn.commit()


def start():
	
	with open(file_name, 'r') as the_file:
		
		data = the_file.read()
		headers = data.split('\n')[0].replace(' ', '').replace('\r', '').lower()
		data1 = data.split('\n')[1:]
		columns = "depedentdbname,dependenttblname,dependent_jobid,createdby,frequency"
		if columns == headers:
		
			for row in list(data1):
				
				row1 = row.replace(' ', '').replace('\r', '').split(',')
				if len(row1)==1: pass
				else: 
					depedentdbname,dependenttblname,dependent_jobid,createdby,frequency = row1
					status = sql_check(depedentdbname,dependenttblname)
					
					if status > 0:
						update(row1)
					else: 
						insert(row1)
				
			
		
		else: print("the headers are wrong")
		
		
	the_file.close()
	conn.close()
	cursor.close()
	
file_name = sys.argv[1]
masterid = int(sys.argv[2])

flag = is_csv(file_name)

if flag and len(sys.argv) == 3:
	start()
else: print("Input file format is wrong or check the input parameters")




