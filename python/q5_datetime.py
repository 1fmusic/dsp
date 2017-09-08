# Hint:  use Google to find python function

####a) 
from datetime import datetime
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
dt1 = datetime.strptime(date_start, '%m-%d-%Y')
dt2 = datetime.strptime(date_stop, '%m-%d-%Y')
days = (int(dt2.day))-(int(dt1.day))

####b)  
from datetime import datetime
date_start = '12312013'  
date_stop = '05282015'  
dt1 = datetime.strptime(date_start, '%m%d%Y')
dt2 = datetime.strptime(date_stop, '%m%d%Y')
d = (dt2-dt1)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
dt1 = datetime.strptime(date_start, '%d-%b-%Y')
dt2 = datetime.strptime(date_stop, '%d-%b-%Y')
d = (dt2-dt1)
