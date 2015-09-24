#!/usr/bin/python
from datetime import *
utc_time = datetime(1970, 1, 1) + timedelta(milliseconds=1445484328473)
#1443110400   1443065127345
print(utc_time.strftime("%Y-%m-%d"))