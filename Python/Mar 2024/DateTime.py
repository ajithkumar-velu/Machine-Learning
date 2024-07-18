# from datetime import *
# import pytz


# tz_INDIA = pytz.timezone('asia/Kolkata')
# datetime_INDIA = datetime.now(tz_INDIA)
# print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))


#using datetime
'''
from datetime import datetime

print(datetime.now().strftime("%H:%M:%S"))'''

#datetime 
# from datetime import datetime
# print(datetime.now().time())

#time
from time import localtime, strftime
print(strftime("%H:%M:%S"))