from datetime import datetime
x = datetime.now()
b = datetime(2006, 12, 8)
dif = x - b  
seconds = dif.total_seconds()
print(seconds)