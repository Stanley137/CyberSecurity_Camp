import base64

s = 'QnJlYWtBTExDVEZ7NTN1c1pRM2hXVzI1ZGNoWjdkWGV9'
print(base64.b64decode(s))
s ='BreakallCTF{happyhackinghighhaaha}'
print(base64.b64encode(s.encode()))