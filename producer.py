

from lib.users import Users
import json
from boto import kinesis

aws_region = "us-west-2"
user = "aguilarcamiloa@gmail.com"
password = "C@milo2011bak3"
interval = 1500
count = 100
stream_name = "TestStream"

u = Users(user, password, interval, count)
x = u.list()
for line in x.iter_lines():
        kinesis = kinesis.connect_to_region(aws_region)
        kinesis.put_record(stream_name, line, "partitionkey")
        if line:
            print (line)